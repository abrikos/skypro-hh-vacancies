import json
import os
import sys
from abc import ABC, abstractmethod
from math import trunc
from typing import Any

from src.vacancy import Vacancy


class FileHandler(ABC):
    def __init__(self, filename: str) -> None:
        self._filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Add vacancies to file"""
        pass

    @abstractmethod
    def get_vacancies(self, **criteria: Any) -> list:
        """Get vacancies by criteria"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> None:
        """Delete vacancy by id"""
        pass


class JSONFileHandler(FileHandler):
    def __init__(self, filename: str = "data/vacancies.json") -> None:
        super().__init__(os.path.join(sys.path[1],filename))

    def add_vacancy(self, vacancy: Vacancy) -> list:
        vacancies = self.get_vacancies()
        if len([x for x in vacancies if x.id == vacancy.id]) > 0:
            print("Vacancy exists")
            return vacancies
        vacancies.append(vacancy)
        with open(self._filename, "w") as f:
            json.dump(list(map(lambda x: x.to_dict(), vacancies)), f, indent=4, ensure_ascii=False)
        return vacancies

    def get_vacancies(self, search:str="") -> Any:
        if not os.path.exists(self._filename):
            print(f"File '{self._filename}' not exists")
            return []
        with open(self._filename, "r") as f:
            vacancies_json = json.load(f)
        if search:
            fields = list(map(lambda x: x.replace('_', ''), Vacancy.__slots__))
            fields.remove('salary')
            filtered_vacancies = []
            for vacancy_json in vacancies_json:
                add_to_filtered = False
                for f in fields:
                    if vacancy_json.get(f).lower().find(search.lower())>=0:
                        add_to_filtered = True
                        break
                if add_to_filtered:
                    filtered_vacancies.append(Vacancy(vacancy_json))
            return filtered_vacancies
        return list(map(lambda x: Vacancy(x), vacancies_json))

    def delete_vacancy(self, vacancy_id: str) -> list:
        vacancies = self.get_vacancies()
        found_vacancy = None
        for v in vacancies:
            if v.id==vacancy_id:
                found_vacancy = v
        if found_vacancy:
            vacancies = [vacancy for vacancy in vacancies if vacancy.id != found_vacancy.id]
            with open(self._filename, "w") as f:
                json.dump(list(map(lambda x: x.to_dict(), vacancies)), f, indent=4, ensure_ascii=False)
            print(f"Vacancy {vacancy_id} deleted")
        else:
            print(f"Vacancy with ID:{vacancy_id} not found")
        return vacancies
