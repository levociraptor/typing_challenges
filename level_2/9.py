from typing import TypeAlias
import datetime

ShoppingList: TypeAlias = list[tuple[str, int, float]]
CashReceipt: TypeAlias = tuple[int, datetime.date, ShoppingList]


def parse_receipt(raw_receipt: str) -> CashReceipt:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
