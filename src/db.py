import psycopg2


class DBManager:
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        self._conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname)
        self._cur = self._conn.cursor()

    def clear_db(self) -> None:
        self._cur.execute("DROP TABLE IF EXISTS employers, vacancies")

    def prepare_db(self) -> None:
        with self._conn:
            create_companies_sql = (
                "CREATE TABLE IF NOT EXISTS employers(" "employer_id serial primary key," "name varchar(255)" ");"
            )
            create_vacancies_sql = (
                "CREATE TABLE IF NOT EXISTS vacancies("
                "vacancy_id serial primary key,"
                "name varchar(255),"
                "salary real,"
                "url varchar(255),"
                "city varchar (100),"
                "requirement text,"
                "responsibility text,"
                "employer_id int REFERENCES employers"
                ");"
            )
            self._cur.execute(create_companies_sql + create_vacancies_sql)

    def insert_employers(self, employers: list) -> None:
        """Insert employers to table"""
        sql_employers = "INSERT INTO employers values "
        values = []
        for employer in employers:
            values.append(f"({employer["id"]} , '{employer["name"]}')")
        try:
            self._cur.execute(sql_employers + ",".join(values) + "returning *")
            self._conn.commit()
        except Exception:
            self._cur.execute("rollback")

    def insert_vacancies(self, vacancies: list) -> None:
        """Insert vacancies to table"""
        sql_vacancies = (
            "INSERT INTO vacancies "
            "(vacancy_id, name, employer_id, salary, url, city, requirement, responsibility) values "
        )
        values = []
        for vac in vacancies:
            values.append(
                f"("
                f"{vac["id"]} , "
                f"'{vac["name"]}', "
                f"{vac["employer"]}, "
                f"{vac["salary"]}, "
                f"'{vac["url"]}', "
                f"'{vac["city"]}', "
                f"'{vac["requirement"]}', "
                f"'{vac["responsibility"]}'"
                f")"
            )
        sql_vacancies += ",".join(values) + "returning *"
        try:
            self._cur.execute(sql_vacancies)
            self._conn.commit()
        except Exception:
            self._cur.execute("rollback")

    def get_companies_and_vacancies_count(self) -> list:
        """список всех компаний и количество вакансий у каждой компании"""
        sql = "select e.*, count(*) from employers e inner join vacancies using(employer_id) group by employer_id;"
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except Exception as e:
            self._cur.execute("rollback")
        res = []
        for r in self._cur:
            res.append(r)
        return res

    def get_all_vacancies(self) -> list:
        """список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        sql = "select * from vacancies"
        self._cur.execute(sql)
        res = []
        for r in self._cur:
            res.append(r)
        return res

    def get_avg_salary(self) -> float:
        """средняя зарплата по вакансиям"""
        sql = "select avg(salary) from vacancies"
        self._cur.execute(sql)
        r = self._cur.fetchone()
        return r[0]

    def get_vacancies_with_higher_salary(self) -> list:
        """список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        avg = self.get_avg_salary()
        sql = f"select * from vacancies where salary > {avg}"
        self._cur.execute(sql)
        res = []
        for r in self._cur:
            res.append(r)
        return res

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """список всех вакансий, в названии которых содержатся переданные в метод слова"""
        sql = f"select * from vacancies where lower(name) like '%{keyword.lower()}%'"
        self._cur.execute(sql)
        res = []
        for r in self._cur:
            res.append(r)
        return res

    def print_vacancy(self, vac: tuple) -> None:
        """human representation of vacancy"""
        print(f"Name: {vac[1]}, Salary: {vac[2]}")
