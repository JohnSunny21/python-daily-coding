""" 

Food Chain
Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.

The apex predator is the animal that is never prey to another animal.
Return the chain as an array of strings.
"""


import unittest


class FoodChainTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_food_chain([["cat", "mouse"]]), ["cat", "mouse"])

    def test2(self):
        self.assertEqual(get_food_chain([["wolf", "deer"], ["deer", "grass"]]), ["wolf", "deer", "grass"])

    def test3(self):
        self.assertEqual(get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]), ["hawk", "snake", "frog", "fly"])

    def test4(self):
        self.assertEqual(get_food_chain([["rabbit","grass"], ["fox", "rabbit"], ["eagle", "fox"]]), ["eagle", "fox", "rabbit", "grass"])

    def test5(self):
        self.assertEqual(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]), ["orca", "seal", "salmon", "herring", "shrimp", "plankton"])


TESTCASES = [
    (([["cat", "mouse"]],), ["cat", "mouse"]),
    (([["wolf", "deer"], ["deer", "grass"]],), ["wolf", "deer", "grass"]),
    (([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]],), ["hawk", "snake", "frog", "fly"]),
    (([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]],), ["eagle", "fox", "rabbit", "grass"]),
    (([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]],), ["orca", "seal", "salmon", "herring","shrimp", "plankton"])
]



def get_food_chain(pairs):

    # Build maps
    predator_to_prey = {}
    prey_set = set()

    for predator, prey in pairs:
        predator_to_prey[predator] = prey
        prey_set.add(prey)

    # Apex predator = one that is never the prey
    apex = None
    for predator in predator_to_prey:
        if predator not in prey_set:
            apex = predator
            break

    # Build chain 
    chain = [apex]
    while apex in predator_to_prey:
        apex = predator_to_prey[apex]
        chain.append(apex)

    return chain


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": get_food_chain}, TESTCASES, 10000)
    unittest.main()
