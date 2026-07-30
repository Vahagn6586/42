class Plant:
    _grow_rate: float = 0.8
    _age_rate: int = 1

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


class Flower(Plant):
    _color: str
    _bloom_ident: int = 0

    def __init__(self, name: str, color: str,
                 height: float, age: int) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        if not self._bloom_ident:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._bloom_ident = 1


class Tree(Plant):

    _trunk_diameter: float = 0

    def __init__(self, name: str, trunk_diameter: float, height: float,
                 current_age: int) -> None:
        super().__init__(name, height, current_age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"The {self._name} produces", end=" ")
        print(f"a shade of {self._height}cm long and",
              f"{self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(self, name: str, color: str,  height: float, current_age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, current_age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        self._height += self._grow_rate
        self._height = round(self._height, 1)
        self._nutritional_value = self._nutritional_value + 1

    def age(self) -> None:
        self._age += 1
        self._nutritional_value = self._nutritional_value + 1


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", "red", 15.0, 10)

    print("=== Flower")

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
