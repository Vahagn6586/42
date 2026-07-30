class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float = 0.8, age_rate: int = 1) -> None:
        if height < 0:
            print("Height cannot be negative")
            height = 0.0
        if age < 0:
            print("Age cannot be negative")
            age = 0

        self._name = name
        self._height = height
        self._age = age
        self._grow_rate = grow_rate
        self._age_rate = age_rate
        self._stats = Plant.Stats()

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
        self._stats._show_count += 1

    def grow_plant(self) -> None:
        self._height += self._grow_rate
        self._height = round(self._height, 1)
        self._stats._grow_count += 1

    def age_plant(self) -> None:
        self._age += self._age_rate
        self._stats._age_count += 1

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    _color: str
    _bloom_ident: int = 0

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
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

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show, "
                  f"{self._shade_count} shade")

    def __init__(self, name: str, trunk_diameter: float, height: float,
                 current_age: int) -> None:
        super().__init__(name, height, current_age)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        print(f"The {self._name} produces", end=" ")
        print(f"a shade of {self._height}cm long and",
              f"{self._trunk_diameter}cm wide.")
        self._stats._shade_count += 1


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


class Seed(Flower):
    def __init__(self, name: str,
                 height: float, age: int, color: str, seeds: int = 0) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def grow(self) -> None:
        super().grow_plant()

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seeds = seeds


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print("Is 400 days more than a year? ->",
          f"{Plant.is_older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow_plant()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 5.0, 365)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.produce_shade()
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow_plant()
    sunflower.age_plant()
    sunflower.bloom(42)
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)


if __name__ == "__main__":
    main()
