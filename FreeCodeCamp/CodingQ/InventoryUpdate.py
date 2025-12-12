"""
Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].

"""

import unittest

class InventoryUpdateTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]), [[3, "apples"], [8, "bananas"]])

    def test2(self):
        self.assertEqual(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]),[[3, "apples"], [8, "bananas"], [4, "oranges"]])

    def test3(self):
        self.assertEqual(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]),[[10, "apples"], [30, "bananas"], [20, "oranges"]])

    def test4(self):
        self.assertEqual(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]),[[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]])



def update_inventory(inventory, shipment):

    inventory_dict = {item: qty for qty, item in inventory}

    for qty, item in shipment:
        if item in inventory_dict:
            inventory_dict[item] += qty
        else:
            inventory_dict[item] = qty

    
    updated = []
    existing_items = set()
    for qty, item in inventory:
        updated.append([inventory_dict[item], item])
        existing_items.add(item)

    for qty, item in shipment:
        if item not in existing_items:
            updated.append([inventory_dict[item], item])

    return updated


if __name__ == "__main__":
    print(update_inventory([[2, "apples"], [5, "bananas"]],
                       [[1, "apples"], [3, "bananas"]]))
    
    unittest.main()

