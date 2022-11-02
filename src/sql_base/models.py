from typing import Optional
from pydantic import BaseModel


class Students(BaseModel):
    id: Optional[int]
    surname: str
    name: str
    phone: str


class Subjects(BaseModel):
    id: Optional[int]
    name: str


class Mark(BaseModel):
    id: Optional[int]
    student_id: int
    subject_id: int
    mark: int