from abc import abstractmethod, ABC
from typing import List

from utils.exceptions import ServiceValidationError


class BaseService(ABC):
    def __init__(self):
        self.validation_errors = []

    def add_error(self, message: str, error_code: int = 0, fields: List = None):
        self.validation_errors.append({"message": message,
                                       "code": error_code,
                                       "fields": fields if fields is not None else []})

    @abstractmethod
    def validate(self):
        pass

    def check_validations(self):
        if len(self.validation_errors) > 0:
            raise ServiceValidationError("service validation errors", self.validation_errors)

    @abstractmethod
    def process(self):
        pass

    def execute(self):
        try:
            self.validate()
            self.check_validations()
            return self.process()
        except Exception as ex:
            raise ex
