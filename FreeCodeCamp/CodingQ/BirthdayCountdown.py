""" 



Birthday Countdown
Given today's date and a birthday, return the number of days until the person's next birthday.

Today's date is given as a string in "YYYY-MM-DD" format, with leading zeros, for example: "2026-07-16".
The birthday is given as a string in "M/D" format, without leading zeros, for example: "9/7".
If today is their birthday, return the number of days until their next birthday (not 0).
Leap years should be accounted for.
"""


import unittest


class BirthdayCountdownTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(days_until_birthday("2026-07-16", "9/7"), 53)

    def test2(self):
        self.assertEqual(days_until_birthday("2026-07-16", "3/22"), 249)

    def test3(self):
        self.assertEqual(days_until_birthday("2026-07-16", "7/16"), 365)

    def test4(self):
        self.assertEqual(days_until_birthday("2024-02-28", "3/1"), 2)

    def test5(self):
        self.assertEqual(days_until_birthday("2023-04-24", "12/30"), 250)

    def test6(self):
        self.assertEqual(days_until_birthday("2024-03-01", "2/29"), 1460)

    def test7(self):
        self.assertEqual(days_until_birthday("2096-03-01", "2/29"), 2920)


TESTCASES = [
    (("2026-07-16", "9/7",), 53),
    (("2026-07-16", "3/22",), 249),
    (("2026-07-16", "7/16",), 365),
    (("2024-02-28", "3/1",), 2),
    (("2023-04-24", "12/30",), 250),
    (("2024-03-01", "2/29",), 1460),
    (("2096-03-01", "2/29",), 2920)
]



from datetime import datetime, date, timedelta

def days_until_birthday(today, birthday):

    # Parsing today's date
    today = datetime.strptime(today, "%Y-%m-%d").date()
    year = today.year


    # Parsing the birthday Month / day
    month, day = map(int, birthday.split("/"))

    # Handle leap year birthdays (feb 29)
    try:
        birthday_this_year = date(year, month, day)
    except ValueError:
        # If Feb 29 and not a leap year, use Fed 28
        birthday_this_year = date(year, 2, 28)

    # If birthday has already passed or is today, go to next year
    if birthday_this_year <= today:
        year += 1
        try:
            birthday_next = date(year, month, day)
        except ValueError:
            birthday_next = date(year, 2, 28)
    else:
        birthday_next = birthday_this_year
    
    return (birthday_next - today).days


""" The above solution works but only two test cases fails cause of a special condition where the 29 feb as birthday
    he needs to wait for he another leap year and count up to the days until his birthday
"""


def days_until_birthday(today_str, birthday_str):

    today = datetime.strptime(today_str, "%Y-%m-%d").date()
    year = today.year
    month, day = map(int, birthday_str.split("/"))

    # Special case: Feb 29
    if month == 2 and day == 29:
        # If today is before Feb 29 in a leap year
        if(year % 4 ==0  and (year % 100 != 0 or year % 400 == 0)) and today < date(year, 2, 29):
            next_birthday = date(year, 2, 29)
        else:
            # Find the next leap year
            while True:
                year += 1
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    next_birthday = date(year, 2, 29)
                    break
    
    else:
        # Normal birthdays
        try:
            birthday_this_year = date(year, month, day)
        except ValueError:
            raise ValueError("Invalid birthday date")
        
        if birthday_this_year <= today:
            year += 1
            birthday_this_year = date(year, month, day)
        
        next_birthday = birthday_this_year

    return (next_birthday - today).days








from utils.benchmark import benchmark

if __name__ == "__main__":


    print(days_until_birthday("2024-03-01", "2/29"))
    # scores = benchmark({"first": days_until_birthday}, TESTCASES, 10000)

    # unittest.main()




