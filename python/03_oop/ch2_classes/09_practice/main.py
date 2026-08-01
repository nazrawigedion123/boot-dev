class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title=title
        self.author=author

class Library:
    def __init__(self, name: str) -> None:
        self.name=name
        self.books=[]

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        book_to_keep=[]
        for b in self.books:
            if b.title==book.title and b.author==book.author:
                continue
            else:
                book_to_keep.append(b)
        self.books=book_to_keep

    def search_books(self, search_string: str) -> list[Book]:
        if search_string=="":
            return self.books
        book_res=[]
        for book in self.books:
            if search_string.lower() in book.title.lower():
                book_res.append(book)
            if search_string.lower() in book.author.lower():
                book_res.append(book)
        return book_res

