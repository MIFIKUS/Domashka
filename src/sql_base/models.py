from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str
    post: Optional[int]
    reg_date: Optional[datetime]



class Students(BaseModel):
    id: Optional[int]
    surname: str
    name: str
    phone: str
    snils: Optional[str]


class Subjects(BaseModel):
    id: Optional[int]
    name: str


class Mark(BaseModel):
    id: Optional[int]
    student_id: int
    subject_id: int
    mark: int