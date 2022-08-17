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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_default_rating_result1(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        collector.add_new_book(name)
        assert collector.get_book_rating(name) == 1

    def test_add_new_book_the_same_book_twice_result1(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert collector.get_book_rating(name) == 1
    def test_set_book_rating_to_5_result5(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        collector.add_new_book(name)
        collector.set_book_rating(name, 5)
        assert collector.get_book_rating(name) == 5

    def test_set_book_rating_to_outrange0_result1(self):
        collector = BooksCollector()
        name = 'Горе от ума'
        collector.add_new_book(name)
        collector.set_book_rating(name, 0)
        assert collector.get_book_rating(name) == 1

    def test_set_book_rating_to_outrange11_result1(self):
        collector = BooksCollector()
        name = 'The English Patient'
        collector.add_new_book(name)
        collector.set_book_rating(name, 11)
        assert collector.get_book_rating(name) == 1

    def test_set_book_rating_to_nonexisting_book_result_None(self):
        collector = BooksCollector()
        assert collector.set_book_rating('No name', 6) == None

    def test_get_book_rating_for_existing_book_result1(self):
        collector = BooksCollector()
        name = 'The English Patient'
        collector.add_new_book(name)
        collector.set_book_rating(name, 6)
        assert collector.get_book_rating(name) == 6


    def test_get_book_rating_nonexisting_book_result_None(self):
        collector = BooksCollector()
        assert collector.get_book_rating('No name') == None


    def test_get_books_with_specific_rating_2of3books_result2(self):
        collector = BooksCollector()
        rating = 7
        collector.add_new_book('The English Patient')
        collector.add_new_book('Three Steps Above Heaven')
        collector.add_new_book('The Old Man and the Sea')
        collector.set_book_rating('The English Patient', rating)
        collector.set_book_rating('Three Steps Above Heaven', rating)
        collector.set_book_rating('The Old Man and the Sea', 2)
        assert len(collector.get_books_with_specific_rating(rating)) == 2
    def test_add_book_in_favorites_add_existing_book_result1(self):
        collector = BooksCollector()
        name = 'The English Patient'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.get_list_of_favorites_books()[0] == name

    def test_add_book_in_favorites_add_nonexisting_book_result0(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('No name')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_the_same_book_twice_result1(self):
        collector = BooksCollector()
        name = 'The English Patient'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_existing_book_result0(self):
        collector = BooksCollector()
        name = 'The English Patient'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_nonexisting_book_result1(self):
        collector = BooksCollector()
        name = 'The English Patient'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('No name')
        assert len(collector.get_list_of_favorites_books()) == 1