print('Утилиты библиотеки установлены')

__all__ = ['data_validation', 'formatting']

from .data_validation import validate_book_data
from .formatting import format_book_data