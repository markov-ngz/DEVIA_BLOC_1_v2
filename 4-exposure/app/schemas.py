from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

class UserCreate(BaseModel):
    email: EmailStr
    password : str

class UserOut(BaseModel):
    id: int
    email : EmailStr
    created_at: datetime

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email : EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

class TranslationBase(BaseModel):
    lang_origin: str
    lang_target: str
    text_origin: str
    text_target: str

    class Config:
        orm_mode = True
