"""

Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given
"""

import unittest

class RecipeScalerTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2),["4 C Flour", "3 T Sugar"])

    def test2(self):
        self.assertEqual(scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5),["6 T Flour", "1.5 C Milk", "3 T Oil"])

    def test3(self):
        self.assertEqual(scale_recipe(["3 C Milk", "2 C Oats"], 0.5),["1.5 C Milk", "1 C Oats"])

    def test4(self):
        self.assertEqual(scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5),["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter", "1.25 C Sugar", "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"])


def scale_recipe(ingredients, scale):

    result = []
    for item in ingredients:
        quantity, unit, ingredient = item.split(' ',2)
        quantity = float(quantity) * scale

        if quantity.is_integer():
            quantity = int(quantity)
        else:
            quantity = str(quantity).rstrip("0").rstrip('.')
        
        result.append(f"{quantity} {unit} {ingredient}")

    return result




def scale_recipe_optimized(ingredients, scale):

    scaled = []

    for item in ingredients:

        parts = item.split(' ', 2) # only split into 3 parts max

        quantity , unit, ingredient = parts[0], parts[1], parts[2]

        # Scale the quantity
        scaled_quantity = float(quantity) * scale

        # Remove trailing zeros (convert to int if whole number)
        # .is_integer() check ensures whole numbers are returned as integers (no trailing .0).
        if scaled_quantity.is_integer():
            scaled_quantity = int(scaled_quantity) # is_integer() returns True if 2.0 False if 2.1,2.2....2.9 etc..
        else: 
            # .rstrip("0").rstrip(".") trims unnecessasry trailing zeros for decimals.
            scaled_quantity = str(scaled_quantity).rstrip("0").rstrip(".")

        scaled.append(f"{scaled_quantity} {unit} {ingredient}")

    return scaled

if __name__ == "__main__":
    print(scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5))
    print(scale_recipe(["3 C Milk", "2 C Oats"], 0.5))
    unittest.main()
