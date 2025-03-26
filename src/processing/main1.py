from typing import List, Dict, Any
from typing import List [Dict[str, Any]]


def sort_by_date(list_of_dictionaries: list, reverse: bool = True) -> list:
    """Функция возвращает список словарей, отсортированный по дате"""
    for dictionary in list_of_dictionaries:
    #"""Для словаря в данном списке словарей"""
        total_of_dictionary = sorted(
    #"""Обозначение списка, который будет содержать отсортированные по дате словари, задаём команду sorted"""
            list_of_dictionaries, key=lambda x: x["date"], reverse=reverse
        )
    """Обозначаем в скобках из какого списка берём словари для сортировки, задаём функцию лямбда, выполняющую 
    одно действие (сбор дат из каждого словаря заданного списка), обозначаем реверс"""
    return total_of_dictionary
    #"""Функция возвращает список total... с отсортированными словарями"""


if __name__ == "__main__":
    total_of_dictionary = sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
    print(total_of_dictionary)
#"""В блоке if __name...задаём данные для сортировки"""