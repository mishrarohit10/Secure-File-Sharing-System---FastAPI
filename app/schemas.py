from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId
from enum import Enum

class UserRoles(Enum):
    user = "user"
    admin = "admin"

class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserResponseSchema(UserBaseSchema):
    id: str
    pass

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

class FilteredUserResponse(UserBaseSchema):
    id: str

class FileBaseSchema(BaseModel):
    name: str
    url_token: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True

class CreateFileSchema(FileBaseSchema):
    pass

class FileResponseSchema(BaseModel):
    file_name: str
    file_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class FileResponse(BaseModel):
    message: str
    download_link: str

class FileListResponse(BaseModel):
    files: List[FileResponseSchema]

