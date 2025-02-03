# Simple API

The code contain a demo to create health api using FastAPI. 

## Server configration 
- running at localhost:8300 or 127.0.0.1:8300

## To create migration 

```
alembic init alembic

alembic revision --autogenerate -m "create books table"
```

## To apply migration
`alembic upgrade head`


## APIs Included

`GET`: `/heath_api`

**response**
```json
{
  "status": "Server up and running"
}
```

`POST`: `/books/`

**request**
```json
{
    "title": "Sample Book 1",
    "description": "This book is a imaginary book for test entry",
    "author_name": "Saurabh",
    "is_published": false
}
```

**response**
```json
{
    "success": true,
    "message": "Book added successfully",
    "payload": {
        "id": 1,
        "title": "Sample Book 1",
        "description": "This book is a imaginary book for test entry",
        "author": "Saurabh",
        "created_at": "2025-01-06T01:19:26.205171"
    }
}
```

`GET`: `/books/`

**response**
```json
{
    "success": true,
    "message": "Book added successfully",
    "payload": [
        {
            "id": 1,
            "title": "Sample Book 1",
            "description": "This book is a imaginary book for test entry",
            "author": "Saurabh Pandey",
            "created_at": "2025-01-06T01:13:50.192825"
        },
        {
            "id": 2,
            "title": "Sample Book 2",
            "description": "This book is a imaginary book for test entry",
            "author": "Sumit",
            "created_at": "2025-01-06T01:14:05.937272"
        },
        {
            "id": 3,
            "title": "Sample Book 3",
            "description": "This book is a imaginary book for test entry",
            "author": "Aakash",
            "created_at": "2025-01-06T01:14:16.944026"
        },
        {
            "id": 4,
            "title": "Sample Book 4",
            "description": "This book is a imaginary book for test entry",
            "author": "Aakash",
            "created_at": "2025-01-06T01:19:26.205171"
        }
    ]
}
```
