import json
import os
from abc import ABC, abstractmethod

import requests

input("для начала нажмите 'enter'")
api = os.getenv("SUPER_JOB_API_KEY")


class GetVacancy(ABC):

    @abstractmethod
    def get_vacancies_sj(self):
        pass

    @abstractmethod
    def get_vacancies_hh(self):
        pass


class SuperJobAPI(GetVacancy):
    def __init__(self):
        pass

    def get_vacancies_sj(self, keyword="python"):
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {
            "count": 100,
            "page": 0,
            "keyword": keyword,
            "archive": False,
        }
        headers = {
            "X-Api-App-Id": api
        }
        response = requests.get(url, headers=headers, params=params).json()
        vacancies = []

        for item in response["objects"]:
            vacancy = {
                "title": item["profession"],
                "link": item["link"],
                "salary": str(item.get("payment_to", "No salary info")) + "-" + str(
                    item.get("payment_from", "No salary info")),
                "requirements": {"Опыт работы": str(item['experience']['title']),
                                 "Вакцинация": str(item['covid_vaccination_requirement']['title']),
                                 "Передвигаемость": str("Да" if item['moveable'] else "Нет"),
                                 "Дети": str(item['children']['title']),
                                 "Образование": str(item["education"]["title"]),
                                 "Семейное положение": str(item['maritalstatus']['title']),
                                 "Место работы": str(item["place_of_work"]["title"])}
            }
            vacancies.append(vacancy)
        return vacancies

    def get_vacancies_hh(self):
        pass


class HeadHunterAPI(GetVacancy):
    def __init__(self):
        pass

    def get_vacancies_sj(self):
        pass

    def get_vacancies_hh(self, keyword="python"):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': keyword,
            'area': '1',
            'per_page': 100,
            'archived': False
        }

        response = requests.get(url, params=params).json()
        vacancies = []
        for item in response["items"]:
            vacancy = {
                "title": item["name"],
                "link": item["alternate_url"],
                "salary": item.get("salary", {}),
                "requirements": item["snippet"]["requirement"],
            }
            vacancies.append(vacancy)
        return vacancies


class Vacancy:
    def __init__(self, title, link, salary, requirements):
        self.title = title
        self.link = link
        self.salary = salary
        self.requirements = requirements


class JSONSaver:
    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            for vacancy in self.vacancies:
                json.dump(vacancy, file)


def print_vacancy(vacancy):
    print(f"Вакансия: {vacancy['title']}")
    print(f"Ссылка: {vacancy['link']}")
    if vacancy['salary'] == None:
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


vacancy_storage = JSONSaver()


def choice_one(hh_api):
    keyword = input("Введите ключевое слово для поиска: ")
    top_n = input("Введите количество вакансий для вывода в топ: ")
    vacancies = hh_api.get_vacancies_hh(keyword)
    counter = 0
    for vacancy_data in vacancies:
        if counter < int(top_n):
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                    salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                           "requirements": vacancy_class.requirements}

            print_vacancy(vacancy_dir)

    answer = input("Добавить вакансии?\nНапишите:'Да' или 'Нет'").lower()
    if answer == "да":
        for vacancy_data in vacancies:
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                        salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                               "requirements": vacancy_class.requirements}
            vacancy_storage.add_vacancy(vacancy_dir)
        print("Вакансии успешно добавлены")


def choice_two(superjob_api):
    keyword = input("Введите ключевое слово для поиска: ")
    vacancies = superjob_api.get_vacancies_sj(keyword)
    for vacancy_data in vacancies:
        vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
        vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                       "requirements": vacancy_class.requirements}
        print_vacancy(vacancy_dir)

    answer = input("Добавить вакансии?\nНапишите:'Да' или 'Нет'").lower()
    if answer == "да":
        for vacancy_data in vacancies:
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                    salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                           "requirements": vacancy_class.requirements}
            vacancy_storage.add_vacancy(vacancy_dir)
        print("Вакансии успешно добавлены")


def choice_three(hh_api, superjob_api):
    keyword = input("Введите ключевое слово для поиска: ")
    vacancies = [*superjob_api.get_vacancies_sj(keyword), *hh_api.get_vacancies_hh(keyword)]
    for vacancy_data in vacancies:
        vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
        vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                       "requirements": vacancy_class.requirements}
        print_vacancy(vacancy_dir)

    answer = input("Добавить вакансии?\nНапишите:'Да' или 'Нет'").lower()
    if answer == "да":
        for vacancy_data in vacancies:
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                    salary=vacancy_data['salary'],
                                    requirements=str(vacancy_data["requirements"]).replace(
                                        '<highlighttext>1</highlighttext>', ''))
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                           "requirements": vacancy_class.requirements}
            vacancy_storage.add_vacancy(vacancy_dir)
        print("Вакансии успешно добавлены")


def coice_four():
    count = []
    while True:
        for counter in range(len(vacancy_storage.vacancies)):
            salary = {"from": "???", "to": "???"}
            if vacancy_storage.vacancies[counter]["salary"] != None:
                salary = vacancy_storage.vacancies[counter]["salary"]
            print(f"{counter + 1}|Вакансия:{vacancy_storage.vacancies[counter]['title']}\n"
                  f"Ссылка: {vacancy_storage.vacancies[counter]['link']}\n"
                  f"Зарплата:от {salary['from']} до {salary['to']}\n"
                  f"Зарплата:от{vacancy_storage.vacancies[counter]['requirements']}\n")
            count.append(counter + 1)
        print(count)
        choice_to_del = input("Введите номер вакансии которую хотите удалить:")

        if choice_to_del not in count:
            input_usr = input("Не удалось найти вакансию с таким номером\nХотите Выйти?").lower()
            if input_usr == "да":
                break
        else:
            vacancy_storage.delete_vacancy(vacancy_storage.vacancies[int(choice_to_del) - 1])
            print("Вакансия успешно удалена")
            break


def choice_five():
    vacancy_storage.save_to_file(input("Введите название файла:"))


def end_question():
    while True:
        back = input("Вернуться в меню?\nНапишите:'Да' или 'Нет'").lower()
        if back == "нет":
            return False
        elif back == "да":
            return True
        else:
            print("Нет такого варианта ответа")


def user_interaction():
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    while True:
        choice = main_menu()
        if choice == '1':
            choice_one(hh_api)
            if not end_question():
                break
        elif choice == "2":
            choice_two(superjob_api)
            if not end_question():
                break
        elif choice == "3":
            choice_three(hh_api, superjob_api)
            if not end_question():
                break
        elif choice == "4":
            coice_four()
            if not end_question():
                break
        elif choice == "5":
            choice_five()
            if not end_question():
                break
        elif choice == "0":
            break


if __name__ == "__main__":
    user_interaction()
    input()
