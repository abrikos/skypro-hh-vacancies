from src.filehandler import JSONFileHandler
from src.vacancy import Vacancy


def test_add_vacancy(json_file_handler: JSONFileHandler, vacancy1: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["id"] == "1"


def test_add_duplicate_vacancy(json_file_handler: JSONFileHandler, vacancy1: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.add_vacancy(vacancy1)
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 1


def test_add_notduplicate(json_file_handler: JSONFileHandler, vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.add_vacancy(vacancy2)
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 2


def test_get_vacancies_by_criteria(json_file_handler: JSONFileHandler, vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.add_vacancy(vacancy2)
    filtered_vacancies = json_file_handler.get_vacancies(company="b")
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0]["id"] == "1"


def test_delete_vacancy(json_file_handler: JSONFileHandler, vacancy1: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.delete_vacancy("1")
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 0
