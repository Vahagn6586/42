import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(',')
        count = 0
        for i in parts:
            count += 1
        if count != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            return (x, y, z)
        except ValueError:
            count = 0
            for i in parts:
                count += 1
            j = 0
            while j < count:
                part = parts[j].strip()
                try:
                    float(part)
                except ValueError as e:
                    print(f"Error on parameter '{part}': {e}")
                    break
                j += 1
            continue


def distance_between_points(p1: tuple[float, float, float],
                            p2: tuple[float, float, float]) -> float:
    return math.sqrt((p2[0] - p1[0])**2 +
                     (p2[1] - p1[1])**2 +
                     (p2[2] - p1[2]) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    center = (0, 0, 0)
    dist_to_center = distance_between_points(center, pos1)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    dist_between = distance_between_points(pos1, pos2)
    print(f"Distance between the 2"
          f"sets of coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    main()
