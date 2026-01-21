
from app.services.financial_summary import generate_monthly_summary
from fastapi import APIRouter, UploadFile, File, Form
from app.services.transaction_loader import load_transactions
from app.services.simulator import simulate_large_purchase


router = APIRouter()

@router.post("/analyze")
async def analyze_purchase(
    file: UploadFile = File(...),
    purchase_amount: float = Form(...)
):
    df = load_transactions(file.file)
    summary_df = generate_monthly_summary(df)
    sim_df, risk, min_balance = simulate_large_purchase(
        summary_df, purchase_amount
    )

    original_savings = summary_df.iloc[0]["savings"] if not summary_df.empty else 0
    new_savings = original_savings - purchase_amount

    return {
        "recommendation": "Proceed" if risk == "Safe" else "Caution" if risk == "Caution" else "Not Recommended",
        "summary": f"This purchase would result in a {risk.lower()} financial position. Your lowest balance would be ${min_balance:.2f}.",
        "savings_change": new_savings,
        "lowest_balance": min_balance,
        "risk_level": risk,
        "projection": sim_df.to_dict(orient="records")
    }