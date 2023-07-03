"""
Вывод на экран
"""


def print_vacancy(vacancy):
    print(f"Вакансия: {vacancy['title']}")
    print(f"Ссылка: {vacancy['link']}")
    if vacancy['salary'] is None:
        print("Зарплата: не указана")
    elif type(vacancy['salary']) == str:
        slr = vacancy['salary'].split("-")
        vacancy['salary'] = {"from": slr[1], "to": slr[0]}
        print(f"Зарплата:от {vacancy['salary']['from']} до {vacancy['salary']['to']}")
    else:
        print(f"Зарплата:от {vacancy['salary']['from']} до {vacancy['salary']['to']}")
    print(f"Требования: {vacancy['requirements']}")
    print()


def main_menu():
    print("Меню:")
    print("1. Вывести вакансии с HH.ru")
    print("2. Вывести вакансии с SuperJob")
    print("3. Вывести вакансии с ключевым словом")
    print("4. Удалить вакансию")
    print("5. Сохранить вакансии?")
    print("0. Выход")
    choice = input("Выберите пункт меню: ")
    return choice

