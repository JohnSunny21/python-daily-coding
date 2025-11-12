"""

Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
"""


import unittest

class EmailSignatureGeneratorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"), "--Quinn Waverly, Founder and CEO at TechCo")

    def test2(self):
        self.assertEqual(generate_signature("Alice Reed", "Engineer", "TechCo"),">>Alice Reed, Engineer at TechCo")
    
    def test3(self):
        self.assertEqual(generate_signature("Tina Vaughn", "Developer", "example.com"),"::Tina Vaughn, Developer at example.com")

    def test4(self):
        self.assertEqual(generate_signature("B. B.", "Product Tester", "AcmeCorp"),">>B. B., Product Tester at AcmeCorp")

    def test5(self):
        self.assertEqual(generate_signature("windstorm", "Cloud Architect", "Atmospheronics"),"::windstorm, Cloud Architect at Atmospheronics")
        

def generate_signature(name, title, company):
    first = name[0].upper()

    if 'A' <= first <= 'I':
        prefix = '>>'
    elif 'J' <= first <= 'R':
        prefix = '--'
    elif 'S' <= first <= 'Z':
        prefix = '::'

    email_signature = f"{prefix}{name}, {title} at {company}"

    return email_signature

if __name__ == "__main__":
    print(generate_signature("Tina Vaughn", "Developer", "example.com"))
    unittest.main()