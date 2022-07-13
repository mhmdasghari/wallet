from typing import Optional

from pydantic import BaseModel


class UserRegister(BaseModel):
    mobile: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    birthday: Optional[str] = None
