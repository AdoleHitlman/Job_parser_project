import os
from abc import ABC, abstractmethod

import requests

# Получение api
api = os.getenv("SUPER_JOB_API_KEY")

"""
Абстрактный класс
"""


class GetVacancy(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


"""
Основное тело программы
"""


# Класс получения вакансий из Superjob
class SuperJobAPI(GetVacancy):
    def __init__(self):
        pass

    def get_vacancies(self, keyword="python"):
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
                "requirements": {'experience': item['experience']['title'],
                                 "covid": item['covid_vaccination_requirement']['title'],
                                 "moveable": str("Да" if item['moveable'] else "Нет"),
                                 "kids": item['children']["title"],
                                 "education": item["education"]["title"],
                                 'maritalstatus': item['maritalstatus']['title'],
                                 "place_of_work": item["place_of_work"]["title"]}}
            vacancies.append(vacancy)
        return vacancies


# Класс получения вакансий из HeadHunter
class HeadHunterAPI(GetVacancy):
    def __init__(self):
        pass

    def get_vacancies(self, keyword="python"):
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
