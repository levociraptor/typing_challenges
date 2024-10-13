from typing import TypeAlias

User: TypeAlias = tuple[str, int, str]


def get_current_user() -> User:
    pass


if __name__ == "__main__":
    assert get_current_user() == ("Ilya Lebedev", 33, "melevir@gmail.com")
