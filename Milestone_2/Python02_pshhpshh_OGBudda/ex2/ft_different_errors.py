def input_temperature(temp_str) -> int:
    return (int(temp_str))


def garden_operations(operation_number) -> None:
    match operation_number:
        case 0:
            print(input_temperature("abc"))
        case 1:
            print(operation_number / 0)
        case 2:
            open("smth.smth")
        case 3:
            print("abc" + 67)


def test_error_types() -> None:
    for i in range(4):
        print("Testing operation", i)
        try:
            garden_operations(i)
        except ValueError as e:
            print("Caught ValueError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except TypeError as e:
            print("Caught TypeError:", e)


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All tests completed - programm didnt crash!")


if __name__ == "__main__":
    main()
