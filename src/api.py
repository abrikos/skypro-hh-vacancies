import abc
from typing import Any

import requests

from src.vacancy import Vacancy


class VacanciesApi(abc.ABC):
    @abc.abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """Vacancies by keyword"""
        pass

    @abc.abstractmethod
    def _connect(self) -> Any:
        """Connect to API"""
        pass


class HH(VacanciesApi):
    """
    Класс для работы с API HeadHunter
    """

    BASE_URL = "https://api.hh.ru/vacancies"

    def _connect(self) -> Any:
        self.__session = requests.Session()
        response = self.__session.get(self.BASE_URL)
        response.raise_for_status()
        return response

    def __init__(self) -> None:
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 20, "only_with_salary": 1}

    def load_vacancies(self, keyword: str) -> list:
        self._connect()
        self.params["text"] = keyword
        response = self.__session.get(self.BASE_URL, headers=self.headers, params=self.params)
        vacancies = response.json()["items"]
        result = []
        for v in vacancies:
            salary = 0 if not v["salary"] else v["salary"]["from"] or v["salary"]["to"]
            result.append(
                Vacancy(
                    v["id"],
                    v["name"],
                    v["employer"]["name"],
                    salary,
                    v["alternate_url"],
                    v["area"]["name"],
                    v["snippet"]["responsibility"],
                )
            )
        return result
