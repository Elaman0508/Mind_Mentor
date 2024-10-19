from pydantic import BaseModel, EmailStr

# Schemas for user creation, login, update, and response

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str
    terms_agreed: bool

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: str
    password: str = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
