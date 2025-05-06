import json
from typing import Any

from src.filehandler import JSONFileHandler
from src.vacancy import Vacancy
from unittest.mock import patch, mock_open


def test_add_vacancy(json_file_handler: JSONFileHandler, test_data_from_json: list, vacancy1: Vacancy) -> None:
    #with patch("builtins.open", mock_open(read_data=json.dumps(test_data_from_json))) as mock_file:
    vacs = json_file_handler.add_vacancy(vacancy1)
    assert len(vacs) == 1
    assert vacs[len(vacs) - 1].id == "1"


def test_add_duplicate_vacancy(json_file_handler: JSONFileHandler, vacancy1: Vacancy, capfd: Any) -> None:
    json_file_handler.add_vacancy(vacancy1)
    out, err = capfd.readouterr()
    json_file_handler.add_vacancy(vacancy1)
    out, err = capfd.readouterr()
    assert out == 'Vacancy exists\n'


def test_add_same(json_file_handler: JSONFileHandler, vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.add_vacancy(vacancy2)
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 2


def test_get_vacancies_by_criteria(json_file_handler: JSONFileHandler, vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.add_vacancy(vacancy2)
    filtered_vacancies = json_file_handler.get_vacancies("b")
    assert len(filtered_vacancies) == 2
    assert filtered_vacancies[0].id == "1"


def test_delete_vacancy(json_file_handler: JSONFileHandler, test_data_from_json: list) -> None:
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data_from_json))) as mock_file:
        vacs = json_file_handler.delete_vacancy('11')
        assert len(vacs) == 1

def test_delete_vacancy_wrong_id(json_file_handler: JSONFileHandler, test_data_from_json: list, capfd:Any) -> None:
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data_from_json))) as mock_file:
        vacs = json_file_handler.delete_vacancy('wrong')
        out, err = capfd.readouterr()
        assert out == "Vacancy with ID:wrong not found\n"

def test_no_file(capfd: Any)->None:
    fh = JSONFileHandler('/not/exists')
    fh.get_vacancies()
    out, err = capfd.readouterr()
    assert out == "File '/not/exists' not exists\n"