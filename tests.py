import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    def test_add_new_book_add_only_one_unique_book(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем две уникальные книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение')

        # Проверяем, что добавилось две уникальные книги
        # Словарь books_genre, который нам возвращает метод add_new_book, имеет длину 2
        assert len(collector.books_genre) == 2



    # дабавили параметризацию проверки с тестовыми данными и ожидаемыми результатами True and False
    @pytest.mark.parametrize('books, result',
    [
        ['Эта книга в названии которой ровно 40!!!', True],
        ['В названии этой книги больше 40 символов!', False]
    ])
    def test_add_new_book_where_symbol_equally_40_not_add_books_genre_more_40(self, books, result):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Передаем параметр
        collector.add_new_book(books)

        # Проверяем, что добавилась книга со параметром True и не добавилась с False
        assert (books in collector.books_genre) == result



    # проверяем, что книга добавляется без жанра
    def test_add_new_book_book_has_no_genre(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу без жанра
        collector.add_new_book('Гордость и предубеждение и зомби')

        # Проверяем, что книга добавлена и у нее нет жанра
        assert 'Гордость и предубеждение и зомби' in collector.books_genre
        assert collector.books_genre['Гордость и предубеждение и зомби'] is ''



    # проверяем, что жанр добавляется в книге
    def test_set_book_genre_add_book_genre(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # Добавляем жанр в книге
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        # Словарь books_genre по ключу name имеет значение 'Ужасы'
        assert 'Ужасы' in collector.books_genre.values()



    # проверяем получение жанра книги по её названию
    def test_get_book_genre_get_genre_by_name(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # Добавляем жанр в книге
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # Проверяяем, что метод get_book_genre возвращает жарн книги
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'



    # проверяем получение списка книг с определённым жанром
    def test_get_books_with_specific_genre_get_books_by_genre(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу и жанр в книге
        collector.add_new_book('Уголовное право')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Правила ПДД')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Уголовное право', 'Фантастика')
        collector.set_book_genre('Правила ПДД', 'Фантастика')

        # Получаем список книги по её жанру
        assert collector.get_books_with_specific_genre('Фантастика') == ['Уголовное право', 'Правила ПДД']



    #проверяем что метод get_books_genre возвращает словарь books_genre

    def test_get_books_genre_return_actual_book_ganre(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу и жанр в книге
        collector.add_new_book('Уголовное право')
        collector.set_book_genre('Уголовное право', 'Фантастика')

        # Получаем текущий словарь
        result = collector.books_genre

        # Проверяем на равенство текущий словарь с полученным методом get_books_genre
        assert result == collector.get_books_genre()



    # проверяем что метод get_books_for_children возвращает список книг
    # жанр которых не содержится в genre_age_rating
    def test_get_books_for_children_genre_age_rating_not_add_in_list(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу и жанр в книге
        collector.add_new_book('Сапромат')
        collector.set_book_genre('Сапромат', 'Ужасы')
        collector.add_new_book('Как приручить дракона')
        collector.set_book_genre('Как приручить дракона', 'Мультфильмы')

        # Создаем переменную, которая хранит значение вернувшееся из метода get_books_for_children
        books_for_children = collector.get_books_for_children()

        # Проверяем, что 'Как приручить дракона' попадает в список книг для детей, а книга с жанром Ужасы нет
        assert 'Как приручить дракона' in books_for_children and 'Сапромат' not in books_for_children



    # Проверяем, что книга попадает с список избранного
    def test_add_book_in_favorites_add_book_in_favorites(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Сапромат')

        # Добавляем книгу в избранное
        collector.add_book_in_favorites('Сапромат')

        # Проверяем что метод add_book_in_favorites добавил книгу в избранное
        assert 'Сапромат' in collector.favorites



    # проверяем что книгу нельзя повторно добавить в избранное
    def test_add_book_in_favorites_add_again_book_in_favorites_False(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Сапромат')

        # Добавляем книгу в избранное
        collector.add_book_in_favorites('Сапромат')

        # Добавляем книгу в избранное повторно
        collector.add_book_in_favorites('Сапромат')

        # Проверяем, что метод add_book_in_favorites повторно не добавляет книгу в избранное
        assert len(collector.favorites) == 1



    # проверяем что при вызове метода delete_book_from_favorites книга удаляется из избранного
    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Сапромат')

        # Добавляем книгу в избранное
        collector.add_book_in_favorites('Сапромат')

        # Удаляем книгу методом delete_book_from_favorites из избранного
        collector.delete_book_from_favorites('Сапромат')

        # Проверяем что книга удалена из списка favorites
        assert 'Сапромат' not in collector.favorites



    # проверяемм что метод get_list_of_favorites_books возвращает список избранных книг
    def test_get_list_of_favorites_books_return_list_of_favorites_books(self):
        # Создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем две уникальные книги
        collector.add_new_book('Сапромат')
        collector.add_new_book('Химия')

        # Добавляем книги в словарь favorites
        collector.add_book_in_favorites('Сапромат')
        collector.add_book_in_favorites('Химия')

        # Проверяем, что метод get_list_of_favorites_books возвращает избранные книги
        assert collector.get_list_of_favorites_books() == collector.favorites



