from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import init_db
from controller import contacts

app = FastAPI( title="Contacts API", description="软件工程第一次作业", version="1.0.0" )

origins = [ "http://localhost:5173"]

app.add_middleware( CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=[""], allow_headers=[""],)

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(contacts.router)
@app.get("/")
def read_root():
    return {"message": "欢迎访问通讯录 API !"}