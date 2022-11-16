from sql_base import base_worker
from sql_base import models


def new_student(student: models.Students) -> int:
    new_id = base_worker.execute("INSERT INTO students(surname, name, phone) "
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (student.surname, student.name, student.phone))
    return new_id
