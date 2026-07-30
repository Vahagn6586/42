import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item = parts[0]
        quantity_str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = quantity

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())

    print(
        f"Total quantity of the {len(inventory)} items: {total_quantity}"
    )

    for item in inventory:
        percentage = inventory[item] * 100 / total_quantity
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_item:  (str | None) = None
    least_item: (str | None) = None

    for item in inventory:
        if most_item is None:
            most_item = item
            least_item = item
            continue

        if inventory[item] > inventory[most_item]:
            most_item = item

        assert least_item is not None

        if inventory[item] < inventory[least_item]:
            least_item = item

    if most_item is not None and least_item is not None:
        print(
            f"Item most abundant: "
            f"{most_item} with quantity {inventory[most_item]}"
        )

        print(
            f"Item least abundant: "
            f"{least_item} with quantity {inventory[least_item]}"
        )

    inventory.update({"magic_item": 1})

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
