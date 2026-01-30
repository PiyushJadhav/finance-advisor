def decision_explainer(purchase_amount, lowest_balance, savings_change, risk_level, safety_buffer):
    if risk_level == "Safe":
        return (
            f"This purchase appears financially safe. "
            f"Your lowest projected balance would be ${lowest_balance:.2f}, "
            f"which is comfortably above your safety buffer of ${safety_buffer:.2f}. "
            f"This suggests you can absorb this expense without financial strain."
        )

    if risk_level == "Medium":
        return (
            f"This purchase is possible but requires caution. "
            f"Your projected lowest balance would be ${lowest_balance:.2f}, "
            f"which is close to your safety buffer. "
            f"Consider delaying or reducing discretionary spending."
        )

    return (
        f"This purchase is financially risky. "
        f"Your lowest projected balance would fall below your safety buffer, "
        f"potentially increasing financial stress."
    )

