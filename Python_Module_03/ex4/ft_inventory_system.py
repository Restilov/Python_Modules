import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty_str = parts[0], parts[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item, qty in inventory.items():
        pct = round((qty / total) * 100, 1)
        print(f"Item {item} represents {pct}%")

    def get_value(k):
        return inventory[k]

    most = max(inventory, key=get_value)
    least = min(inventory, key=get_value)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


main()
