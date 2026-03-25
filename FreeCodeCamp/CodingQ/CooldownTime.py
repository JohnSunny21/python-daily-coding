""" 

Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.

"""


import unittest


class CooldownTimeTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"), True)

    def test2(self):
        self.assertEqual(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"), False)

    def test3(self):
        self.assertEqual(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"), True)

    def test4(self):
        self.assertEqual(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"), False)




from datetime import datetime, timedelta

def can_retake(finish_time, current_time):

    fmt = "%Y-%m-%dT%H:%M:%S"

    finished_time = datetime.strptime(finish_time,fmt)
    current_time  = datetime.strptime(current_time,fmt)

    diff = current_time - finished_time

    return diff >= timedelta(hours=48)


from utils.benchmark import benchmark

if __name__ == "__main__":
    TESTCASES = [
    (("2026-03-23T08:00:00", "2026-03-25T14:00:00",), True),      
    (("2026-03-24T14:00:00", "2026-03-25T10:00:00",), False),     
    (("2026-03-23T09:25:00", "2026-03-25T09:25:00",), True),      
    (("2026-03-25T11:50:00", "2026-03-23T11:49:59",), False)      
]
    scores = benchmark(
        {"optimal": can_retake},
        TESTCASES,
        10000
    )
    print(scores)

    unittest.main()