from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.db.session import engine, Base
from app.api.predictions import router as predictions_router
from app.api.users import router as user_router
from app.api.roles import router as role_router
from app.api.user_roles import router as user_role_router
from app.api.auth import router as auth_router
app = FastAPI(title="Iris Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    predictions_router,
    tags=["Predictions"]
)

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router( role_router)
   
app.include_router(user_role_router)

app.include_router(auth_router)

