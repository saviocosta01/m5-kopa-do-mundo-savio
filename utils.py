from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(info):
    date_string = info["first_cup"]
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    year = date_object.year
    find_year = []
    amounts_of_hearts = 0

    if info["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    for i in range(1930, 2023, 4):
        if year == i:
            find_year.append(i)

        if i >= year:
            amounts_of_hearts += 1

    if len(find_year) == 0:
        raise InvalidYearCupError("there was no world cup this year")

    if info["titles"] > amounts_of_hearts:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
