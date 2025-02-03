from src.models.books import Books
class BooksController():
    def __init__(self, db_session):
        self.db = db_session

    def add_book(self, book_info):
        print (book_info)
        new_book = Books(**book_info)
        try:
            self.db.add(new_book)
            self.db.commit()
            self.db.refresh(new_book)
        except Exception as e:
            print (e)
            self.db.rollback()
            return {"success": False, "message": "Unable to add book", "payload": None}

        return {"success": True, "message": "Book added successfully", "payload": {
            "id": new_book.id,
            "title": new_book.title,
            "description": new_book.description,
            "author": new_book.author_name,
            "created_at": new_book.created_at
        }}

    def get_all_books(self):
        all_books = self.db.query(Books).all()
        resp = []
        for book in all_books:
            resp.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "description": book.description,
                    "author": book.author_name,
                    "created_at": book.created_at
                }
            )
        return {"success": True, "message": "Book added successfully", "payload": resp}
