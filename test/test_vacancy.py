from src.vacancy import Vacancy
import pytest


@pytest.fixture
def sample_vacancy():
    """
        Vacancy: Экземпляр класса Vacancy с предопределенными значениями.
    """
    return Vacancy("Software Engineer", "http://example.com",
                   100000, "Develop software", "City")


def test_vacancy_constructor(sample_vacancy):
    """
    Тест для проверки конструктора класса Vacancy.

    Проверяет, что все переданные значения правильно устанавливаются в атрибуты экземпляра.
    """
    assert sample_vacancy.title == "Software Engineer"
    assert sample_vacancy.link == "http://example.com"
    assert sample_vacancy.salary == 100000
    assert sample_vacancy.description == "Develop software"
    assert sample_vacancy.city == "City"


def test_vacancy_constructor_defaults():
    """
    Тест для проверки конструктора класса Vacancy со значениями по умолчанию.

    """
    vacancy = Vacancy("Software Engineer", "http://example.com")
    assert vacancy.title == "Software Engineer"
    assert vacancy.link == "http://example.com"
    assert vacancy.salary == "Зарплата не указана"
    assert vacancy.description is None
    assert vacancy.city == "Город не указан"


def test_vacancy_representation(sample_vacancy):
    """
    Проверяет, что метод __repr__ возвращает строку с правильным форматированием
    и содержимым всех атрибутов экземпляра.
    """
    expected_repr = ("Vacancy(title='Software Engineer', link='http://example.com', "
                     "salary=100000, description='Develop software', city='City')")
    assert repr(sample_vacancy) == expected_repr


def test_vacancy_equality(sample_vacancy):
    """
    Проверяет, что экземпляры с одинаковыми атрибутами считаются равными,
    а экземпляры с разными атрибутами - не равными.
    """
    other_vacancy = Vacancy("Data Scientist", "http://example.com",
                            90000, "Analyze data", "City")
    assert sample_vacancy == sample_vacancy
    assert sample_vacancy != other_vacancy


def test_vacancy_comparison(sample_vacancy):
    """
    Проверяет, что экземпляры вакансий корректно сравниваются по атрибуту salary.
    """
    higher_salary_vacancy = Vacancy("Higher Salary", "http://example.com",
                                    150000, "Higher salary", "City")
    lower_salary_vacancy = Vacancy("Lower Salary", "http://example.com",
                                   50000, "Lower salary", "City")
    assert higher_salary_vacancy > sample_vacancy
    assert lower_salary_vacancy < sample_vacancy
    assert not sample_vacancy > higher_salary_vacancy
    assert not sample_vacancy < lower_salary_vacancy


def test_validate_data():
    """
    Проверяет, что метод validate_data вызывает исключение ValueError, если
    не указаны обязательные атрибуты title и link.
    """
    with pytest.raises(ValueError):
        Vacancy("", "http://example.com").validate_data()
    with pytest.raises(ValueError):
        Vacancy("Software Engineer", "").validate_data()
    with pytest.raises(ValueError):
        Vacancy("", "").validate_data()


def test_vacancy_lt(sample_vacancy):
    """
    Проверяет, что при сравнении экземпляра Vacancy с объектом не являющимся Vacancy,
    вызывается исключение TypeError.
    """
    with pytest.raises(TypeError):
        sample_vacancy < 100
