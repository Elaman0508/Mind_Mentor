from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserInDB(UserCreate):
    hashed_password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
