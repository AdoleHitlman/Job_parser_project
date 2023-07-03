import json

# Класс вакансии
class Vacancy:
    def __init__(self, title, link, salary, requirements):
        self.title = title
        self.link = link
        self.salary = salary
        self.requirements = str(requirements).replace('<highlighttext>', '').replace("</highlighttext>", "")


# Класс взаимодействия с вакансиями
class JSONSaver:
    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)

    def save_to_file(self, file_name="vacancy"):
        # Через file_name="vacancy" не работает
        if file_name == "":
            file_name = "vacancy"
        file_path = '/home/course/course_25.06.23/Job_parser_project/func'
        with open(f"{file_path}/{file_name}.json", "w") as file:
            json.dump(self.vacancies, file)


def sort_vacancies(vacancies):
    for vacancy in vacancies:
        if vacancy['salary'] is None:
            vacancy['salary'] = {"from": 0, "to": 0}
        elif type(vacancy['salary']) == str:
            slr = vacancy['salary'].split("-")
            vacancy['salary'] = {"from": int(slr[1]), "to": int(slr[0])}
        elif type(vacancy['salary']["to"]) == str:
            if len(vacancy['salary']["to"]) == 0:
                vacancy['salary']["to"] = 0
            vacancy['salary']["to"] = int(vacancy['salary']["to"])
        elif vacancy["salary"]["to"] is None:
            vacancy['salary']["to"] = 0
        elif vacancy["salary"]["from"] is None:
            vacancy['salary']["from"] = 0

    sorted_vacancies = sorted(vacancies, key=lambda x: x["salary"]["to"])
    return sorted_vacancies