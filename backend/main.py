from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from api.router import router as api_router
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from database import engine
from admin import CategoryAdmin, SubcategoryAdmin, DishAdmin

app = FastAPI(title="UMAI Restaurant Menu API")

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # TODO: Move to environment variables in production
        if username == "admin" and password == "umai2026":
            request.session.update({"token": "admin_token"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        return True

authentication_backend = AdminAuth(secret_key="secret-key-for-umai-menu-admin")

# Setup CORS to allow the Vue frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to UMAI Menu API. Use /api/menu to fetch options."}

# Setup Admin panel
admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(CategoryAdmin)
admin.add_view(SubcategoryAdmin)
admin.add_view(DishAdmin)
