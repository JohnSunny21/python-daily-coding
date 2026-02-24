"""  


"""

import unittest


class BusinessDayCountTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(count_business_days("2026-02-24", "2026-02-26"), 3)

      def test2(self):
          self.assertEqual(count_business_days("2026-02-24", "2026-02-28"), 4)

      def test3(self):
          self.assertEqual(count_business_days("2026-02-21", "2026-03-01"), 5)

      def test4(self):
          self.assertEqual(count_business_days("2026-03-08", "2026-03-17"), 7)

      def test5(self):
          self.assertEqual(count_business_days("2026-02-24", "2027-02-24"), 262)



from datetime import datetime, timedelta

def count_business_days(start, end):

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    # User might pass the dates in reverse order accidentally.
    # without swap the function returns 0
    # With this swp the it gives the correct output.
    if start > end:
        start, end = end , start

    count = 0
    current = start

    while current <= end:
        # weekday() : Monday= 0 ... Sunday  = 6
        if current.weekday() < 5: # Mon-Fri
            count += 1
        current += timedelta(days=1)


    return count



if __name__ == "__main__":
    unittest.main()