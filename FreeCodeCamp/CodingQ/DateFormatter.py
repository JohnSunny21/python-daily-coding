"""

Date Formatter
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".
"""

import unittest

from datetime import datetime

class DateFormatterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(format_code("December 6, 2025"), "2025-12-06")

    def test2(self):
        self.assertEqual(format_code("January 1, 2000"), "2000-01-01")
    
    def test3(self):
        self.assertEqual(format_code("November 11, 1111"),"1111-11-11")
    
    def test4(self):
        self.assertEqual(format_code("September 7, 512"), "512-09-07")

    def test5(self):
        self.assertEqual(format_code("May 4, 1950"),"1950-05-04")

    def test6(self):
        self.assertEqual(format_code("February 29, 1992"), "1992-02-29")



def format_code(date_string):
    """
        Detailed issue explanation
    - Problem with %Y in Python’s strptime:
    - Behavior: %Y expects a 4‑digit year in parsing. "512" (3 digits) does not match, causing ValueError.
    - Impact: "September 7, 512" fails with strptime("%B %d, %Y").
    - Formatting with %Y in strftime:
    - Behavior: %Y outputs the numeric year without extra leading zeros; it does not preserve any padded input string you may have constructed.
    - Impact: If you tried to pad the year to "0512", datetime still represents year as 512 internally and formats it as "512" in most contexts; manual string composition is needed to force "0512" (but your tests require "512").
    - Solution approach:
    - Parse manually using a regex that captures month name, day, and year as strings.
    - Validate month/day (and leap years) programmatically.
    - Format with year as-is (no padding), and pad month/day to two digits.
    This approach ensures all six test cases pass, including the 3‑digit year case, and avoids strptime’s strict 4‑digit year requirement.

        """
    # If we have the need to accept the variable length years, like September 7, 512 which is failing currently 
    # We need to pad the zeroes before it
    # so changing the code

    # "September 7, 512" -> expected "512-09-07", but %Y rejects  3-digits years, causing ValueError
    # To make all six pass, parse the components  manually (month, name, day, year) and format them, instead of relying on %Y in strptime
    parts = date_string.split(", ")
    month_day, year = parts
    if len(year) < 4:
        year = year.zfill(4) # pad with leading zeroes

    normalized = f"{month_day}, {year}"

    date_object = datetime.strptime(normalized,"%B %d, %Y")

    return date_object.strftime("%Y-%m-%d")

   

import re

MONTHS = {
        "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

def format_code(date_str):

    # Match: Month day, year (Month full name, day and year are digits)

    m = re.match(r"^\s*([A-Za-z]+)\s+(\d{1,2}),\s+(\d{1,4})\s*$",date_str)
    if not m:
        raise ValueError("Invalid format")
    
    month_name, day_str , year_str = m.groups()

    # Validate month name

    if month_name not in MONTHS:
        raise ValueError("Invalid month name")
    
    month = MONTHS[month_name]
    day = int(day_str)
    year = int(year_str) # Keep as integer; do not zero-pad the year

    # Basic range checks

    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    
    if not (1 <= day <= 31):
        raise ValueError("Invalid Calendar Date")
    
    # Optional:  precise day validation including leap year
    if not _valid_day(year, month, day):
        raise ValueError("Invalid Calendar Date")
    
    
    # Year with no forced leading zeroes month/day padded to two digits

    return f"{year}-{month:02d}-{day:02d}"


def _valid_day(year, month, day):

    # Days per month with leap year handling

    if month in (1, 3, 5, 7, 8 , 10, 12):
        return day <= 31
    
    if month in (2, 4 ,6, 9, 11):
        return day <= 30
    
    # February

    if _is_leap(year):
        return day <= 29
    return day <= 28

def _is_leap(year):
    # Gregorian leap year rules

    return (year % 4 == 0 ) and (year % 100 != 0 or year % 400 == 0)









if __name__ == "__main__":
    print(format_code("January 15, 2023"))
    unittest.main()

