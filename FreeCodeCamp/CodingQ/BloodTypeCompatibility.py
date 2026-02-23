"""  

Blood Type Compatibility
Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

Each blood type consists of:

A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
"""

import unittest

class BloodTypeCompatibilityTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(can_donate("B+", "B+"), True)

      def test2(self):
          self.assertEqual(can_donate("O-", "AB-"), True)

      def test3(self):
          self.assertEqual(can_donate("O+", "A-"), False)

      def test4(self):
          self.assertEqual(can_donate("A+", "AB+"), True)

      def test5(self):
          self.assertEqual(can_donate("A-", "B-"), False)

      def test6(self):
          self.assertEqual(can_donate("B-", "AB+"), True)

      def test7(self):
          self.assertEqual(can_donate("B-", "A+"), False)

      def test8(self):
          self.assertEqual(can_donate("O-", "O+"), True)

      def test9(self):
          self.assertEqual(can_donate("O+", "O-"), False)

      def test10(self):
          self.assertEqual(can_donate("AB+", "AB-"), False)  





def can_donate(donor, recipient):

    blood_groups = {
        "O+": ("A+","B+", "AB+","O+"),
        "O-":("A+","B+", "AB+","O+","A-","B-","AB-","O-"),
        "A+": ("A+","AB+"),
        "A-":("A-","AB-","A+","AB+"),
        "B+":("B+","AB+"),
        "B-":("B+","AB+","B-","AB-"),
        "AB+":("AB+"),
        "AB-":("AB+","AB-")
    }

    if blood_groups[donor]:
        if recipient in blood_groups[donor]:
            return True
        else:
            return False
        
    return False


"""

The main issue in the above problem is that for "AB+": ("AB+") is not a tuple, it's just a string.
That means when you check memebership, python will iterate over the characters "A", B","+" instead of treating "AB+" as a single valid recipient.

Also, there is not need of if blood_groups[donor]: check - that will always be truth if the donor exits in the dictionary. 
The below is the simplified logic
"""
def can_donate(donor, recipient):

    blood_groups = {
        "O+": ("A+","B+", "AB+","O+"),
        "O-":("A+","B+", "AB+","O+","A-","B-","AB-","O-"),
        "A+": ("A+","AB+"),
        "A-":("A-","AB-","A+","AB+"),
        "B+":("B+","AB+"),
        "B-":("B+","AB+","B-","AB-"),
        "AB+":("AB+"),
        "AB-":("AB+","AB-")
    }

    return recipient in blood_groups.get(donor, ())


def can_donate(donor, recipient):
    donor_letter, donor_rh = donor[:-1], donor[-1]
    recipient_letter, recipient_rh = recipient[:-1], recipient[-1]


    letter_rules = {
        "O": {"A","B","AB","O"},
        "A": {"A","AB"},
        "B":{"B","AB"},
        "AB":{"AB"}
    }

    def rh_compatible(d_rh, r_rh):
        if d_rh == "-":
            return True     # "-" can donate to both "-" and "+"
        return r_rh == "+" # "+" can donate only to "+"
    
    if recipient_letter in letter_rules[donor_letter] and rh_compatible(donor_rh,recipient_rh):
        return True
    return False



if __name__ == "__main__":
    unittest.main()
