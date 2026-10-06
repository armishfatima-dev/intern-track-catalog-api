from pydantic import BaseModel
from typing import List

class TaskSchema(BaseModel):
    id: str
    title: str
    description: str
    status: str

class WeekSchema(BaseModel):
    id: str
    number: int
    title: str
    tasks: List[TaskSchema]

class ProgramSchema(BaseModel):
    id: str
    title: str
    description: str
    weeks: List[WeekSchema]

class PaginationMeta(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int

class PaginatedTasksResponse(BaseModel):
    data: List[TaskSchema]
    meta: PaginationMeta

