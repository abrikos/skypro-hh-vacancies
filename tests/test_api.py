from typing import Any
from unittest.mock import Mock

from src.hh_api import HH


def test_get_wrong_id(mock_session: Any, capfd: Any) -> None:
    hh = HH()
    mock_response = Mock()
    mock_response.json.return_value = {"errors": [{"type": "not_found"}]}
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response


def test_get_vacancies(mock_session: Any, test_data_from_api: Any) -> None:
    hh = HH()
    mock_response = Mock()
    mock_response.json.return_value = test_data_from_api
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies = hh.load_vacancies("Python")
    assert len(vacancies) == 2
    assert vacancies[0].name == "Менеджер чатов (в Яндекс)"
    assert vacancies[0].salary == 30000
    assert vacancies[0].company == "Гончаров Никита Дмитриевич"
    assert vacancies[1].name == "Ученик флориста"
    assert vacancies[1].salary == 0
    assert vacancies[1].company == "Studio Nargiz balloons&Flowers"


def test_empty_vacancies(mock_session: Any) -> None:
    hh = HH()

    mock_response = Mock()
    mock_response.json.return_value = {"items": []}
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies = hh.load_vacancies("Python")

    assert len(vacancies) == 0


def test_get_by_id(mock_session: Any, test_data_from_api: Any) -> None:
    hh = HH()
    mock_response = Mock()
    mock_response.json.return_value = test_data_from_api["items"][0]
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response
    vacancy = hh.get_vacancy_by_id(test_data_from_api["items"][0]["id"])
    assert str(vacancy) == (
        "ID: 119755314\n"
        "        Name: Менеджер чатов (в Яндекс)\n"
        "        City: Москва\n"
        "        Description: Description not set\n"
        "        Company: Гончаров Никита Дмитриевич\n"
        "        Salary: 30000\n"
        "        Link: https://hh.ru/vacancy/119755314"
    )
