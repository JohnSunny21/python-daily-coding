""" 

Movie Night
Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.
"""


import unittest

class MovieNightTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_movie_night_cost("Saturday", "10:00pm", 1), "$12.00")

    def test2(self):
        self.assertEqual(get_movie_night_cost("Sunday", "10:00am", 1), "$10.00")

    def test3(self):
        self.assertEqual(get_movie_night_cost("Tuesday", "7:20pm", 2), "$10.00")

    def test4(self):
        self.assertEqual(get_movie_night_cost("Wednesday", "5:40pm", 3), "$30.00")

    def test5(self):
        self.assertEqual(get_movie_night_cost("Monday", "11:50am", 4), "$32.00")

    def test6(self):
        self.assertEqual(get_movie_night_cost("Friday", "4:30pm", 5), "$50.00")

    def test7(self):
        self.assertEqual(get_movie_night_cost("Tuesday", "11:30am", 1), "$5.00")

def get_movie_night_cost_normal(day, showtime, number_of_tickets):

    if day in ["Friday", "Saturday", "Sunday"]:
        ticket_cost = 12
    elif day in ["Monday","Wednesday", "Thursday"]:
        ticket_cost = 10

    hour, minute = map(int,showtime[:-2].split(":"))
    meridiem = showtime[-2:]
    if not(hour >= 5 and meridiem == "pm") and day != "Tuesday":
        ticket_cost -= 2
    if day == "Tuesday":
        ticket_cost = 5


    total_ticket_cost = number_of_tickets * ticket_cost

    return f"${total_ticket_cost:.2f}"

""" 

=> The above solution is very close but there are two subtle issues:
    1. Tuesday logic order
        Right now you check for matinee discount before overriding Tuesday pricing.
        That means if the showtime is before 5pm on Tuesday, you first subtract $2, then set it to $5. It still 
        ends up correct, but the logic is a bit confusing. it's clearer to handle Tuesday first, since it overrides everything.

    2. Matinee condition
        if not(hour >= 5 and meridiem == "pm") and day != "Tuesday":
            ticket_cost -= 2
        This works, but it's harder to read. It's basically saying "if it's not 5pm or later, and not Tuesday." A more explicit check is easier to maintain:

        if day != "Tuesday" and (meridiem == "am" or (meridiem == "pm" and hour < 5)):
        ticket_cost -= 2

    

"""

def get_movie_night_cost_refined(day, showtime, number_of_tickets):

    if day == "Tuesday":
        ticket_cost = 5
    elif day in ["Friday","Saturday","Sunday"]:
        ticket_cost = 12
    else: # Monday, Wednesday, Thursday
        ticket_cost = 10

    hour, minute = map(int, showtime[:-2].split(":"))
    meridiem = showtime[-2:]

    if day != "Tuesday":
        if meridiem == "am" or (meridiem == "pm" and hour < 5):
            ticket_cost -= 2

    total_ticket_cost = number_of_tickets * ticket_cost

    return f"${total_ticket_cost:.2f}"

""" 
=> Tuesday -> always $5.
=> Weekend -> $12.
=> Weekday -> $10, minus $2  if matinee.
"""


def get_movie_night_cost(day, showtime, number_of_tickets):

    weekend = {"Friday","Saturday","Sunday"}

    import re
    match = re.match(r"(\d+):(\d+)(am|pm)",showtime)
    hour, minute, meridian = int(match.group(1)), int(match.group(2)), match.group(3)

    if meridian == "pm" and hour != 12:
        hour += 12
    if meridian == "am " and hour == 12:
        hour = 0

    # Base price
    if day == "Tuesday":
        price = 5.00
    elif day in weekend:
        price = 12.00
    else:
        price = 10.00

    # Matinee discount (before 5pm, except Tuesday)
    if day != "Tuesday" and hour < 17:
        price -= 2.00
    
    total = price * number_of_tickets

    return f"${total:.2f}"


from utils.benchmark import benchmark
if __name__ == "__main__":

    TESTCASES = [
    (("Saturday", "10:00pm", 1,), "$12.00"),
    (("Sunday", "10:00am", 1,), "$10.00"),
    (("Tuesday", "7:20pm", 2,), "$10.00"),
    (("Wednesday", "5:40pm", 3,), "$30.00"),
    (("Monday", "11:50am", 4,), "$32.00"),
    (("Friday", "4:30pm", 5,), "$50.00"),
    (("Tuesday", "11:30am", 1,), "$5.00")
]
    scores = benchmark(
        {"normal": get_movie_night_cost_normal,
         "refined": get_movie_night_cost_refined,
         "optimal": get_movie_night_cost},
        TESTCASES,
        10000
    )
    unittest.main()