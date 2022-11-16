from fastapi import APIRouter
from sql_base.models import Students
import resolvers.students

stud_router = APIRouter()


@stud_router.get('/')
def get_students():
    return f'Response: {{text: Страница со списком студентов}}'


@stud_router.post('/')
def new_student(student: Students,):
    new_id = resolvers.students.new_student(student)
    return f'{{code: 201, id: {new_id}}}'


@stud_router.get('/{stud_id}')
def get_student(stud_id: int):
    student = resolvers.get_student(stud_id)
    return f'Student: {{name: имя студена, surname: фамилия, id: {stud_id}}}'


@stud_router.put('/{stud_id}')
def update_student(stud_id: int):
    return f'Update student {stud_id}'


@stud_router.delete('/{stud_id}')
def delelte_student(stud_id: int):
    return f'delete student {stud_id}'