from fastapi import FastAPI

app = FastAPI()

# Fake DB
books= [
    {"id":1, "title":"Harry Potter", "available":True},
    {"id":2, "title":"The Hobbit", "available":True},
    {"id":3, "title":"The best book ever", "available":True},
]

# Home Route
@app.get("/")
def home():
    return {"message":"Norosh's Library API"
            }

# Get all books
@app.get("/books")
def get_books():
    # Connect to DB
    # Run SQL
    # Get output
    # Tidy
    # Format and return
    return books


# get one book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"]==book_id:
            return book
    return {"error": F"Book {book_id} not found"}
