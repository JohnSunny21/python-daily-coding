""" 

Due Date
Given a date string, return the date 9 months in the future.

The given and return strings have the format "YYYY-MM-DD".
If the month nine months into the future doesn't contain the original day number, return the last day of that month.
"""


import unittest

class DueDateTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_due_date("2025-03-30"), "2025-12-30")

    def test2(self):
        self.assertEqual(get_due_date("2025-04-27"), "2026-01-27")

    def test3(self):
        self.assertEqual(get_due_date("2025-05-29"), "2026-02-28")

    def test4(self):
        self.assertEqual(get_due_date("2026-06-30"), "2027-03-30")

    def test5(self):
        self.assertEqual(get_due_date("2026-10-11"), "2027-07-11")




import calendar
def get_due_date(date_str):

    year, month , day   = map(int, date_str.split("-"))

    new_month = month  + 9

    """
    => You start with the original month (say March = 3).
    => Add 9 -> 12. That's December.
    => But if the sum goes beyond 12 (like May = 5 -> 14), you need to roll over into the next year.
    """
    new_year = year + (new_month - 1) // 12

    """
    => (new_month - 1) // 12 is integer division
    => It calculates how many full years you need to add when the month count exceeds 12.
        -> Example: May(5) + 9 = 14 -> (14 - 1) // 12 = 13 // 12 = 1. So add  1 year.
        -> If it's still <= 12 (new_month-1) // 12 = 0, so the year stays the same.
    """
    new_month = ((new_month - 1) % 12) + 1

    """
    Normalize the month
    => % 12 wraps the month back into the 1-12 range.
    => Example: 14 -> (14-1) % 12 + 1 = 13%12  + 1 = 1 + 1 = 2. That's February.
    => So May 2026 + 9 mmonths = February 2027.

    """

    last_day = calendar.monthrange(new_year, new_month)[1]


    """
    => calendar.monthrange(year, month) returns (weekday_of_first_day, number_of_days_in_month)
    => The [1] picks the number of days in that month.
    => Example: calendar.monthrange(2027, 2)[1] -> 28 (or 29 if leap year).
    """
    new_day = min(day, last_day)

    """
    => If the original day exists in the new month, keep it.
    => If not, clamp to the last valid day.
    => Example: Original date= May 31. Add 9 months -> February 2027. February has only 28 days, so min(31, 28)  = 28


    """


    return f"{new_year:04d}-{new_month:02d}-{new_day:02d}"




def due_date(date_str: str) -> str:
    # Parse input string "YYYY-MM-DD" into year, month, day
    year, month, day = map(int, date_str.split("-"))

    # Step 1: Add 9 months to the current month
    # Example: April (month=4) + 9 = 13
    new_month = month + 9

    # Step 2: Adjust the year if new_month goes beyond 12
    # (new_month - 1) // 12 gives how many full years to add
    # For April + 9 = 13 → (13-1)//12 = 12//12 = 1 → add 1 year
    new_year = year + (new_month - 1) // 12

    # Step 3: Normalize the month back into 1–12 range
    # ((new_month - 1) % 12) + 1 wraps the month correctly
    # For 13 → (13-1)%12 + 1 = 12%12 + 1 = 0+1 = 1 → January
    new_month = ((new_month - 1) % 12) + 1

    # So April 2025 + 9 months = January 2026
    # (not December — because April→May(1), June(2), … December(8), January(9))

    # Step 4: Find the last day of the new month
    # calendar.monthrange(year, month) returns (weekday_of_first_day, number_of_days)
    # We take [1] to get the number of days in that month
    last_day = calendar.monthrange(new_year, new_month)[1]

    # Step 5: Clamp the day
    # If the original day is larger than the last day of the new month,
    # use the last valid day instead.
    # Example: "2025-05-31" + 9 months → February 2026 (only 28 days)
    # min(31, 28) = 28 → "2026-02-28"
    new_day = min(day, last_day)

    # Step 6: Format back into YYYY-MM-DD
    return f"{new_year:04d}-{new_month:02d}-{new_day:02d}"


# Example trace:
# Input: "2025-04-15"
# new_month = 4+9 = 13
# new_year = 2025 + (13-1)//12 = 2025+1 = 2026
# new_month = ((13-1)%12)+1 = (12%12)+1 = 0+1 = 1 → January
# last_day = 31 (January has 31 days)
# new_day = min(15, 31) = 15
# Output: "2026-01-15"

from utils.benchmark import benchmark
if __name__ == "__main__":
    TESTCASES = [
    (("2025-03-30",), "2025-12-30"),
    (("2025-04-27",), "2026-01-27"),
    (("2025-05-29",), "2026-02-28"),
    (("2026-06-30",), "2027-03-30"),
    (("2026-10-11",), "2027-07-11")
]
    print(get_due_date("2025-04-12"))
    scores = benchmark(
        {"normal": get_due_date},
        TESTCASES,
        10000
    )
    print(scores)
    unittest.main()