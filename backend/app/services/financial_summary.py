import pandas as pd

FIXED_CATEGORIES = {"Rent", "Utilities", "Loan"}

def generate_monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    df["month"] = df["date"].dt.to_period("M")
    summaries = []

    for month, group in df.groupby("month"):
        income = group[group["type"] == "Credit"]["amount"].sum()
        fixed = group[group["category"].isin(FIXED_CATEGORIES)]["amount"].sum()
        discretionary = group[
            (group["type"] == "Debit") &
            (~group["category"].isin(FIXED_CATEGORIES))
        ]["amount"].sum()

        savings = income - fixed - discretionary

        summaries.append({
            "month": str(month),
            "income": income,
            "fixed": fixed,
            "discretionary": discretionary,
            "savings": savings
        })

    return pd.DataFrame(summaries)
