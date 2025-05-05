class Vacancy:
    __slots__ = ("_id", "_name", "_company", "_salary", "_url", "_city", "_description")

    def __init__(object, id: str, name: str, company: str, salary: int, url: str, city: str, description: str) -> None:
        object._id = id
        object._name = object.__validate_name(name)
        object._company = object.__validate_company(company)
        object._salary = object.__validate_salary(salary)
        object._url = object.__validate_url(url)
        object._city = object.__validate_city(city)
        object._description = object.__validate_description(description)

    @property
    def id(object) -> str:
        return object._id

    @property
    def name(object) -> str:
        return object._name

    @property
    def company(object) -> str:
        return object._company

    @property
    def salary(object) -> float:
        return object._salary

    @property
    def url(object) -> str:
        return object._url

    @property
    def city(object) -> str:
        return object._city

    @property
    def description(object) -> str:
        return object._description

    def __validate_description(object, value: str) -> str:
        """Description validation"""
        if not isinstance(value, str) or not value:
            return "Description not set"
        return value

    def __validate_city(object, value: str) -> str:
        """City validation"""
        if not isinstance(value, str) or not value:
            return "City name not set"
        return value

    def __validate_name(object, name: str) -> str:
        """Name validation"""
        if not isinstance(name, str) or not name:
            return "Vacancy name not set"
        return name

    def __validate_company(object, company: str) -> str:
        """Company validation"""
        if not isinstance(company, str) or not company:
            return "Company name not set"
        return company

    def __validate_salary(object, salary: int) -> int:
        """Salary validation"""
        if not isinstance(salary, int) or salary < 0:
            return 0
        return salary

    def __validate_url(object, url: str) -> str:
        """URL validation"""
        if not isinstance(url, str) or not url.startswith("http"):
            return "Wrong URL"
        return url

    def __lt__(object, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return object.salary < other.salary

    def __le__(object, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return object.salary <= other.salary

    def __eq__(object, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return object.salary == other.salary

    def __ne__(object, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return object.salary != other.salary

    def __gt__(object, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return object.salary > other.salary

    def __ge__(object, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Wrong type comparison")
        return object.salary >= other.salary

    def __str__(object) -> str:
        return f"""ID: {object.id}
        Name: {object.name}
        City: {object.city}
        Description: {object.description}
        Company: {object.company}
        Salary: {object.salary}
        Link: {object.url}"""

    def to_dict(object) -> dict:
        return {
            "id": object.id,
            "name": object.name,
            "company": object.company,
            "salary": object.salary,
            "url": object.url,
            "city": object.city,
            "description": object.description,
        }
