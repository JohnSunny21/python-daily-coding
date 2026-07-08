""" 
Issue Triage
Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:

If the last message is less than 7 days ago, return "leave it"
If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
Otherwise, return "bump it"
"""


import unittest


class IssueTriageTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(triage_issue(86400000, "Lets fix it"), "leave it")

    def test2(self):
        self.assertEqual(triage_issue(1209600000, "still waiting"), "bump it")

    def test3(self):
        self.assertEqual(triage_issue(864000000, "bump"), "close it")

    def test4(self):
        self.assertEqual(triage_issue(604800000, "Do we still want this?"), "bump it")

    def test5(self):
        self.assertEqual(triage_issue(604800000, "Bumping this"), "close it")

    def test6(self):
        self.assertEqual(triage_issue(345600000, "I'll make a PR"), "leave it")


TESTCASES = [
    ((86400000, "Lets fix it",), "leave it"),
    ((1209600000, "still waiting",), "bump it"),
    ((864000000, "bump",), "close it"),
    ((604800000, "Do we still want this?",), "bump it"),
    ((604800000, "Bumping this",), "close it"),
    ((345600000, "I'll make a PR",), "leave it")
]



def triage_issue(ms, message):

    no_of_days = ms / 86400000

    message = message.lower()

    if no_of_days < 7:
        return "leave it"
    elif "bump" in message:
        return "close it"
    else:
        return "bump it"


def issue_triage(ms_since_last, last_message):

    days = ms_since_last / (1000 * 60 * 60 * 24)
    msg_lower = last_message.lower()

    if days < 7:
        return "leave it"
    elif "bump" in msg_lower:
        return "close it"
    else:
        return "bump it"
    




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": triage_issue, "second": issue_triage}, TESTCASES, 10000)
    unittest.main()
