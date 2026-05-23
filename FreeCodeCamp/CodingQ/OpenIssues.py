""" 


Open Issues
Given an array of issue numbers and another array of pull request (PR) numbers, return an array of issues that remain open after all PRs have been merged.

A PR closes an issue if their digits are a rotation of each other. For example, issue 123 would be closed by PR 231 or 312.
A PR does not close an issue with the exact same number. For example, PR 123 does not close issue 123. So an issue with all the same number can't get closed.
Either number may have leading zeros stripped. For example, PR 201 would close issue 12 (012, a rotation of 201). Similarily, issue 201 would be closed by PR 12.
Return the remaining open issues in the order they were given.
"""




import unittest



class OpenIssuesTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_open_issues([123, 234], [231]), [234])

    def test2(self):
        self.assertEqual(get_open_issues([123, 345, 16], [345, 231]), [345, 16])

    def test3(self):
        self.assertEqual(get_open_issues([456, 332, 12, 15], [201, 945, 180]), [456, 332, 15])

    def test4(self):
        self.assertEqual(get_open_issues([12, 115, 296, 170, 24], [17, 18, 19, 20, 21]), [115, 296, 24])

    def test5(self):
        self.assertEqual(get_open_issues([19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802], [395, 440, 9001, 95, 242, 21, 287, 169, 14]), [95, 395, 754, 296, 709, 237, 1802])


TESTCASES = [
    (([123, 234], [231],), [234]),
    (([123, 345, 16], [345, 231],), [345, 16]),
    (([456, 332, 12, 15], [201, 945, 180],), [456, 332, 15]),
    (([12, 115, 296, 170, 24], [17, 18, 19, 20, 21],), [115, 296, 24]),
    (([19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802], [395, 440, 9001, 95, 242, 21, 287, 169, 14],), [95, 395, 754, 296, 709, 237, 1802])
]





def get_open_issues_1(issues, prs):

    for issue_num in issues:
        rotations = []
        issue_str = str(issue_num)
        
        issue_len = len(issue_str)

        if issue_len <= 2:
            rotations.append(int(issue_str[::-1]))
            # rotations.append(int(issue_str))


        issue_str = issue_str.zfill(3)
        issue_len = len(issue_str)

        for i in range(issue_len):
            rotation_str = issue_str[i:] + issue_str[:i]
            rotations.append(int(rotation_str))

        

        for rotation in rotations:
            if rotation in prs and rotation not in issues:
                issues.remove(issue_num)
                break

        rotations.clear()


    return issues


""" 
The above solution has some issues with the code.


=> Mutating the issues list while iterating
    -> You're doing issues.remove(issue_num) inside the loop.
    -> Modifying a list while iterating over it can cause skipped elements or unexpected behaviour.
    -> Safer approach: build a new list of open issues instead of removing in place.

=> Rotation logic for short numbers
    -> You special-case issue_Len <= 2 by reversing the string.
    -> But rotations should be consistent for all lengths. For example, "12" shoudl generate "12" and "21".
    -> Your reverse logic works for 2 digits, but it doesn't handle leading zeros consistently (e.g,, "12" vs "012")


=> Condition rotation not in issues
    -> You're checking if rotation in prs and rotation not in issues.
    -> The spec says: A PR does not close an issue with the exact same number".
    -> That means you should compare rotation != issue_num, not whether the rotataion exists in the issues list.
    -> Otherwise, you might incorrectly skip valid closures.

=> Clearing rotations
    -> You call rotations.clear() at the end of each loop. That's fine, but unnecessary since you reassign rotations = [] at the start of each iteration anyway.

"""


def rotations(num_str):

    """ Generate all rotations of a number string, stripping leading zeros."""
    n = len(num_str)
    rots = []

    for i in range(n):

        rot = num_str[i:] + num_str[:i]
        rots.append(str(int(rot)))
        # if a rotation becomes all zeros, the above line is fine
        # int("000") -> 0 but using int() 
        # solely to strip leading zeros is a bit risky and unnecessary.
        # A safer version is rots.append(rot.lstrip("0") or "0")
    return rots



def get_open_issues_partial(issues, prs):

    prs = set(str(p) for p in prs)
    result = []

    for issue in issues:
        issue_str = str(issue).zfill(3)
        closed = False
        for rot in rotations(issue_str):
            if rot in prs and rot != issue_str:
                closed = True
                break
        if not closed:
            result.append(issue)

    return result

def get_open_issues_full(issues, prs):

    result = []

    for issue in issues:
        closed = False

        for pr in prs:

            # CHANGED:  
            # Use the maximum length of the issue and PR,
            # because either side may have stripped leading zeros.
            length = max(len(str(issue)), len(str(pr)))


            issue_str = str(issue).zfill(length)

            # CHANGED:
            # Same numeric value never closes the issue.
            if issue == pr:
                continue

            for rot in rotations(issue_str):

                # CHANGED:
                # Compare against the actual PR value.

                if rot == str(pr):
                    closed = True
                    break
            
            if closed:
                break

        if not closed:
            result.append(issue)


    return result


""" 
we don't actually need to generate all rotations.

A common trick i:

     a = str(issue).zfill(length)
     b = str(issue).zfill(length)

     b in (a + a)

     because every rotation of a appears inside a + a.

     That reduces both code size and complexity.
"""




def is_closed(issue, pr):
    # same number never closes the issue

    if issue == pr:
        return False
    
    a = str(issue)
    b = str(pr)

    n = max(len(a), len(b))

    a = a.zfill(n)
    b = b.zfill(n)

    return b in (a + a)


def get_open_issues(issues, prs):

    result = []

    for issue in issues:
        closed = False

        for pr in prs:
            if is_closed(issue, pr):
                closed = True
                break
        if not closed:
            result.append(issue)


    return result
        






from utils.benchmark import benchmark


if __name__ == "__main__":


    print(get_open_issues([456, 332, 12, 15], [201, 945, 180]))


    print(get_open_issues([456, 332, 12, 15], [201, 945, 180]))


    print(get_open_issues([12, 115, 296, 170, 24], [17, 18, 19, 20, 21]))

    print(get_open_issues([19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802], [395, 440, 9001, 95, 242, 21, 287, 169, 14]))
    scores = benchmark({
        "first": get_open_issues,
        "second": get_open_issues_full
    },
    TESTCASES,
    10000)

    unittest.main()



            

                