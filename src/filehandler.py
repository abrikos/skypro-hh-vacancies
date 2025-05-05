import json
import os
from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class FileHandler(ABC):
    def __init__(self, filename: str) -> None:
        self._filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, **criteria: Any) -> list:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> None:
        pass


class JSONFileHandler(FileHandler):
    def __init__(self, filename: str = "data/vacancies.json") -> None:
        super().__init__(filename)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Add vacancies to file"""
        vacancies = self.get_vacancies()
        if len([x for x in vacancies if x["id"] == vacancy.id]) > 0:
            print("Vacancy exists")
            return
        vacancies.append(vacancy.to_dict())
        with open(self._filename, "w") as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_vacancies(self, **criteria: Any) -> Any:
        """Get vacancies by criteria"""
        if not os.path.exists(self._filename):
            return []
        with open(self._filename, "r") as f:
            vacancies = json.load(f)
        if criteria:
            filtered_vacancies = []
            for vacancy in vacancies:
                if all(vacancy.get(key) == value for key, value in criteria.items()):
                    filtered_vacancies.append(vacancy)
            return filtered_vacancies
        return vacancies

    def delete_vacancy(self, vacancy_id: str) -> None:
        """Delete vacancy by id"""
        vacancies = self.get_vacancies()
        vacancies = [vacancy for vacancy in vacancies if vacancy.get("id") != vacancy_id]
        with open(self._filename, "w") as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)
