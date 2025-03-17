# from typing import List, Dict, Any
# from typing import List [Dict[str, Any]]


def filter_by_state(list_of_dictionaries: list, state: str) -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ state"""
    total_of_dictionary = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == state:
            total_of_dictionary.append(dictionary)
    return total_of_dictionary


def sort_by_date(list_of_dates: list) -> list:
    """Функция возвращает список словарей, отсортированный по дате"""


if __name__ == "__main__":
    total_of_dictionary = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "CANCELED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
        ],
        "EXECUTED",
    )
    print(total_of_dictionary)
