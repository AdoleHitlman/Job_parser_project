from output import print_vacancy
from vacancy_saver import Vacancy, JSONSaver, sort_vacancies

"""
Взаимодействие с пользователем
"""
# Создание экземпляра класса JSONSaver
vacancy_storage = JSONSaver()


# Выбор перовго пункта меню
def choice_one(hh_api):
    keyword = input("Введите ключевое слово для поиска: ")
    top_n = ""
    while not type(top_n) == int:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ n: "))
        except ValueError:
            print("Надо ввести цифру")
    vacancies = hh_api.get_vacancies(keyword)
    counter = 0
    for vacancy_data in vacancies:
        if counter < int(top_n):
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                    salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                           "requirements": vacancy_class.requirements}

            print_vacancy(vacancy_dir)
            counter += 1
    answer = 0
    while answer != 3:
        answer = int(input("Выберете что сделать с вакансиями\n1:Отсортировать\n2:Добавить в список вакансий\n3:Выход"))
        if answer == 2:
            counter = 0
            for vacancy_data in vacancies:
                if counter < int(top_n):
                    vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                        salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
                    vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                               "requirements": vacancy_class.requirements}
                    vacancy_storage.add_vacancy(vacancy_dir)
                    counter += 1
            print("Вакансии успешно добавлены")
        elif answer == 1:
            counter = 0
            vacancises_to_sort = []
            for vacancy_data in vacancies:
                if counter < top_n:
                    vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
                    vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                       "requirements": vacancy_class.requirements}
                    vacancises_to_sort.append(vacancy_dir)
                    counter += 1
            for vacancy in sort_vacancies(vacancises_to_sort):
                counter = 0
                if counter < top_n:
                    print_vacancy(vacancy)
                    counter +=1



# Выбор второго пункта меню
def choice_two(superjob_api):
    keyword = input("Введите ключевое слово для поиска: ")
    top_n = ""
    while not type(top_n) == int:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ n: "))
        except ValueError:
            print("Надо ввести цифру")
    vacancies = superjob_api.get_vacancies(keyword)
    counter = 0
    for vacancy_data in vacancies:
        if counter < int(top_n):
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                    salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                           "requirements": vacancy_class.requirements}
            print_vacancy(vacancy_dir)
            counter += 1
    answer = 0
    while answer != 3:
        answer = int(input("Выберете что сделать с вакансиями\n1:Отсортировать\n2:Добавить в список вакансий\n3:Выход"))
        if answer == 2:
            counter = 0
            for vacancy_data in vacancies:
                if counter < int(top_n):
                    vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                            salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
                    vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link,
                                   'salary': vacancy_class.salary,
                                   "requirements": vacancy_class.requirements}
                    vacancy_storage.add_vacancy(vacancy_dir)
                    counter += 1
            print("Вакансии успешно добавлены")
        elif answer == 1:
            counter = 0
            vacancises_to_sort = []
            for vacancy_data in vacancies:
                if counter < top_n:
                    vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                            salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
                    vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link,
                                   'salary': vacancy_class.salary,
                                   "requirements": vacancy_class.requirements}
                    vacancises_to_sort.append(vacancy_dir)
                    counter += 1
            for vacancy in sort_vacancies(vacancises_to_sort):
                counter = 0
                if counter < top_n:
                    print_vacancy(vacancy)
                    counter += 1


# Выбор третьего пункта меню
def choice_three(hh_api, superjob_api):
    keyword = input("Введите ключевое слово для поиска: ")
    top_n = ""
    while not type(top_n) == int:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ n: "))
        except ValueError:
            print("Надо ввести цифру")
    vacancies = [*superjob_api.get_vacancies(keyword), *hh_api.get_vacancies(keyword)]
    counter = 0
    for vacancy_data in vacancies:
        if counter < int(top_n):
            vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                    salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
            vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link, 'salary': vacancy_class.salary,
                           "requirements": vacancy_class.requirements}
            print_vacancy(vacancy_dir)
            counter += 1

    answer = 0
    while answer != 3:
        answer = int(input("Выберете что сделать с вакансиями\n1:Отсортировать\n2:Добавить в список вакансий\n3:Выход"))
        if answer == 2:
            counter = 0
            for vacancy_data in vacancies:
                if counter < int(top_n):
                    vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                            salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
                    vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link,
                                   'salary': vacancy_class.salary,
                                   "requirements": vacancy_class.requirements}
                    vacancy_storage.add_vacancy(vacancy_dir)
                    counter += 1
            print("Вакансии успешно добавлены")
        elif answer == 1:
            counter = 0
            vacancises_to_sort = []
            for vacancy_data in vacancies:
                if counter < top_n:
                    vacancy_class = Vacancy(title=vacancy_data['title'], link=vacancy_data['link'],
                                            salary=vacancy_data['salary'], requirements=vacancy_data["requirements"])
                    vacancy_dir = {'title': vacancy_class.title, 'link': vacancy_class.link,
                                   'salary': vacancy_class.salary,
                                   "requirements": vacancy_class.requirements}
                    vacancises_to_sort.append(vacancy_dir)
                    counter += 1
            for vacancy in sort_vacancies(vacancises_to_sort):
                counter = 0
                if counter < top_n:
                    print_vacancy(vacancy)
                    counter += 1


# Выбор четвёртого пункта меню
def coice_four():
    while True:
        indexes = []
        for counter in range(len(vacancy_storage.vacancies)):
            print(counter + 1, "|")
            print_vacancy(vacancy_storage.vacancies[counter])
            indexes.append(counter)

        choice_to_del = int(input("Введите номер вакансии которую хотите удалить:")) - 1

        if choice_to_del not in indexes:
            input_usr = input("Не удалось найти вакансию с таким номером\nХотите Выйти?").lower()
            if input_usr == "да":
                break
        else:
            vacancy_storage.delete_vacancy(vacancy_storage.vacancies[int(choice_to_del)])
            print("Вакансия успешно удалена")
            break


# Выбор пятого пункта меню
def choice_five():
    vacancy_storage.save_to_file(input("Введите название файла:"))


# Возврат в меню
def end_question():
    while True:
        back = input("Вернуться в меню?\nНапишите:'Да' или 'Нет'").lower()
        if back == "нет":
            return False
        elif back == "да":
            return True
        else:
            print("Нет такого варианта ответа")