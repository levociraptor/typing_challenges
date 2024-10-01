from typing import TypeAlias
import datetime

Shopping_list: TypeAlias = list[tuple[str, int, float]]
Cash_receipt = tuple[int, datetime.date, Shopping_list]


def parse_receipt(raw_receipt: str) -> Cash_receipt:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
