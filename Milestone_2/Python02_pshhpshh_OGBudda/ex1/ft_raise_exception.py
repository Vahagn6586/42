def input_temperature(temp_str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp} is too hot for plants (max 40C)")
    elif temp < 0:
        raise ValueError(f"{temp} is too cold for plants (min 0C)")
    return (temp)


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        print("Temperature is now", input_temperature("25"))
    except ValueError as e:
        print("Caught input_temperature error: ", e)

    try:
        print("Input data is 'abc'")
        print("Temperature is now", input_temperature("abc"))
    except ValueError as e:
        print("Caught input_temperature error:", e)

    try:
        print("Input data is '100'")
        print(input_temperature("100"))
    except ValueError as e:
        print("Caught input_temperature error:", e)

    try:
        print("Input data is '-50':")
        print(input_temperature("-50"))
    except ValueError as e:
        print("Caught input_temperature error:", e)


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("All tests completed - programm didnt crash!")


if __name__ == "__main__":
    main()
