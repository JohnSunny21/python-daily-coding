"""
Workstyle: Full Remote
Salary: $60,000-$70,000 USD
*Overseas applicants are welcome (Visas provided)
Requirements:
-3+ years experience
-Java/Spring preferred, or any OOP language
-RDBMS, NoSQL databases, distributed caches
-data structures, algorithms, object oriented programming
-concurrency and distributed computing
-Implementing platform components, RESTFUL APIs, Pub/Sub systems, database clients
-microservices and event-driven architectures
"""

import unittest

class TipCalculatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(calculate_tips("$10.00","25%"),["$1.50","$2.00","$2.50"])

    def test2(self):
        self.assertEqual(calculate_tips("$89.67","26%"),["$13.45","$17.93","$23.31"])

    def test3(self):
        self.assertEqual(calculate_tips("$19.85","9%"),["$2.98","$3.97","$1.79"])



def calculate_tips(meal_price,custom_tip):

    meal_price = float(meal_price[1:])
    fifteen_percent = meal_price * 0.15
    twenty_percent = meal_price * 0.20
    custom_tip_percent = meal_price * int(custom_tip[:-1])/ 100

    result_list = []
    result_list.append(f'${fifteen_percent:.2f}')
    result_list.append(f'${twenty_percent:.2f}')
    result_list.append(f'${custom_tip_percent:.2f}')




    return result_list


def calculate_tips_refined(meal_price, custom_tip):

    # Extract numeric values

    price = float(meal_price.strip('$'))
    custom_percent = float(custom_tip.strip('%'))

    # Calculate tips

    tips = [
        round(price * 0.15,2),
        round(price * 0.20),
        round(price * (custom_percent / 100), 2)
    ]

    return [f"${tip:.2f}" for tip in tips]


if __name__ == "__main__":

    print(calculate_tips("$10.00","25%"))
    print(calculate_tips_refined("$10.00","25%"))
    unittest.main()
