def validate_book_data(data: dict) -> bool:
    return "title" in data and "author" in data and "genre" in data
