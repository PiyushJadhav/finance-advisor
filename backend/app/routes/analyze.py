
from app.services.financial_summary import generate_monthly_summary
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.transaction_loader import load_transactions 
from app.services.simulator import simulate_large_purchase
from app.services.decision_explainer import decision_explainer
from app.services.decision_store import save_decision, get_all_decisions
from app.models.decision_record import DecisionRecord
from app.services.decision_retriever import retrieve_similar_decisions
import traceback


router = APIRouter()

@router.post("/analyze")
async def analyze_purchase(
    file: UploadFile = File(...),
    purchase_amount: float = Form(...)
):
    try:
        df = load_transactions(file.file)
        summary_df = generate_monthly_summary(df)
        sim_df, risk, min_balance = simulate_large_purchase(
            summary_df, purchase_amount
        )

        original_savings = summary_df.iloc[0]["savings"] if not summary_df.empty else 0
        new_savings = original_savings - purchase_amount
        explanation = decision_explainer(purchase_amount,min_balance,new_savings, risk, 500)

        record = DecisionRecord(
            purchase_amount=purchase_amount,
            risk_level=risk,
            lowest_balance=min_balance,
            savings_change=new_savings,
            explanation=explanation
            )  

        save_decision(record)

        
        past_decisions = get_all_decisions()
        similar = retrieve_similar_decisions(purchase_amount, past_decisions)
        
        # Convert numpy types to native Python types for JSON serialization
        return {
            "recommendation": "Proceed" if risk == "Safe" else "Caution" if risk == "Caution" else "Not Recommended",
            "summary": explanation,
            "savings_change": float(new_savings),
            "lowest_balance": float(min_balance),
            "risk_level": risk,
            "projection": [
                {k: float(v) if isinstance(v, (int, float)) else str(v) for k, v in record.items()}
                for record in sim_df.to_dict(orient="records")
            ],
            "similar_decisions": [
                {
                    "purchase_amount": d.purchase_amount,
                    "risk_level": d.risk_level,
                    "outcome": d.explanation
                }
                for d in similar[:3]
            ]
        }
    except Exception as e:
        print(f"Error in analyze_purchase: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=400, detail=f"Error processing request: {str(e)}")