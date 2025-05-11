import abc
import json
import os.path
from typing import Any

import requests


class VacanciesApi(abc.ABC):
    @abc.abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """Vacancies by keyword"""
        pass

    @abc.abstractmethod
    def prepare_vacancy(self, json: dict) -> Any:
        """Prepare vacancy fields from response"""
        pass


debug = True


class HH(VacanciesApi):
    """
    Класс для работы с API HeadHunter
    """

    BASE_URL = "https://api.hh.ru"

    def __init__(self) -> None:
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "only_with_salary": True, "order_by": "salary_asc"}

    def get_employers(self) -> list:
        employers_file = "data/empl.json"
        if os.path.isfile(employers_file) and debug:
            with open(employers_file, "r") as f:
                return json.load(f)
        else:
            self.params = {"only_with_vacancies": True}
            response = requests.get(self.BASE_URL + "/employers", headers=self.headers, params=self.params)
            emp_json = response.json()
            if "errors" in emp_json:
                print(f"Error get employers: {emp_json['errors']}")
                return []
            else:
                with open(employers_file, "w") as f:
                    json.dump(emp_json["items"], f, indent=2, ensure_ascii=False)
                return emp_json["items"]

    def get_employer_vacancies(self, employer_ids: list) -> list:
        vacancies_file = "data/vacs.json"
        vacancies = []
        if os.path.isfile(vacancies_file) and debug:
            with open(vacancies_file, "r") as f:
                vacancies = json.load(f)
        else:
            vacancies = []
            for id in employer_ids:
                response = requests.get(self.BASE_URL + "/vacancies", headers=self.headers, params={"employer_id": id})
                empl_json_response = response.json()
                if "errors" in empl_json_response:
                    print(f"Error get employer's {id} vacancies : {empl_json_response['errors']}")
                else:
                    vacancies.extend(empl_json_response["items"])
            with open(vacancies_file, "w") as f:
                json.dump(vacancies, f, indent=2, ensure_ascii=False)
        return list(map(lambda x: self.prepare_vacancy(x), vacancies))

    def get_employers_with_vacancies(self) -> dict:
        """Get employers with vacancies"""
        employers = self.get_employers()
        vacancies = self.get_employer_vacancies(list(map(lambda x: x["id"], employers)))
        return {"employers": employers, "vacancies": vacancies}

    def prepare_vacancy(self, v: dict) -> Any:
        salary = 0
        if "salary" in v and v["salary"]:
            if "from" in v["salary"] and v["salary"]["from"] > 0:
                salary = v["salary"]["from"]
            else:
                salary = v["salary"]["to"]
        return {
            "id": v["id"],
            "name": v["name"],
            "salary": salary,
            "employer": v["employer"]["id"],
            "url": v["alternate_url"] if "url" in v else "",
            "city": v["area"]["name"] if "area" in v else "",
            "requirement": v["snippet"]["requirement"],
            "responsibility": v["snippet"]["responsibility"],
        }

    def load_vacancies(self, keyword: str, per_page: int = 20) -> list:
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        response = requests.get(self.BASE_URL + "/vacancies", headers=self.headers, params=self.params)
        json_response = response.json()
        if "errors" in json_response:
            print(f"'Error get vacancies: {json_response['errors']}'")
            return []
        return json_response.json()["items"]
