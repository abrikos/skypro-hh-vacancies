from dotenv import load_dotenv
import os
from src.hh_api import HH
from src.db import DBManager

load_dotenv()
db_config = {
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'dbname': os.getenv('POSTGRES_DB')
}

def main():
    hh = HH()
    data = hh.get_employers_with_vacancies()
    db = DBManager(**db_config)
    db.clear_db()
    db.prepare_db()
    db.insert_employers(data["employers"])
    db.insert_vacancies(data["vacancies"])
    vacancies =  db.get_all_vacancies()
    companies = db.get_companies_and_vacancies_count()
    print("==================")
    print("Companies:")
    print("==================")
    for company in companies:
        print(f"Company: {company[1]}. Vacancies: {company[2]}")
    print("==================")
    print("Vacancies:")
    print("==================")
    for vac in vacancies:
        db.print_vacancy(vac)
    avg = db.get_avg_salary()
    print("=================")
    print(f"Average salary: {avg}")
    print("=================")
    print("Vacancies with salary over avg:")
    print("==================")
    higher = db.get_vacancies_with_higher_salary()
    for vac in higher:
        db.print_vacancy(vac)
    keyword = "монтажник"
    print("=================")
    print(f"Vacancies by keyword '{keyword}':")
    print("==================")
    search = db.get_vacancies_with_keyword(keyword)
    for vac in search:
        db.print_vacancy(vac)



if __name__ == "__main__":
    main()

    # def print_vacancies(vacs: list) -> None:
    #     for v in vacs:
    #         print(v)
    #         print("-----------")
    #
    #
    # def search_by_keyword(kw: str) -> None:
    #     print_vacancies(hh.load_vacancies(kw))
    #
    #
    # def search_top_by_salary(count: int) -> None:
    #     vacs = hh.load_vacancies(keyword, count)
    #     vacs.sort(key=lambda x: x.salary, reverse=True)
    #     print_vacancies(vacs)
    #
    #
    # def input_int(prompt: str) -> int:
    #     try:
    #         return int(input("Input count of vacancies: "))
    #     except TypeError:
    #         print("Wrong input")
    #         return 0
    #
    #
    # def get_saved_vacancies() -> list:
    #     vacs = file_handler.get_vacancies()
    #     for v in vacs:
    #         print(Vacancy(v))
    #     return vacs
    #
    #
    # def add_vacancy_by_id(id):
    #     v = hh.get_vacancy_by_id(id)
    #     if v:
    #         file_handler.add_vacancy(v)
    #
    #
    # def search_saved_vacancies(search: str) -> None:
    #     vacs = file_handler.get_vacancies(search)
    #     if not len(vacs):
    #         print('No vacancies found')
    #         return
    #     for v in vacs:
    #         print(v)
    #
    #
    # def delete_from_saved(id: str) -> None:
    #     file_handler.delete_vacancy(id)


