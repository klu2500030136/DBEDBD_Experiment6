from fastapi import APIRouter
from models import Book
from routes.catalog import books

router = APIRouter()

@router.post("/admin/books")
def add_book(book: Book):
    books.append(book.dict())
    return {"message": "Book added successfully"}

@router.put("/admin/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = updated_book.dict()
            return {"message": "Book updated successfully"}

    return {"message": "Book not found"}

@router.delete("/admin/books/{book_id}")
def delete_book(book_id: int):

    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {"message": "Book deleted successfully"}

    return {"message": "Book not found"}