from typing import Optional

from fastapi import Request

from services.base_service import BaseService


class UserRegisterService(BaseService):
    def __init__(self, request: Request):
        self.mobile: Optional[str] = None
        self.username: Optional[str] = None
        self.password: Optional[str] = None
        self.birthday: Optional[str] = None
        super().__init__(request=request, contain_form=True)

    def validate(self):
        if not self.username or not len(self.username) > 3:
            self.add_error("Username should be > 3 chars")
        if not self.mobile or not (self.mobile.__len__() == 12):
            self.add_error("Email is required")
        if not self.password or not len(self.password) >= 4:
            self.add_error("Password must be > 4 chars")

    def process(self):
        pass
