""" 

Allergen Friendly Meals
Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.

Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
Allergens to avoid will be an array of strings.
Return safe meal names in the same order given. If no meal is safe, return an empty array.
"""


import unittest

class AllergenFriendlyMealsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]), ["salad"])

    def test2(self):
        self.assertEqual(get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]), ["fried rice", "chicken parmesan"])

    def test3(self):
        self.assertEqual(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"]), ["oatmeal", "granola", "toast"])

    def test4(self):
        self.assertEqual(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"]), ["granola", "yogurt", "eggs"])


TESTCASES = [
    (([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"],), ["salad"]),
    (([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"],), ["fried rice", "chicken parmesan"]),
    (([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"],), ["oatmeal", "granola", "toast"]),
    (([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"],), ["granola", "yogurt", "eggs"])
]




def get_allergen_friendly_meals_continue(meals, allergens):

    result = []

    for meal, allergies in meals:

        flag = False
        for allergy in allergies:
            if allergy in allergens:
                flag = True
                continue
        if flag:
            continue

        result.append(meal)

    return result

""" 

But there is a subtle issue in the above solution

-> You loop through each meal's allergens.
-> If you find one that matches the avoid list, you set flat = True.
-> Then continue inside the inner loop, but that just skips to the next allergen - it doesn't break out of the loop
-> After finishing the inner loop, you check if flag: continue to skip adding the meal.
-> The inner continue is unnecessary.

The above solution works but a bit roundabout. You don't actually need the inner continue - once you've market flag=True , you can break out of the loop immdiately.

"""

def get_allergen_friendly_meals_break(meals, allergens):

    result = []

    for meal, allergies in meals:
        flag = False

        for allergy in allergies:
            if allergy in allergens:
                flag = True
                break
        
        if not flag:
            result.append(meal)



def get_allergen_friendly_meals(meals, avoid):
    safe = []
    avoid_set = set(avoid)

    for meal, allergens in meals:
        if not any(a in avoid_set for a in allergens):
            safe.append(meal)

    return safe



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": get_allergen_friendly_meals_continue,
         "second": get_allergen_friendly_meals_continue,
         "third": get_allergen_friendly_meals},
        TESTCASES,
        10000
    )

    unittest.main()