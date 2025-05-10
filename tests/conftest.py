import json
from typing import Any
from unittest.mock import patch

import pytest


@pytest.fixture
def mock_session() -> Any:
    with patch("src.hh_api.requests.Session") as mock:
        yield mock


@pytest.fixture()
def test_data_from_json() -> list:
    return [
        {
            "id": "11",
            "name": "Junior Data Engineer",
            "company": "ForteBank",
            "salary": 150000,
            "url": "https://hh.ru/vacancy/120202348",
            "city": "Астана",
            "description": "Сопровождение DataLake. Разработка ETL. Разработка и автоматизация форм отчетности, витрин данных.",
        },
        {
            "id": "12",
            "name": "QA Engineer (middle)",
            "company": "Клируэй Текнолоджис",
            "salary": 20000,
            "url": "https://hh.ru/vacancy/120207758",
            "city": "Москва",
            "description": "Выполнять все виды тестирование: smoke, регресс, новая функциональность, повторное тестирование, участие в ПМИ\\ПСИ и тестирование требований. Вести тестовую документацию...",
        },
    ]


@pytest.fixture
def test_data_from_api() -> dict:
    return {
        "items": [
            {
                "id": "119755314",
                "premium": False,
                "name": "Менеджер чатов (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "salary": {"from": 30000, "to": 77000, "currency": "RUR", "gross": True},
                "salary_range": {
                    "from": 30000,
                    "to": 77000,
                    "currency": "RUR",
                    "gross": True,
                    "mode": {"id": "MONTH", "name": "За месяц"},
                    "frequency": None,
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-04-21T10:39:30+0300",
                "created_at": "2025-04-21T10:39:30+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=119755314",
                "show_logo_in_search": None,
                "show_contacts": True,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/119755314?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/119755314",
                "relations": [],
                "employer": {
                    "id": "4685961",
                    "name": "Гончаров Никита Дмитриевич",
                    "url": "https://api.hh.ru/employers/4685961",
                    "alternate_url": "https://hh.ru/employer/4685961",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1393267.png",
                        "90": "https://img.hhcdn.ru/employer-logo/7192851.png",
                        "240": "https://img.hhcdn.ru/employer-logo/7192852.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4685961",
                    "accredited_it_employer": False,
                    "employer_rating": {"total_rating": "4", "reviews_count": 131},
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Опыт работы не требуется (будет оплачиваемое обучение). Будет плюсом опыт работы на вакансиях:",
                    "responsibility": None,
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
                "working_hours": [{"id": "HOURS_8", "name": "8 часов"}],
                "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
                "night_shifts": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "119920638",
                "premium": False,
                "name": "Ученик флориста",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "159", "name": "Астана", "url": "https://api.hh.ru/areas/159"},
                "salary": None,
                "salary_range": None,
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-04-24T15:27:49+0300",
                "created_at": "2025-04-24T15:27:49+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=119920638",
                "show_logo_in_search": None,
                "show_contacts": False,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/119920638?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/119920638",
                "relations": [],
                "employer": {
                    "id": "10480966",
                    "name": "Studio Nargiz balloons&Flowers",
                    "url": "https://api.hh.ru/employers/10480966",
                    "alternate_url": "https://hh.ru/employer/10480966",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1416527.png",
                        "90": "https://img.hhcdn.ru/employer-logo/7285757.png",
                        "240": "https://img.hhcdn.ru/employer-logo/7285758.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10480966",
                    "accredited_it_employer": False,
                    "employer_rating": None,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Ты будешь учиться и сразу применять знания на практике: помогать в сборке букетов, ухаживать за цветами, оформлять витрины.  ",
                    "responsibility": None,
                },
                "contacts": None,
                "schedule": {"id": "flexible", "name": "Гибкий график"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [{"id": "ON_SITE", "name": "На месте работодателя"}],
                "working_hours": [{"id": "FLEXIBLE", "name": "По договорённости"}],
                "work_schedule_by_days": [{"id": "OTHER", "name": "Другое"}],
                "night_shifts": True,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
        ]
    }
