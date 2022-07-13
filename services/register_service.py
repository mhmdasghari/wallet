from typing import Optional

from api.schema.request.register import UserRegister
from services.base_service import BaseService


class UserRegisterService(BaseService):
    def __init__(self, user_model: UserRegister):
        self.mobile = user_model.mobile
        self.username = user_model.username
        self.password = user_model.password
        self.birthday = user_model.birthday
        super().__init__()

    def validate(self):
        if not self.username or not len(self.username) > 3:
            self.add_error("Username should be > 3 chars", fields=["Username"])
        if not self.mobile or not (self.mobile.__len__() == 12):
            self.add_error("Email is required", fields=["Email"])
        if not self.password or not len(self.password) >= 4:
            self.add_error("Password must be > 4 chars", fields=["Password"])

    def process(self):
        return f"{self.mobile}, {self.username}, {self.password}, {self.birthday}"
