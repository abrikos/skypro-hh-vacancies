import abc
import json
from typing import Any

import requests

from src.vacancy import Vacancy


class VacanciesApi(abc.ABC):
    @abc.abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """Vacancies by keyword"""
        pass

    @abc.abstractmethod
    def get_vacancy_by_id(self, id: str) -> list:
        """Vacancy by ID"""
        pass

    @abc.abstractmethod
    def _connect(self) -> Any:
        """Connect to API"""
        pass

    @abc.abstractmethod
    def _prepare_vacancy(self, json: dict) -> Any:
        """Prepare vacancy fields from response"""
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
        self.params = {"text": "", "page": 0, "only_with_salary": True, "order_by": "salary_asc"}

    def _prepare_vacancy(self, v: dict) -> Any:
        salary = 0
        if "salary" in v and v["salary"]:
            if "from" in v["salary"] and v["salary"]["from"]>0:
                salary = v["salary"]["from"]
            else:
                salary = v["salary"]["to"]
        return {"id":v["id"],
                "name":v["name"],
                "company":v["employer"]["name"]  if "employer" in v else "",
                "salary":salary,
                "url":v["alternate_url"]  if "url" in v else "",
                "city":v["area"]["name"]  if "area" in v else "",
                "description":v["description"] if "description" in v else ""
                }

    def get_vacancy_by_id(self, id: str) -> (Vacancy, None):
        self._connect()
        response = self.__session.get(self.BASE_URL + '/' + id, headers=self.headers, params=self.params)
        json_response = response.json()
        if "errors"in json_response:
            print(f"'Error get vacancy with id '{id}': {json_response['errors']}'")
            return None
        args = self._prepare_vacancy(json_response)
        return Vacancy(args)

    def load_vacancies(self, keyword: str, per_page=20) -> list:
        self._connect()
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        response = self.__session.get(self.BASE_URL, headers=self.headers, params=self.params)
        vacancies = response.json()["items"]
        result = []
        for v in vacancies:
            result.append(Vacancy(self._prepare_vacancy(v)))
        return result
