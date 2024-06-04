class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, title, link, salary=None, description=None, city=None):
        self.title = title
        self.link = link
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.city = city if city else "Город не указан"

    def __repr__(self):
        return (f"Vacancy(title='{self.title}', link='{self.link}',"
                f" salary='{self.salary}', description='{self.description}, city='{self.city}')")

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            if self.salary == "Зарплата не указана" and other.salary != "Зарплата не указана":
                return True
            elif self.salary != "Зарплата не указана" and other.salary == "Зарплата не указана":
                return False
            elif self.salary == "Зарплата не указана" and other.salary == "Зарплата не указана":
                return False
            else:
                return self.salary < other.salary
        else:
            raise TypeError("Невозможно сравнить «Вакансия» с объектом, отличным от «Вакансия».")

    def validate_data(self):
        if not self.title or not self.link:
            raise ValueError("На вакансию необходимо указать название и ссылку.")
