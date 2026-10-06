# InternTrack API Foundation - Program & Task Catalog API

A read-only REST API built with FastAPI, Pydantic, and Uvicorn serving NeuroFive's internship program structure.

## Features

- Full REST endpoints for programs, weeks, and tasks.
- Strict Pydantic response modeling and status code discipline (200 / 404).
- Built-in pagination support for listing tasks.

## Setup & Execution

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

3. **Access Interactive API Documentation:**

   ```bash
   Open http://127.0.0.1:8000/docs in your browser.
   ```

## API Endpoints & Example curl Commands

1. **List Programs**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/programs' -H 'accept: application/json'
```

2. **List Weeks for a Program**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/programs/backend-web-dev/weeks' -H 'accept: application/json'
```

3. **List Tasks for a Week**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/weeks/week-1/tasks' -H 'accept: application/json'
```

4. **Get Single Task Details**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/tasks/task-1' -H 'accept: application/json'
```

5. **List All Tasks with Pagination**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/tasks?page=1&page_size=10' -H 'accept: application/json'
```
