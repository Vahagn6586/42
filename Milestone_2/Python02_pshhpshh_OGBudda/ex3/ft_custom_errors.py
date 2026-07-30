class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def WaterPlant(water_resources) -> None:
    if water_resources < 10:
        raise WaterError("Not enough water in the tank!")


def CheckPlant(age) -> None:
    if age > 60:
        raise PlantError("The plant is wilting!")


def TestCustomErrors() -> None:
    try:
        CheckPlant(67)
    except PlantError as e:
        print(e)

    try:
        WaterPlant(6)
    except WaterError as e:
        print(e)

    try:
        CheckPlant(80)
    except GardenError as e:
        print(e)

    try:
        WaterPlant(0)
    except GardenError as e:
        print(e)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    TestCustomErrors()
    print("All custom errors work correctly!")


if __name__ == "__main__":
    main()
