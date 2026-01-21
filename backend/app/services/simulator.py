def simulate_large_purchase(summary_df, purchase_amount, safety_buffer=500):
    df = summary_df.copy()
    df.loc[0, "discretionary"] += purchase_amount
    df["balance"] = df["income"] - df["fixed"] - df["discretionary"]

    min_balance = df["balance"].min()

    if min_balance > safety_buffer * 2:
        risk = "Safe"
    elif min_balance > safety_buffer:
        risk = "Caution"
    else:
        risk = "Risky"

    return df, risk, min_balance
