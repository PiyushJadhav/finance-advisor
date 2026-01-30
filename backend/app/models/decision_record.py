from dataclasses import dataclass

@dataclass
class DecisionRecord:
    purchase_amount: float
    risk_level: str
    lowest_balance: float
    savings_change: float
    explanation: str
