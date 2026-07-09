""" 
Issue Triage 2
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

If the issue doesn't have any labels, add:

"bug" and "needs triage" if the title contains "error" or "bug"
"enhancement" and "discussing" if the title contains "feature" or "add"
Otherwise, if the given labels contain:

"needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
"discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
If the title contains:

"security", add a "critical" label
"""


import unittest


class IssueTriage2Test(unittest.TestCase):


    def test1(self):
        self.assertEqual(triage_issue("app crasheswith error", []), ["bug", "needs triage"])

    def test2(self):
        self.assertEqual(triage_issue("app crasheswith error", ["bug", "needs triage"]), ["bug", "help wanted"])

    def test3(self):
        self.assertEqual(triage_issue("add dark mode", []), ["enhancement", "discussing"])

    def test4(self):
        self.assertEqual(triage_issue("add dark mode", ["enhancement", "discussing"]), ["enhancement", "help wanted"])

    def test5(self):
        self.assertEqual(triage_issue("xss security bug", []), ["bug", "needs triage", "critical"])

    def test6(self):
        self.assertEqual(triage_issue("security vulnerability in auth", []), ["critical"])

    def test7(self):
        self.assertEqual(triage_issue("easy a11y fix", ["bug", "needs triage"]), ["bug", "good first issue"])

    def test8(self):
        self.assertEqual(triage_issue("planned apimigration", ["enhancement", "discussing"]), ["enhancement", "on the roadmap"])

    def test9(self):
        self.assertEqual(triage_issue("improve security", ["enhancement", "discussing"]), ["enhancement", "help wanted", "critical"])


TESTCASES = [
    (("app crashes with error", [],), ["bug", "needs triage"]),
    (("app crashes with error", ["bug", "needs triage"],), ["bug", "help wanted"]),
    (("add dark mode", [],), ["enhancement", "discussing"]),
    (("add dark mode", ["enhancement", "discussing"],), ["enhancement", "help wanted"]),
    (("xss security bug", [],), ["bug", "needs triage", "critical"]),
    (("security vulnerability in auth", [],), ["critical"]),
    (("easy a11y fix", ["bug", "needs triage"],), ["bug", "good first issue"]),
    (("planned api migration", ["enhancement", "discussing"],), ["enhancement", "on the roadmap"]),
    (("improve security", ["enhancement", "discussing"],), ["enhancement", "help wanted", "critical"])
]




def triage_issue(title, labels):

    if not labels:
        if "error" in title or "bug" in title:
            labels.append("bug")
            labels.append("needs triage")
        elif "feature" in title or "add" in title:
            labels.append("enhancement")
            labels.append("discussing")


    elif "needs triage" in labels and ("simple" in title or "easy" in title):
        labels.remove("needs triage")
        labels.append("good first issue")

    elif "discussing" in labels and ("planned" in title or "next" in title):
        labels.remove("discussing")
        labels.append("on the roadmap")
    
    else:
        if "needs triage" in labels:
            labels.remove("needs triage")
        elif "discussing" in labels:
            labels.remove("discussing")
        labels.append("help wanted")

    if "security" in title:
        labels.append("critical")

    return labels





from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": triage_issue}, TESTCASES, 10000)
    unittest.main()