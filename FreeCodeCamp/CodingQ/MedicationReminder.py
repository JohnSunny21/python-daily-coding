""" 


Medication Reminder
Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.

Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time it was last taken.
All given times will be in "HH:MM" (24-hour) format.
Use the following medication schedule:

Name	Schedule
Deployxitrin	08:00, 16:00
Debuggamanizole	07:00, 13:00, 21:00
Mergeflictamine	every 4 hours
Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m".
"""


import unittest


class MedicationReminderTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"), "Debuggamanizole in 2h 0m")

    def test2(self):
        self.assertEqual(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55"), "Deployxitrin in 1h 5m")

    def test3(self):
        self.assertEqual(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15"), "Mergeflictamine in 0h 45m")

    def test4(self):
        self.assertEqual(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59"), "Debuggamanizole in 0h 1m")

    def test5(self):
        self.assertEqual(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55"), "Debuggamanizole in 0h 5m")

    def test6(self):
        self.assertEqual(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00"), "Mergeflictamine in 3h 30m")


TESTCASES = [
    (([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00",), "Debuggamanizole in 2h 0m"),
    (([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55",), "Deployxitrin in 1h 5m"),
    (([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15",), "Mergeflictamine in 0h 45m"),
    (([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59",), "Debuggamanizole in 0h 1m"),
    (([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55",), "Debuggamanizole in 0h 5m"),
    (([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00",), "Mergeflictamine in 3h 30m")
]


def time_to_min(t):
    h, m = map(int, t.split(":"))

    return h * 60 + m



def medication_reminder(meds, current_time):

    curr_min = time_to_min(current_time)

    # Fixed schedules in minutes past midnight
    schedules = {
        "Deployxitrin": [time_to_min("08:00"), time_to_min("16:00")],
        "Debuggamanizole": [time_to_min("07:00"), time_to_min("13:00"), time_to_min("21:00")]
    }

    candidates = []

    for name, last_taken in meds:
        last_min = time_to_min(last_taken)

        if name == "Mergeflictamine":
            #Every 4 hours
            interval = 4 * 60
            next_min = last_min + interval

            # Advance until it's in the future
            while next_min <= curr_min:
                next_min += interval
            delta = next_min - curr_min
        else:

            # Fixed schedule medications
            times = schedules[name]
            future = [t for t in times if t > curr_min]

            if future:
                next_min = min(future)
            else:
                # Next day first dose
                next_min = times[0] + 1440
            
            delta = next_min - curr_min

        candidates.append((name, delta))


    next_med, time_delta = min(candidates, key=lambda x: x[1])

    hours = time_delta // 60
    minutes = time_delta % 60

    return f"{next_med} in {hours}h {minutes}m"

    






from utils.benchmark import benchmark


if __name__ == "__main__":
    print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"))
    scores = benchmark(
        {"first": medication_reminder},
        TESTCASES,
        10000
    )

    unittest.main()

