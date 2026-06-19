""" 

Rental Cost
Given a rental timestamp, a return timestamp, and a rental tier, return the total cost of the rental including any late fees.

Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
The rental tier is the number of days before the rental is due back: 1, 3, or 7.
Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period. For example, a 1-day rental checked out at any time on March 15 is due back by 12:00 PM UTC on March 16.
Each day past the due date and time incurs a late fee.
Pricing is as follows:

Tier	Base cost	Late fee per day
1 day	$4.99	$3.99
3 days	$3.99	$2.99
7 days	$2.99	$0.99
Return the total cost rounded to two decimal places in the format "$D.CC".
"""


import unittest


class RentalCostTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1), "$4.99")

    def test2(self):
        self.assertEqual(get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1), "$12.97")

    def test3(self):
        self.assertEqual(get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3), "$3.99")

    def test4(self):
        self.assertEqual(get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3), "$9.97")

    def test5(self):
        self.assertEqual(get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7), "$2.99")

    def test6(self):
        self.assertEqual(get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7), "$358.40")


TESTCASES = [
    (("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1,), "$4.99"),
    (("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1,), "$12.97"),
    (("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3,), "$3.99"),
    (("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3,), "$9.97"),
    (("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7,), "$2.99"),
    (("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7,), "$358.40")
]


from datetime import datetime, timedelta

def get_rental_cost(rented, returned, tier):

    # Parse timestamps
    rental_time = datetime.fromisoformat(rented.replace("Z","+00:00"))
    return_time = datetime.fromisoformat(returned.replace("Z", "+00:00"))

    # Pricing table

    pricing = {
        1: { "base": 4.99, "late": 3.99},
        3: { "base": 3.99, "late": 2.99},
        7: { "base": 2.99, "late": 0.99}
    }

    # Due date = rental_date + tier days, due by 12:00 PM UTC
    due_date = (rental_time.date() + timedelta(days=tier))
    due_time = datetime.combine(due_date, datetime.min.time()).replace(hour=12, tzinfo=rental_time.tzinfo)

    total = pricing[tier]["base"]


    if return_time > due_time:
        # late days = ceil difference in days
        late_days = (return_time - due_time).days
        if (return_time - due_time).seconds > 0:
            late_days += 1
        
        total += late_days * pricing[tier]["late"]

    return f"${total:.2f}"

"""
Rental Fee / Due Date Logic Explained
=====================================

1. rental_time.date()
---------------------
Purpose:
    Extracts only the date portion (year, month, day) from a datetime object.
    The time component is discarded.

Return Type:
    datetime.date

Example:
    rental_time = datetime(2026, 6, 18, 18, 30)
    rental_time.date()
    # Output: 2026-06-18


2. timedelta(days=tier)
-----------------------
Purpose:
    Creates a time duration representing a specific number of days.
    Here, the number of days depends on the rental tier.

Return Type:
    datetime.timedelta

Example:
    timedelta(days=3)
    # Represents a duration of 3 days


3. rental_time.date() + timedelta(days=tier)
--------------------------------------------
Purpose:
    Calculates the due calendar date by adding the rental period
    to the rental date.

Example:
    rental_date = 2026-06-18
    tier = 3

    due_date = rental_date + 3 days
    # Output: 2026-06-21


4. datetime.combine(due_date, datetime.min.time())
--------------------------------------------------
Purpose:
    Converts a date object back into a datetime object by attaching
    a time component.

    datetime.min.time() represents midnight (00:00:00).

Return Type:
    datetime.datetime

Example:
    due_date = date(2026, 6, 21)

    datetime.combine(due_date, datetime.min.time())
    # Output: 2026-06-21 00:00:00


5. .replace(hour=12, tzinfo=rental_time.tzinfo)
------------------------------------------------
Purpose:
    Modifies the datetime object to:

    - Set the hour to 12 (noon)
    - Preserve the same timezone as rental_time

Return Type:
    datetime.datetime

Example:
    dt = datetime(2026, 6, 21, 0, 0)

    dt.replace(hour=12)
    # Output: 2026-06-21 12:00:00

Result:
    Due time becomes noon on the due date.


6. return_time - due_time
-------------------------
Purpose:
    Subtracts two datetime objects to determine how late
    the item was returned.

Return Type:
    datetime.timedelta

Example:
    return_time = datetime(2026, 6, 22, 13, 0)
    due_time    = datetime(2026, 6, 21, 12, 0)

    diff = return_time - due_time

    # Output:
    # 1 day, 1:00:00


7. .days and .seconds
---------------------
Purpose:
    Extract values from a timedelta object.

    .days
        Whole number of days.

    .seconds
        Remaining seconds after removing full days.

Example:
    diff = timedelta(days=1, hours=3)

    diff.days
    # Output: 1

    diff.seconds
    # Output: 10800 (3 hours)


8. Late Fee Rounding Logic
--------------------------
Code:

    late_days = (return_time - due_time).days

    if (return_time - due_time).seconds > 0:
        late_days += 1

Purpose:
    - Count complete late days.
    - If any extra hours/minutes/seconds exist,
      round up to the next full day.

Examples:

    1 day 0 hours late  -> 1 late day
    1 day 1 hour late   -> 2 late days
    2 days 5 mins late  -> 3 late days


Overall Flow
------------
1. Extract rental date.
2. Add rental tier days to get due date.
3. Create due datetime at midnight.
4. Change due time to noon while preserving timezone.
5. Compare return time against due time.
6. Calculate late days.
7. Round up partial days.
8. Apply base fee + late fee.
"""





from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": get_rental_cost},
        TESTCASES,
        10000
    )

    unittest.main()