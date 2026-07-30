def ft_water_reminder():
    days_wout_water = int(input("Days since last watering: "))
    if days_wout_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
