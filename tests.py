import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_add_new_book_add_only_one_unique_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('books, result',
                             [
                                 ['Эта книга в названии которой ровно 40!!!', True],
                                 ['В названии этой книги больше 40 символов!', False]
                             ])
    def test_add_new_book_where_symbol_equally_40_not_add_books_genre_more_40(self, books, result):
        collector = BooksCollector()

        collector.add_new_book(books)

        assert (books in collector.books_genre) == result

    def test_add_new_book_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.books_genre
        assert collector.books_genre['Гордость и предубеждение и зомби'] is ''

    def test_set_book_genre_add_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert 'Ужасы' in collector.books_genre.values()

    def test_get_book_genre_get_genre_by_name(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_get_books_by_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Уголовное право')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Правила ПДД')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Уголовное право', 'Фантастика')
        collector.set_book_genre('Правила ПДД', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Уголовное право', 'Правила ПДД']

    def test_get_books_genre_return_actual_book_ganre(self):
        collector = BooksCollector()

        collector.add_new_book('Уголовное право')
        collector.set_book_genre('Уголовное право', 'Фантастика')

        result = collector.books_genre

        assert result == collector.get_books_genre()

    def test_get_books_for_children_genre_age_rating_not_add_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Сапромат')
        collector.set_book_genre('Сапромат', 'Ужасы')
        collector.add_new_book('Как приручить дракона')
        collector.set_book_genre('Как приручить дракона', 'Мультфильмы')

        books_for_children = collector.get_books_for_children()

        assert 'Как приручить дракона' in books_for_children and 'Сапромат' not in books_for_children

    def test_add_book_in_favorites_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сапромат')
        collector.add_book_in_favorites('Сапромат')

        assert 'Сапромат' in collector.favorites

    def test_add_book_in_favorites_add_again_book_in_favorites_False(self):
        collector = BooksCollector()
        collector.add_new_book('Сапромат')
        collector.add_book_in_favorites('Сапромат')
        collector.add_book_in_favorites('Сапромат')

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Сапромат')
        collector.add_book_in_favorites('Сапромат')
        collector.delete_book_from_favorites('Сапромат')

        assert 'Сапромат' not in collector.favorites

    def test_get_list_of_favorites_books_return_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Сапромат')
        collector.add_new_book('Химия')
        collector.add_book_in_favorites('Сапромат')
        collector.add_book_in_favorites('Химия')

        assert collector.get_list_of_favorites_books() == collector.favorites
