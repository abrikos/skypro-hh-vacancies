from typing import Callable


class Vacancy:
    __slots__ = ("_id", "_name", "_company","_salary","_url","_city","_description")

    def __init__(self, args) -> None:
        self._id = args['id']
        self._name = self.__validate_name(args['name'])
        self._company = self.__validate_company(args['company'])
        self._salary = self.__validate_salary(args['salary'])
        self._url = self.__validate_url(args['url'])
        self._city = self.__validate_city(args['city'])
        self._description = self.__validate_description(args['description'])

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def company(self) -> str:
        return self._company

    @property
    def salary(self) -> float:
        return self._salary

    @property
    def url(self) -> str:
        return self._url

    @property
    def city(self) -> str:
        return self._city

    @property
    def description(self) -> str:
        return self._description

    def __validate_description(self, value: str) -> str:
        """Description validation"""
        if not isinstance(value, str) or not value:
            return "Description not set"
        return value

    def __validate_city(self, value: str) -> str:
        """City validation"""
        if not isinstance(value, str) or not value:
            return "City name not set"
        return value

    def __validate_name(self, name: str) -> str:
        """Name validation"""
        if not isinstance(name, str) or not name:
            return "Vacancy name not set"
        return name

    def __validate_company(self, company: str) -> str:
        """Company validation"""
        if not isinstance(company, str) or not company:
            return "Company name not set"
        return company

    def __validate_salary(self, salary: int) -> int:
        """Salary validation"""
        if not isinstance(salary, int) or salary < 0:
            return 0
        return salary

    def __validate_url(self, url: str) -> str:
        """URL validation"""
        if not isinstance(url, str) or not url.startswith("http"):
            return "Wrong URL"
        return url

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return self.salary < other.salary

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return self.salary <= other.salary

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return self.salary == other.salary

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return self.salary != other.salary

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return self.salary > other.salary

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return self.salary >= other.salary

    def __str__(self) -> str:
        return f"""ID: {self._id}
        Name: {self.name}
        City: {self.city}
        Description: {self.description}
        Company: {self.company}
        Salary: {self.salary}
        Link: {self.url}"""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "company": self.company,
            "salary": self.salary,
            "url": self.url,
            "city": self.city,
            "description": self.description,
        }
