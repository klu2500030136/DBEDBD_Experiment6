from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    price: float = Field(..., ge=0)
    status: str
    