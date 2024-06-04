from src.api_request import HH
from src.save_json import SaveJSON
from src.operations_path import OPERATIONS_PATH
from src.vacancy import Vacancy


def user_interface():
    hh = HH()
    file_worker = SaveJSON()
    file_path = OPERATIONS_PATH

    while True:
        print("\nВыберите действие:")
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Сохранить вакансии в файл")
        print("4. Загрузить вакансии из файла")
        print("5. Удалить информацию о вакансиях из файла")
        print("6. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            hh.load_vacancies(keyword)
            hh.vacancies = [
                Vacancy(
                    v['name'],
                    v['alternate_url'],
                    v['salary']['from'] if v['salary'] and v['salary']['from'] else "Зарплата не указана",
                    v['snippet']['responsibility'],
                    v['area']['name'] if v['area'] else "Город не указан"
                ) for v in hh.vacancies
            ]
            print(f"Найдено {len(hh.vacancies)} вакансий по запросу '{keyword}'.")

        elif choice == '2':
            n = int(input("Введите количество вакансий для отображения: "))
            hh.vacancies.sort(reverse=True)
            for vacancy in hh.vacancies[:n]:
                print(vacancy)

        elif choice == '3':
            file_worker.save_vacancies(hh.vacancies, file_path)
            print("Вакансии сохранены в файл.")

        elif choice == '4':
            hh.vacancies = file_worker.load_vacancies(file_path)
            print("Вакансии загружены из файла.")

        elif choice == '5':
            file_worker.remove_vacancies(file_path)
            print("Информация о вакансиях удалена из файла.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")
