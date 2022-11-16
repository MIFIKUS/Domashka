from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.students import stud_router
from routers.subjects import subj_router
from routers.users import user_pouter


base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}


app.include_router(stud_router, prefix='/students')
app.include_router(subj_router, prefix='/subjects')
app.include_router(user_pouter, prefix='/users')



