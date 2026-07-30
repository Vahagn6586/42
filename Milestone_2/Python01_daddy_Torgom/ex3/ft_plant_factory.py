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


def main():
    print("=== Garden Plant Growth ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
