from fastapi import FastAPI
from routers import stud_router

app = FastAPI()
app.include_router(stud_router, prefix='/students')

