from datetime import datetime
from pydantic import BaseModel


class SDataIn(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: str

    class Config:
        from_attributes = True


class SDataOut(BaseModel):
    dataset: list
    labels: list

    class Config:
        from_attributes = True
