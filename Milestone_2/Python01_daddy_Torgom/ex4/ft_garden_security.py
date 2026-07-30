class Plant:
    _grow_rate = 0.8
    _age_rate = 1

    def __init__(self, name: str, height: float, age: int) -> None:
        if height < 0:
            print("Height cannot be negative")
            height = 0.0
        if age < 0:
            print("Age cannot be negative")
            age = 0

        self._name = name
        self._height = height
        self._age = age

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: ", end="")
        print(f"{self._height}cm, ", end="")
        print(f"{self._age} days old")

    def grow_plant(self) -> None:
        self._height += self._grow_rate
        self._height = round(self._height, 1)

    def age_plant(self) -> None:
        self._age += self._age_rate


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)

    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-42)
    rose.set_age(-67)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
