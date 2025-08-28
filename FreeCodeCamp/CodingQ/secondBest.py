"""
===============================>    Second Best <====================================

Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.

=========================================================================
O/P:
1. get_laptop_cost([1500, 2000, 1800, 1400], 1900) should return 1800
2. get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) should return 1800
"""

def get_laptop_cost1(laptops,budget):

    valid_prices = sorted(set(laptops),reverse=True)

# This solution includes the sorting of the laptop prices but the real problem does not need to sort the prices but use only the actual order 
# ignoring the duplicates
    if len(valid_prices) >= 2:
        if valid_prices[1] <= budget:
            return valid_prices[1]
        elif valid_prices[0] <= budget:
            return valid_prices[0]
    if len(valid_prices) == 1:
        if valid_prices <= budget:
            return valid_prices[0]
    else:
        return 0
    
def get_laptop_cost(laptops,budget):

    seen = set()
    unique_ordered = []

    for price in laptops:
        if price not in seen:
            seen.add(price)
            unique_ordered.append(price)

    if len(unique_ordered) >= 2:
        second_last = unique_ordered[-2]
        last = unique_ordered[-1]

        if second_last <=budget:
            return second_last
        elif last <= budget:
            return last
    elif len(unique_ordered) == 1:
        if unique_ordered[0] <= budget:
            return unique_ordered[0]
        

    return 0

if __name__ == "__main__":

    print( get_laptop_cost([1500, 2000, 1800, 1400], 1900))
    print(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450))