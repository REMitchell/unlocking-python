class User:
    def __init__(self, name: str):
        self.name: str = name


def process_user(user: User):
    print(f"processing {user.name}")


alice = User("Alice")
process_user(alice)
process_user(1)


def remove_smaller(elements: list[str | list], size: int):
    return [e for e in elements if len(e) < size]


remove_smaller(["apple", "bearable", [1, 2, 3]], 5)


words_by_character: dict[str, list[str]] = {"a": ["ant", "apple", "and"]}
