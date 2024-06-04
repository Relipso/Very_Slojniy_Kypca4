import requests
from abc import ABC, abstractmethod


class PapaHH(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        """
        Абстрактный метод для загрузки вакансий по ключевому слову
        """
        pass


class HH(PapaHH):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '',  'area': '113', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        self.params['page'] = 0  # Ensure starting from page 0 for new search
        self.vacancies = []  # Reset vacancies list for new search
        while self.params['page'] < 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                print(f"Ошибка {response.status_code}: {response.text}")
                break
            data = response.json()
            self.vacancies.extend(data.get('items', []))
            if len(data.get('items', [])) == 0:
                break
            self.params['page'] += 1
