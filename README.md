# qa_python
# qa_python
Список реализованных тестов

Тестируемый код в файле main.py
Тестовый код в файле tests.py

1. Пример теста test_add_new_book_add_two_books 
- тестируемый метод add_new_book 
- проверяет, что добавилось именно две книги

2. test_add_new_book_add_only_one_unique_book
- тестируемый метод add_new_book
- проверяет, что можно добавить только одну книгу с уникальным названием

3. test_add_new_book_where_symbol_equally_40_not_add_books_genre_more_40
- тестуруемый метод add_new_book
- проверяет, что книги в названий которых более 40 символов добавить в словарь books_genre нельзя
- параметры для теста True - меньше 40 символов, False больше 40 символов

4. test_add_new_book_book_has_no_genre
- тестируемый метод add_new_book
- проверяет, что книга добавляется без жанра

5. test_set_book_genre_add_book_genre
- тестируемый метод set_book_genre
- проверяет, что метод добавляет книге в словарь books_genre жанр

6. test_get_book_genre_get_genre_by_name
- тестируемый метод get_book_genre
- проверяет, что метод возвращает жанр книги по ее названию 

7. test_get_books_with_specific_genre_get_books_by_genre
- теструемый метод get_books_with_specific_genre
- проверяет, что метод возвращает список книг с определенным жанром 

8. test_get_books_genre_return_actual_book_ganre
- тестируемый метод get_books_genre
- проверяет, что метод возвращает словарь books_genre

9. test_get_books_for_children_genre_age_rating_not_add_in_list
- тестируемый метод get_books_for_children
- проверяет, что метод возвращает список книг, жанр которых не содержится в списке genre_age_rating

10. test_add_book_in_favorites_add_book_in_favorites
- тестируемый метод add_book_in_favorites
- проверяет, что метод помещает книгу в словарь favorites 

11. test_add_book_in_favorites_add_again_book_in_favorites_False
- тестируемый метод add_book_in_favorites
- проверяет, что метод не дает повторно добавить книгу словарь favorites

12. test_delete_book_from_favorites_delete_book_from_favorites
- тестируемый метод delete_book_from_favorites
- проверяет, что метод удаляет книгу из словаря favorites, если она там есть

13. test_get_list_of_favorites_books_return_list_of_favorites_books
- тестируемый метод test_get_list_of_favorites_books_return_list_of_favorites_books
- проверяет, что метод возвращает список книг из словаря favorites
