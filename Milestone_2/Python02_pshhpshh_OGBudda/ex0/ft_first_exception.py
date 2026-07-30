def input_temperature(temp_str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        print("Temperature is now", input_temperature("25"))
    except ValueError as e:
        print("Caught input_temperature error: ", e)

    try:
        print("Input data is 'abc':", input_temperature("abc"))
    except ValueError as e:
        print("Caught input_temperature error:", e)


def main() -> None:
    print("=== Garden temperature ===")
    test_temperature()
    print("All tests completed - programm didnt crash!")


if __name__ == "__main__":
    main()
