""" 
Class Average
Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:

Average Score	Letter Grade
97-100	"A+"
93-96	"A"
90-92	"A−"
87-89	"B+"
83-86	"B"
80-82	"B-"
77-79	"C+"
73–76	"C"
70-72	"C-"
67-69	"D+"
63-66	"D"
60–62	"D-"
below 60	"F"
Calculate the average by adding all scores in the array and dividing by the total number of scores.


"""

import unittest

class ClassAverageTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_average_grade([92, 91, 90, 94, 89, 93]), "A-")

    def test2(self):
        self.assertEqual(get_average_grade([84, 89, 85, 100, 91, 88, 79]), "B+")

    def test3(self):
        self.assertEqual(get_average_grade([63, 69, 65, 66, 71, 64, 65]), "D")

    def test4(self):
        self.assertEqual(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]), "A+")

    def test5(self):
        self.assertEqual(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]), "C+")

    def test6(self):
        self.assertEqual(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]), "F")


def get_average_grade(scores):

    avg = sum(scores) / len(scores)

    if avg >= 97:
        return "A+"
    elif avg >= 93:
        return "A"
    elif avg >= 90:
        return "A-"
    elif avg >= 87:
        return "B+"
    elif avg >= 83:
        return "B"
    elif avg >= 80:
        return "B-"
    elif avg >= 77:
        return "C+"
    elif avg >= 73:
        return "C"
    elif avg >= 70:
        return "C-"
    elif avg >= 67:
        return "D+"
    elif avg >= 63:
        return "D"
    elif avg >= 60:
        return "D-"
    else:
        return "F"
    
"""  

We just need to add some safe guard for the empty input.And we can also the write the python code as follows.
"""


def get_average_grade(scores):

    if not scores:
        return None
    
    avg = sum(scores) / len(scores)
    avg = int(avg)

    if 97 <= avg <= 100:
        return "A+"
    elif 93 <= avg <= 96:
        return "A"
    elif 90 <= avg <= 92:
        return "A-"
    elif 87 <= avg <= 89:
        return "B+"
    elif 83 <= avg <= 86:
        return "B"
    elif 80 <= avg <= 82:
        return "B-"
    elif 77 <= avg <= 79:
        return "C+"
    elif 73 <= avg <= 76:
        return "C"
    elif 70 <= avg <= 72:
        return "C-"
    elif 67 <= avg <= 69:
        return "D+"
    elif 63 <= avg <= 66:
        return "D"
    elif 60 <= avg <= 62:
        return "D-"
    else:
        return "F"
    
def get_average_grade_lookup_apporach(scores):

    if not scores:
        return None
    
    avg = round(sum(scores) / len(scores))

    """ 
    converting to integer truncates the decimal part (floor toward zero).
    so 66.9433434 becomes like 66
    it works for few test cases or some failing cases, but it can misclassify averages near the upper boundary of a grade.

    Better apporach is to use the round()

    1. Round instead of truncate

        avg = round(sum(scores) / len(scores))

        66.943.. -> 67 -> "D+" (arguably more accurate).
        92.9 -> 93 -> "A".
        This avoids the bias of always flooring.

    2. We can also keep the float, and adjsut the ranges like

        -> for that we need to define the ranges with decimals in mind:
            elif 63 <= avg < 67:     # D
            elif 67 <= avg < 70:    # D+
            
            => This way, 66.97 fails into "D" naturally without castling.

    
    3. Explicit floor/cell if desired
        -> If your grading policy is "always round down", then int() is valid
        -> But you must accept that it will systematically bias toward the lower grade.


    FINALLY
        -> If you want realistic grading, use round() so averages are classified faily.
        -> If you want strict floor behaviour, keep int(), but be aware it can under-grade students near cutoofs.
        -> If you want precise float handling, adjust your conditions to use < and <= properly.

        Using int() is valid if you want floor behaviour, but it's not ideal because it can misclassify averages near the upper boundary. Using round() or adjusting your ranges is more accurate and less error- prone.


    """
    # avg = int(avg)
    grade_table = [
        (97, 100, "A+"),
        (93, 96, "A"),
        (90, 92, "A-"),
        (87, 89, "B+"),
        (83, 86, "B-"),
        (80, 82, "B-"),
        (77, 79, "C+"),
        (73, 76, "C"),
        (70, 72, "C-"),
        (67, 69, "D+"),
        (63, 66, "D"),
        (60, 62, "D-"),
        (0, 59, "F")
    ]

    for low, high, grade in grade_table:
        if low <= avg <= high:
            return grade
        
"""

This apporach is maintainable : => Adding or changing ranges is easy - just need to edit the table.

This is more readable than the previous elif long chains.

Flexibility: This can be reused for other grading logic (e.g., numeric ranges -> GPA).
"""
    
def get_average_grade_dict_apporach(scores):

    if not scores:
        return None
    
    avg = round(sum(scores) / len(scores))

    grade_cutoffs = {
        97: "A+",
        93: "A",
        90: "A-",
        87: "B+",
        83: "B",
        80: "B-",
        77: "C+",
        73: "C",
        70: "C-",
        67: "D+",
        63: "D",
        60: "D-",
        0: "F",
    }


    for cutoff in sorted(grade_cutoffs.keys(), reverse=True):
        if avg >= cutoff:
            return grade_cutoffs[cutoff]
        
        


if __name__ == "__main__":
    unittest.main()
    # print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]))
    print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))