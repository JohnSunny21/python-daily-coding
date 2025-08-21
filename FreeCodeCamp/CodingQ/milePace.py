"""
Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.

O/P : ====>

1. mile_pace(3, "24:00") should return "08:00".
2. mile_pace(1, "06:45") should return "06:45".
"""


def mile_pace(miles,duration):

    minutes , seconds = map(int, duration.split(":"))

    total_seconds = minutes * 60 + seconds

    # pace_seconds = total_seconds // miles
    pace_seconds = round(total_seconds / miles)
    # here we need to use the '/' 
    """
    if we use integer division '//' to compute pace_seconds, it truncates the decimal - which causes rounding errors. For example.
    total_seconds = 120 * 60 + 35 = 7235 for the input mile_pace(26.2,"120:35")
    pace_seconds = 7235 // 26.2 = 276.0 => truncated to 276

    but the correct pace is:

    7235 / 26.2 => 276.03 => rounded to 276.03 => 4 min 36 sec

    if we truncate instead of round, we might get 4.0:36.0 instead of 04:36
    """

    pace_min = pace_seconds // 60
    pace_sec = pace_seconds % 60

    return f"{pace_min:02}:{pace_sec:02}"


if __name__ == "__main__":
    print(mile_pace(26.2,"120:35"))
