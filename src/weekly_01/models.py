from typing import Literal
from pydantic import BaseModel, Field

class RestockItem(BaseModel):
    sku: str
    warehouse: str
    quantity: int = Field(gt=0)     
    unit_cost: float = Field(gt=0)
    category: Literal["electronics", "perishable", "apparel", "hardware"]
