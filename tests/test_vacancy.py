import pytest

from src.vacancy import Vacancy


def test_valid_vacancy(vacancy1: Vacancy) -> None:
    assert vacancy1.name == "a"
    assert vacancy1.company == "b"
    assert vacancy1.salary == 10
    assert vacancy1.url == "http://x.com"


def test_invalid_name(vacancy_wrong: Vacancy) -> None:
    assert vacancy_wrong.name == "Vacancy name not set"
    assert vacancy_wrong.company == "Company name not set"
    assert vacancy_wrong.salary == 0
    assert vacancy_wrong.url == "Wrong URL"
    assert vacancy_wrong.description == "Description not set"


def test_salary_comparison(vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    with pytest.raises(TypeError, match="Wrong type comparison"):
        assert vacancy1 < 10
    with pytest.raises(TypeError, match="Wrong type comparison"):
        assert vacancy1 <= 10
    with pytest.raises(TypeError, match="Wrong type comparison"):
        assert vacancy1 == 10
    with pytest.raises(TypeError, match="Wrong type comparison"):
        assert vacancy1 > 10
    with pytest.raises(TypeError, match="Wrong type comparison"):
        assert vacancy1 >= 10
    with pytest.raises(TypeError, match="Wrong type comparison"):
        assert vacancy1 != 10
    assert vacancy1 < vacancy2
    assert vacancy1 <= vacancy2
    assert vacancy2 > vacancy1
    assert vacancy2 >= vacancy1
    assert not (vacancy1 == vacancy2)
    assert vacancy1 == vacancy1
    assert vacancy1 != vacancy2


def test_to_string(vacancy1: Vacancy) -> None:
    assert str(vacancy1) == (
        "ID: 1\n"
        "        Name: a\n"
        "        City: Y\n"
        "        Description: AA\n"
        "        Company: b\n"
        "        Salary: 10\n"
        "        Link: http://x.com"
    )
