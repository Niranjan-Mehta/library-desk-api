# Library Desk API
Small Python + SQLite library-loan API for AI Competency Assessor testing.
Run with Python 3.10+: `python app.py` (127.0.0.1:8000).
Routes: GET /books, GET /books/{id}, POST /books, GET /loans, POST /loans.
Example book JSON: `{"title":"Clean Code","author":"R. Martin","copies":2}`.
Example loan JSON: `{"book_id":1,"member_name":"Asha"}`.
Layers: app.py (HTTP), library_service.py (business rules), database.py (SQLite), models.py (domain dataclasses).
See docs/library_design.pdf. No authentication, pagination, book-return route or production concurrency controls.
