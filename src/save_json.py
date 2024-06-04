import json
import os
from abc import ABC, abstractmethod
from src.operations_path import OPERATIONS_PATH
from src.vacancy import Vacancy


class PapaSaver(ABC):
    """
    Абстрактный класс для работы с файлом в контексте хранения информации о вакансиях
    """

    @abstractmethod
    def save_vacancies(self, vacancies, file_path):
        """
        Абстрактный метод для сохранения информации о вакансиях в файле
        """
        pass

    @abstractmethod
    def load_vacancies(self, file_path, **kwargs):
        """
        Абстрактный метод для загрузки информации о вакансиях из файла с возможностью фильтрации по указанным критериям
        """
        pass

    @abstractmethod
    def remove_vacancies(self, file_path):
        """
        Абстрактный метод для удаления информации о вакансиях из файла
        """
        pass


class SaveJSON(PapaSaver):
    """
    Класс для сохранения и загрузки информации о вакансиях в JSON-формате
    """

    def save_vacancies(self, vacancies, file_path=OPERATIONS_PATH):
        # Создание директории, если её не существует
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([vars(v) for v in vacancies], file, ensure_ascii=False, indent=4)

    def load_vacancies(self, file_path=OPERATIONS_PATH, **kwargs):
        with open(file_path, 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)
            return [Vacancy(**v) for v in vacancies_data]

    def remove_vacancies(self, file_path=OPERATIONS_PATH):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('')
