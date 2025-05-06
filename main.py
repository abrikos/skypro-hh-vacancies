import json
from typing import Any

from src.api import HH
from src.filehandler import JSONFileHandler
from src.vacancy import Vacancy

if __name__ == "__main__":
    hh = HH()
    file_handler = JSONFileHandler()
    keyword = "Python"


    def print_vacancies(vacs: list) -> None:
        for v in vacs:
            print(v)
            print("-----------")


    def search_by_keyword(kw: str) -> None:
        print_vacancies(hh.load_vacancies(kw))


    def search_top_by_salary(count: int) -> None:
        vacs = hh.load_vacancies(keyword, count)
        vacs.sort(key=lambda x: x.salary, reverse=True)
        print_vacancies(vacs)


    def input_int(prompt: str) -> int:
        try:
            return int(input("Input count of vacancies: "))
        except TypeError:
            print("Wrong input")
            return 0


    def get_saved_vacancies() -> list:
        vacs = file_handler.get_vacancies()
        for v in vacs:
            print(Vacancy(v))
        return vacs


    def add_vacancy_by_id(id):
        v = hh.get_vacancy_by_id(id)
        if v:
            file_handler.add_vacancy(v)


    def search_saved_vacancies(search: str) -> None:
        vacs = file_handler.get_vacancies(search)
        if not len(vacs):
            print('No vacancies found')
            return
        for v in vacs:
            print(v)

    def delete_from_saved(id:str)->None:
        file_handler.delete_vacancy(id)

    while True:
        print("Choose action:")
        print("1. Get vacancies from HH by keyword")
        print("2. Get top N vacancies by salary from HH")
        print("3. Save vacancy to file by ID")
        print("4. Search in saved vacancies")
        print("5. Delete vacancy from file by ID")
        print("6. Exit")

        choice = input("Your choice: ")

        match choice:
            case '1':
                keyword = input("Input keyword: ")
                if keyword:
                    search_by_keyword(keyword)
                else:
                    print('Wrong keyword')

            case '2':
                per_page = input_int("Input count of vacancies: ")
                if per_page:
                    search_top_by_salary(per_page)
                else:
                    print('Wrong count')

            case '3':
                search_id = input("Input vacancy ID to save: ")
                add_vacancy_by_id(search_id)
            case '4':
                search = input('Input search word (empty for list all saved): ')
                search_saved_vacancies(search)

            case '5':
                delete_id = input("Input vacancy ID to delete: ")
                delete_from_saved(delete_id)
            case '6':
                break

