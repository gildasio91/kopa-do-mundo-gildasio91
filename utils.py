from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError
from datetime import datetime


def data_processing(data: dict):
    if data["titles"] < 0:
        raise NegativeTitlesError()
    
    first_cup_date = datetime.strptime(data["first_cup"], "%Y-%m-%d")
    first_cup_date_year = first_cup_date.year
    
    if first_cup_date_year < 1930 or not (first_cup_date_year - 1930) % 4 == 0:
        raise InvalidYearCupError()
    
    current_year = datetime.now().year
    total_cups_disputed = (current_year - first_cup_date_year) // 4 + 1

    if total_cups_disputed < data["titles"]:
        raise ImpossibleTitlesError