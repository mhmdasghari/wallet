from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


class ServiceValidationError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.http_error_code = HTTP_422_UNPROCESSABLE_ENTITY
        self.errors = errors if errors is not None else []

    def to_json(self):
        return {
            'http_status': self.http_error_code,
            'messages': self.errors
        }
