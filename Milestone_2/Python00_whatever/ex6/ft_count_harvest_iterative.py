def ft_count_harvest_iterative():
    harvest_days = int(input("Days until harvest: "))
    if harvest_days < 0:
        return
    for i in range(1, harvest_days + 1):
        print(f"Day {i}")
    print("Harvest time!")
