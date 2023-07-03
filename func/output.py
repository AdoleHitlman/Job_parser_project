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
    elif vacancy["salary"]["to"] is None:
        if not vacancy["salary"]["from"] is None:
            vacancy['salary']["to"] = vacancy['salary']["from"]
        else:
            vacancy['salary']["to"] = ""
        print(f"Зарплата:от {vacancy['salary']['from']} до {vacancy['salary']['to']}")
    elif vacancy["salary"]["from"] is None:
        vacancy['salary']["from"] = 0
        print(f"Зарплата:от {vacancy['salary']['from']} до {vacancy['salary']['to']}")
    else:
        print(f"Зарплата:от {vacancy['salary']['from']} до {vacancy['salary']['to']}")
    if type(vacancy['requirements']) == dict:
        print("Требования:")
        print(
                f"Опыт работы: {vacancy['requirements']['experience']}\n"
                f"Образование: {vacancy['requirements']['education']}\n"
                f"Место работы: {vacancy['requirements']['place_of_work']}\n"
                f"Вакцинация: {vacancy['requirements']['covid']}\n"
                f"Дети: {vacancy['requirements']['kids']}\n"
                f"Передвигаемость: {vacancy['requirements']['moveable']}\n"
                f"Семейное положение: {vacancy['requirements']['maritalstatus']}")
    else:
        print(f"Требования: {vacancy['requirements']}")
    print("\n")


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
