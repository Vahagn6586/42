def calcculate(num: int):
    if num == 0:
        return
    elif num > 1:
        calcculate(num - 1)
    print(f"Day {num}")


def ft_count_harvest_recursive():
    harvest_days = int(input("Days until harvest: "))
    if harvest_days < 0:
        return
    calcculate(harvest_days)
    print("Harvest time!")
