from fastapi import FastAPI

from src.routes import users, auth

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(users.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}
