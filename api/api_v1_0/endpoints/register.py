from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from api.schema.request.register import UserRegister
from services.register_service import UserRegisterService

router = APIRouter()


@router.post("/register/", response_class=HTMLResponse)
def register(user_model: UserRegister):
    user_data = UserRegisterService(user_model=user_model).process()
    return f"""
    <html>
        <head>
            <title>Register Data</title>
        </head>
        <body>
            <h1>{user_data}</h1>
        </body>
    </html>
    """
