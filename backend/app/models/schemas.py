from pydantic import BaseModel
from datetime import date
from typing import List

class Transaction(BaseModel):
    date: date
    amount: float
    category: str
    merchant: str
    type: str  # Credit / Debit

class AnalyzeRequest(BaseModel):
    purchase_amount: float
