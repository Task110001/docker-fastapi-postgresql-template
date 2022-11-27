from pydantic import BaseModel, Field
from typing import Optional


class AccountSchema(BaseModel):
    # name: Optional[str]
    login: Optional[str]
    password: Optional[str]
    
    class Config:
        orm_mode = True