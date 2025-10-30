class Book:
    def __init__(self, book_id, title, author, pages, year_published, status, category,
                 genre=None, subject=None, level=None, field=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.pages = pages
        self.year_published = year_published
        self.status = status
        self.category = category
        self.genre = genre
        self.subject = subject
        self.level = level
        self.field = field

    def add_book(self, db):
        query = """
            INSERT INTO books (title, author, pages, year_published, status, category, genre, subject, level, field)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.title, self.author, self.pages, self.year_published,
            self.status, self.category, self.genre, self.subject, self.level, self.field
        )
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        book_id = cursor.lastrowid
        cursor.close()
        print(f"Đã thêm sách: '{self.title}' với ID là {book_id}")

    def update_book(self, db):
        query = """
            UPDATE books
            SET title = %s, author = %s, pages = %s, year_published = %s,
                status = %s, category = %s, genre = %s, subject = %s, level = %s, field = %s
            WHERE book_id = %s
        """
        params = (self.title, self.author, self.pages, self.year_published,
                  self.status, self.category, self.genre, self.subject, self.level, self.field, self.book_id)
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        cursor.close()

    
    def delete_book(self, db):
        query = "DELETE FROM books WHERE book_id = %s"
        db.execute_query(query, (self.book_id,))
    
    @staticmethod
    def search_book(db, book_id):
        query = "SELECT * FROM books WHERE book_id = %s"
        return db.fetch_one(query, (book_id,))
    

    @staticmethod
    def get_all_books(db):
        query = "SELECT * FROM books"
        return db.fetch_all(query)

    @staticmethod
    def search_book_by_title(db, title):
        query = "SELECT * FROM books WHERE title = %s"
        result = db.fetch_one(query, (title,))
        if result:
            return Book(*result)  # Chuyển tuple thành đối tượng Book
        return None
   

