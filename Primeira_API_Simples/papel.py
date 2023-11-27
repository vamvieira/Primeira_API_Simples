from fastapi import FastAPI

from controllers.papeis_controller import Papel

from rotas import router

app = FastAPI()

app.include_router(router, prefix="")