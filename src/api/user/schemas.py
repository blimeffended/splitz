from pydantic import BaseModel
from typing import Optional

from db.base_model import Base




# Base model inherent in all classes
class UserBase(BaseModel):
    phone_number: str
    # approved: bool = False


# For 'creating' (POST) a user
class UserCreate(UserBase):
    pass

class UserLogin(UserBase):
    otp: str


# For 'updating' (PUT) a user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None


# For 'reading' (GET) a user
class User(UserBase):
    id: int

    name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    profile_picture_url: Optional[str] = None

    class Config:
        from_attributes = True

class MiniUser(BaseModel):
    id: Optional[int] = None
    name: str

    class Config:
        from_attributes = True

class FriendUser(BaseModel):
    friend_id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class UserUploadProfilePicture(BaseModel):
    user_id: int
    profile_picture: str