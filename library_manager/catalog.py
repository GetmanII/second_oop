class Library:
    books = []
    
    def add_book(self, title: str, author: str, genre: str):
        book = {"title": title, "author": author, "genre": genre}
        self.books.append(book)
        return f'Книга "{title}" добавлена в библиотеку.'
    
    def remove_book(self, title: str):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return f'Книга "{title}" удалена из библиотеки.'
        return f'Книга "{title}" не найдена в библиотеке.'
    
    def search_book(self, title: str, author: str, genre: str):
        for book in self.books:
            if book["title"] == title and book["author"] == author and book["genre"] == genre:
                return f'Книга "{title}" найдена в библиотеке.'
        return f'Книга "{title}" не найдена в библиотеке.'
    
    def view_all_books(self):
        return f'В библиотеке находятся следующие книги: {", ".join([book["title"] for book in self.books])}'