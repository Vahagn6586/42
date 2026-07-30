class Plant:
    grow_rate = 0.8
    age_rate = 1

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{self.height}cm, ", end="")
        print(f"{self.age} days old")

    def grow_plant(self) -> None:
        self.height += self.grow_rate
        self.height = round(self.height, 1)

    def age_plant(self) -> None:
        self.age += self.age_rate


def main() -> None:
    rose = Plant("Rose", 25, 30)
    total_growth = 0.0

    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age_plant()
        rose.grow_plant()
        rose.show()
        total_growth += float(rose.grow_rate)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
