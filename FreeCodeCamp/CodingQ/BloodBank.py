""" 
Blood Bank
Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's inventory, and Y is the total number of patients.

Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".

Compatibility rules:

"AB" can receive from any blood type.
"A" can receive from "A" and "O".
"B" can receive from "B" and "O".
"O" can only receive from "O".
Duplicate entries in the given arrays represent quantity.

"""


import unittest


class BloodBankTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]), "4 of 4 patients served")

    def test2(self):
        self.assertEqual(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]), "3 of 5 patients served")

    def test3(self):
        self.assertEqual(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]), "4 of 5 patients served")

    def test4(self):
        self.assertEqual(triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]), "4 of 4 patients served")

    def test5(self):
        self.assertEqual(triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]), "8 of 11 patients served")

    def test6(self):
        self.assertEqual(triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]), "13 of 14 patients served")


TESTCASES = [
    ((["O", "A", "B", "AB"], ["O", "A", "B", "AB"],), "4 of 4 patients served"),
    ((["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"],), "3 of 5 patients served"),
    ((["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"],), "4 of 5 patients served"),
    ((["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"],), "4 of 4 patients served"),
    ((["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B","A", "B"],), "8 of 11 patients served"),
    ((["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"],), "13 of 14 patients served")
]



def triage_blood(bank, patients):

    count = 0

    total_patients = len(patients)

    for bd_group in patients:
        if bd_group == "AB" and len(bank) > 0:
            count += 1
            bank.pop(0)

        elif bd_group == "A":
            if "A" in bank:
                count += 1
                bank.remove("A")
            elif "O" in bank:
                count += 1
                bank.remove("O")

        elif bd_group == "B":
            if "B" in bank:
                count += 1
                bank.remove("B")
            elif "O" in bank:
                count += 1
                bank.remove("O")

        elif bd_group == "O" and "O" in bank:
            count += 1
            bank.remove("O")


    return f"{count} of {total_patients} patients served"
""" 

=> The above logic is correct: You check compatibility and remove from inventory.
=> For "AB" patients, you always pop(0) - that removes he first unit in the bank, regardless of type. This could waste inventory
    if the first unit isn't the best match. A greedy strategy would try "AB" -> "AB" first, then "A", "B", "O".

=> Using list.remove() is fine, but it's O(n) each time. For large inventories, a Counter or dictionary of counts is faster.

The above soliion if fine for the small inputs and pass basic tests.

But to maximize patients served:

=> Handle "AB" patients last (since they can take anything).
=> Use counts per blood type instead of repeatedly searching / removing from arrays.
"""

def blood_bank(inventory, patients):

    # Count inventory
    inv = {t: inventory.count(t) for t in ["AB", "A", "B", "O"]}
    served = 0

    for p in patients:
        if p == "O":
            if inv["O"] > 0:
                inv["O"] -= 1
                served += 1
        elif p == "A":
            if inv["A"] > 0:
                inv["A"] -= 1
                served += 1
            elif inv["O"] > 0:
                inv["O"] -= 1
                served += 1
        elif p == "B":
            if inv["B"] > 0:
                
                inv["B"] -= 1
                served += 1
            elif inv["O"] > 0:
                inv["O"] -= 1
                served += 1
        elif p == "AB":
            # Try AB first, then A, then B, then O
            if inv["AB"] > 0:
                inv["AB"] -= 1
                served += 1
            elif inv["A"] > 0:
                inv["A"] -= 1
                served += 1
            elif inv["B"] > 0:
                inv["B"] -= 1
                served += 1
            elif inv["O"] > 0:
                inv["O"] -= 1
                served += 1

    return f"{served} of {len(patients)} patients served"




from utils.benchmark import benchmark

if __name__ == "__main__":


    scores = benchmark({
        "first": triage_blood,
        # "second": blood_bank
    }, TESTCASES, 10000)

    unittest.main()