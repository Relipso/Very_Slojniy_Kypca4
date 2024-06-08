import pytest
from src.user_interface import user_interface
from src.vacancy import Vacancy


class ExampleHH:
    def __init__(self):
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.vacancies = [
            {'name': 'Python Developer', 'alternate_url': 'http://example.com',
             'salary': {'from': 100000}, 'snippet': {'responsibility': 'Develop software'}, 'area': {'name': 'City'}}
        ]


class ExampleSaveJSON:
    def save_vacancies(self, vacancies, file_path):
        pass

    def load_vacancies(self, file_path):
        return [
            Vacancy('Python Developer', 'http://example.com',
                    100000, 'Develop software', 'City')
        ]

    def remove_vacancies(self, file_path):
        pass


@pytest.fixture
def example_hh(monkeypatch):
    example = ExampleHH()
    monkeypatch.setattr('src.user_interface.HH', lambda: example)
    return example


@pytest.fixture
def example_file_worker(monkeypatch):
    example = ExampleSaveJSON()
    monkeypatch.setattr('src.user_interface.SaveJSON', lambda: example)
    return example


@pytest.fixture
def example_input(monkeypatch):
    inputs = []
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    return inputs


@pytest.fixture
def example_print(monkeypatch):
    printed = []
    monkeypatch.setattr('builtins.print', lambda msg: printed.append(msg))
    return printed


def test_user_interface_load_vacancies(example_hh, example_file_worker, example_input, example_print):
    example_input.extend(['1', 'Python', '6'])
    user_interface()
    assert len(example_hh.vacancies) == 1
    assert isinstance(example_hh.vacancies[0], Vacancy)
    assert example_hh.vacancies[0].title == 'Python Developer'
    assert "Найдено 1 вакансий по запросу 'Python'." in example_print


def test_user_interface_save_vacancies(example_hh, example_file_worker, example_input, example_print):
    example_hh.vacancies = [Vacancy('Python Developer', 'http://example.com',
                                 100000, 'Develop software', 'City')]
    example_input.extend(['3', '6'])
    user_interface()
    assert "Вакансии сохранены в файл." in example_print


def test_user_interface_load_vacancies_from_file(example_hh, example_file_worker, example_input, example_print):
    example_input.extend(['4', '6'])
    user_interface()
    assert len(example_hh.vacancies) == 1
    assert example_hh.vacancies[0].title == 'Python Developer'
    assert "Вакансии загружены из файла." in example_print


def test_user_interface_remove_vacancies(example_hh, example_file_worker, example_input, example_print):
    example_input.extend(['5', '6'])
    user_interface()
    assert "Информация о вакансиях удалена из файла." in example_print


def test_user_interface_exit(example_hh, example_file_worker, example_input, example_print):
    example_input.extend(['6'])
    user_interface()
    assert "Выход из программы." in example_print
