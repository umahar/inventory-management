"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for i in items:
        inventory.update({i: items.count(i)})
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for i in items:
        if i in inventory.keys():
            inventory.update({i: (inventory.get(i)) + 1})
        else:
            inventory.update({i: 1})
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for i in items:
        if i in inventory.keys():
            if inventory.get(i) - 1 < 0:
                inventory.update({i: 0})
            else:
                inventory.update({i: (inventory.get(i)) - 1})
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inv = []
    for key, value in inventory.items():
        if value > 0:
            inv.append((key, value))
    return inv


# print(create_inventory(["wood", "iron", "coal", "wood"]))
# print(add_items({"coal": 1}, ["wood", "iron", "coal", "wood"]))
# print(
#     decrement_items(
#         {"coal": 3, "diamond": 1, "iron": 5},
#         ["diamond", "diamond", "coal", "iron", "iron"],
#     )
# )
# print(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coald"))
print(list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0}))
