from typing import Any
from unittest.mock import Mock

from src.hh_api import HH


def test_get_wrong_id(mock_session: Any, capfd: Any) -> None:
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
