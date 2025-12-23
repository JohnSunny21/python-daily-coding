"""  
Re: Fwd: Fw: Count
Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

"fw:"
"fwd:"
"re:"
Return the total number of occurrences of these markers.


"""
import unittest

class ReFwdFwCountTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(email_chain_count("Re: Meeting Notes"), 1)

    def test2(self):
        self.assertEqual(email_chain_count("Meeting Notes"), 0)
    
    def test3(self):
        self.assertEqual(email_chain_count("Re: re: RE: rE: Meeting Notes"), 4)

    def test4(self):
        self.assertEqual(email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes"), 5)

    def test5(self):
        self.assertEqual(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"), 23)



def email_chain_count(subject):
    subject = subject.lower()
    checkers = ["fw:","fwd:","re:"]
    count = 0
    for check in checkers:
        count += subject.count(check)
    
    return count

"""  
The above solution works fine for some cases but there are issues with this code

1. Overlapping markers
    -> "fwd:" contains "fw:"
    -> if the subject has "fwd:", the above code will count both "fw:" and "fwd:"
    Example:
        print(email_chain_count("Fwd: Meetig"))
        # Output: 2 (counts "fw:" and "fwd:")

        # Expected: 1

2. Exact matching:
    -> if you want to avoid double-counting, you need to ensure "fw:" and "fwd:" are treated as distinct
        tokens, not substrings.

=> This solution works fine unless "fwd:" appears, where it double-count because "fw:" is a substring of "fwd:".
=> Regex avoids this overlap by treating each marker as a distinct option.
=> if the requirement is okay with the slight overcount, this version is perfectly serviceable. If you want exact correctness,
regext is the safer choice.

"""

import re
# Corrected Version
def email_chain_count(subject):

    markers = ["fw:","fwd:","re:"]

    pattern = re.compile(r"(fw:|fwd:|re:)",re.IGNORECASE)

    matches = pattern.findall(subject)

    return len(matches)

"""  
This solution

=> Use case-insensitive matching re.IGNORECASE in (python, /gi i JS).
=> Regex is the cleanest way since it handles overlapping and mixed cases.
=> The result is simply the length of all matches.

"""



if __name__ == "__main__":
    
    unittest.main()