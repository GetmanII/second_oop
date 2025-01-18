from library_manager import Library, generate_report


library = Library()

library.add_book("Война и мир", "Лев Толстой", "Роман")
library.add_book("Чапаев и Пустота", "Виктор Пелевин", "Роман")
library.add_book('Капитанская дочка', 'Александр Пушкин', 'Роман')
print(library.search_book("Война и мир", "Лев Толстой", "Роман"))
print(library.remove_book("Война и мир"))
print(library.search_book("Война и мир", "Лев Толстой", "Роман"))
generate_report(library)