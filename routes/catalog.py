from fastapi import APIRouter

router = APIRouter()

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Doe",
        "isbn": "ISBN101",
        "price": 500,
        "status": "Available"
    },
    {
        "id": 2,
        "title": "Database Systems",
        "author": "Jane Smith",
        "isbn": "ISBN102",
        "price": 700,
        "status": "Available"
    }
]

@router.get("/books")
def get_books():
    return books

@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}