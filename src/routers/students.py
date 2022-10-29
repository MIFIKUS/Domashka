from fastapi import APIRouter

stud_router = APIRouter()


@stud_router.get('/')
def get_students():
    return 'Students page'


@stud_router.get('/{stud_id}')
def get_student(stud_id: int):
    return f'Student {stud_id}'


@stud_router.put('/{stud_id}')
def update_student(stud_id: int):
    return f'Update student {stud_id}'


@stud_router.delete('/{stud_id}')
def delelte_student(stud_id: int):
    return f'delete student {stud_id}'