print('Библиотека запущена')


__all__ = ['catalog', 'report']

from .catalog import Library
from .report import generate_report