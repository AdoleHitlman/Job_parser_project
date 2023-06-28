import requests
import json
import os


class HeadHunterAPI:
    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies"
        params = {
            "text": search_query,
            "page": 0,
            "per_page": 20
        }
        response = requests.get(url, params=params)
        data = response.json()
        vacancies = []
        for item in data["items"]:
            vacancy = {
                "title": item["name"],
                "link": item["alternate_url"],
                "salary": item.get("salary", {}),
                "requirements": item["snippet"]["requirement"]
            }
            vacancies.append(vacancy)
        return vacancies


class SuperJobAPI:
    def get_vacancies(self, search_query):
        url = f"https://api.superjob.ru/2.0/vacancies"
        headers = {
            "X-Api-App-Id": os.getenv('SUPER_JOB_API_KEY')
        }
        params = {
            "keyword": search_query,
            "page": 0,
            "count": 20
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        vacancies = []
        for item in data["objects"]:
            vacancy = {
                "title": item["profession"],
                "link": item["link"],
                "salary": item.get("payment_to", "No salary info") + "-" + item.get("payment_from", "No salary info"),
                "requirements": item["candidat"]["requirements"]
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

    def get_vacancies_by_salary(self, salary):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if vacancy.salary == salary]
        return filtered_vacancies

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            json.dump([vars(vacancy) for vacancy in self.vacancies], file)


def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    filtered_vacancies = []
    for vacancy in hh_vacancies + superjob_vacancies:
        if any(word in vacancy["title"] or word in vacancy["requirements"] for word in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def sort_vacancies(vacancies):
    sorted_vacancies = sorted(vacancies, key=lambda x: x["salary"])
    return sorted_vacancies


def get_top_vacancies(vacancies, top_n):
    top_vacancies = vacancies[:top_n]
    return top_vacancies


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(f"Title: {vacancy['title']}")
        print(f"Link: {vacancy['link']}")
        print(f"Salary: {vacancy['salary']}")
        print(f"Requirements: {vacancy['requirements']}")
        print()


def user_interaction():
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh_vacancies = hh_api.get_vacancies(search_query)
    superjob_vacancies = superjob_api.get_vacancies(search_query)
    filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()