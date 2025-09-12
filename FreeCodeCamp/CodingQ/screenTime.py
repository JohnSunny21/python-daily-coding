"""
Screen Time
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.

"""

def too_much_screen_time(hours):

    if len(hours) != 7:
        raise ValueError("Input must be a list of 7 integers.")
    
    # Rule 1: Any single day >= 10 hours

    if any(day >= 10 for day in hours):
        return True
    
    # Rule 2: Any 3-day average >= 8 hours

    for i in range(5): # Only 5 possible 3-day windows in a 7-day week
        avg = sum(hours[i:i+3]) / 3

        if avg >= 8:
            return True
        
    # Rule 3: Weekley average >= 6 hours
    weekly_avg = sum(hours) / 7

    if weekly_avg >= 6:
        return True

    return False






if __name__ == "__main__":
    print(too_much_screen_time([1,2,3,4,5,6,7]))