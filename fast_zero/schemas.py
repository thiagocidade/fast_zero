from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: str
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    type_token: str


class TokenData(BaseModel):
    username: str | None = None
