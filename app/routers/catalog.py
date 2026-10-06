import json
from pathlib import Path
from math import ceil
from typing import List
from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.catalog import (
    ProgramSchema,
    WeekSchema,
    TaskSchema,
    PaginatedTasksResponse,
    PaginationMeta,
)

router = APIRouter(tags=["Catalog"])

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "catalog.json"

def load_catalog_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@router.get("/programs", response_model=List[ProgramSchema], status_code=status.HTTP_200_OK)
def get_programs():
    data = load_catalog_data()
    return data["programs"]

@router.get("/programs/{program_id}/weeks", response_model=List[WeekSchema], status_code=status.HTTP_200_OK)
def get_program_weeks(program_id: str):
    data = load_catalog_data()
    program = next((p for p in data["programs"] if p["id"] == program_id), None)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Program with id '{program_id}' not found."
        )
    return program["weeks"]

@router.get("/weeks/{week_id}/tasks", response_model=List[TaskSchema], status_code=status.HTTP_200_OK)
def get_week_tasks(week_id: str):
    data = load_catalog_data()
    for program in data["programs"]:
        for week in program["weeks"]:
            if week["id"] == week_id:
                return week["tasks"]
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Week with id '{week_id}' not found."
    )

@router.get("/tasks/{task_id}", response_model=TaskSchema, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: str):
    data = load_catalog_data()
    for program in data["programs"]:
        for week in program["weeks"]:
            for task in week["tasks"]:
                if task["id"] == task_id:
                    return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id '{task_id}' not found."
    )

@router.get("/tasks", response_model=PaginatedTasksResponse, status_code=status.HTTP_200_OK)
def list_all_tasks(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=50)
):
    data = load_catalog_data()
    all_tasks = []
    
    for program in data["programs"]:
        for week in program["weeks"]:
            all_tasks.extend(week["tasks"])

    total_count = len(all_tasks)
    total_pages = ceil(total_count / page_size) if total_count > 0 else 1

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_tasks = all_tasks[start_idx:end_idx]

    return PaginatedTasksResponse(
        data=paginated_tasks,
        meta=PaginationMeta(
            total=total_count,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )
    )

