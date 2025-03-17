# from typing import List, Dict, Any
# from typing import List [Dict[str, Any]]


def sort_by_date(list_of_dictionaries: list) -> list:
    """Функция возвращает список словарей, отсортированный по дате"""
    for dictionary in list_of_dictionaries:
        total_of_dictionary = sorted(
            list_of_dictionaries, key=lambda x: x["date"], reverse=True
        )
    return total_of_dictionary


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
