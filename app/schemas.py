from pydantic import BaseModel
from datetime import date
from typing import Optional

class RateInput(BaseModel):
    date: date
    rate: float

class RateOutput(BaseModel):
    date: date
    rate: float
    change_pct: Optional[float]