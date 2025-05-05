import json

from src.api import HH
from src.filehandler import JSONFileHandler
from src.vacancy import Vacancy

if __name__ == "__main__":
    hh = HH()
    file_handler = JSONFileHandler()
    vacancies = hh.load_vacancies('Python')
    print(vacancies[0]  < vacancies[1])
    file_handler.add_vacancy(vacancies[0])
    file_handler.add_vacancy(vacancies[12])

    vacancies_file = file_handler.get_vacancies()
    for vac in vacancies_file:
        print(json.dumps(vac, indent=2, ensure_ascii=False))
        v = Vacancy(**vac)

    #file_handler.delete_vacancy('120202348')