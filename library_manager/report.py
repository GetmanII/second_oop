from .utils import validate_book_data, format_book_data

def generate_report(library):
    text_for_report = f"""
Всего книг в библиотеке: {len(library.books)}
Книги, представленные в библиотеке: {library.view_all_books()}
Отчет по книгам:
    """
    print(text_for_report)
    for book in library.books:
        result = validate_book_data(book)
        if result:
            print(format_book_data(book))
        else:
            print("Некорректные данные книги:", book)