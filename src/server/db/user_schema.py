from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserObject(BaseModel):
    id: str
    email: EmailStr
    password: str
    is_active: bool
    is_admin: bool
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class CreateUserResponse(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True


class GetUserRequest(BaseModel):
    id: str

    class Config:
        orm_mode = True


class GetUserResponse(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateUserRequest(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class UpdateUserResponse(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UpdatePasswordRequest(BaseModel):
    id: str
    password: str

    class Config:
        orm_mode = True


class UpdatePasswordResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True


class DeleteUserRequest(BaseModel):
    id: str

    class Config:
        orm_mode = True


class DeleteUserResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class LoginResponse(BaseModel):
    access_token: str

    class Config:
        orm_mode = True
