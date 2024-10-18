from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str
    confirm_password: str
    terms_agreed: bool
    confirm_password: str
    terms_agreed: bool