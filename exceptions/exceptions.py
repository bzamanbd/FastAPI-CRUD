from fastapi import HTTPException

class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)

class NotFoundException(CustomException):
    def __init__(self, detail: str = "Not Found"):
        super().__init__(detail=detail, status_code=404)

class ValidationException(CustomException):
    def __init__(self, detail: str = "Validation Error"):
        super().__init__(detail=detail, status_code=422)
