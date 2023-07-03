import json

# Класс вакансии
class Vacancy:
    def __init__(self, title, link, salary, requirements):
        self.title = title
        self.link = link
        self.salary = salary
        self.requirements = str(requirements).replace('<highlighttext>1</highlighttext>', '')


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

