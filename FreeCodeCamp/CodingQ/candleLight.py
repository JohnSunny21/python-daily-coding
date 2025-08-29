"""
===============================================>    Candlelight     <======================================================

Given an integer representing the number of candles you start with, and an integer representing how many burned candles it takes to create a new one, return the number of candles you will have used after creating and burning as many as you can.

For example, if given 7 candles and it takes 2 burned candles to make a new one:

Burn 7 candles to get 7 leftovers,
Recycle 6 leftovers into 3 new candles (1 leftover remains),
Burn 3 candles to get 3 more leftovers (4 total),
Recycle 4 leftovers into 2 new candles,
Burn 2 candles to get 2 leftovers,
Recycle 2 leftovers into 1 new candle,
Burn 1 candle.
You will have burned 13 total candles in the example.

===========================================================================
O/P :
1. burn_candles(7, 2) should return 13
2. burn_candles(10, 5) should return 12
3. burn_candles(20, 3) should return 29

"""

def burn_candles(candles, make_new):

    total_burned = candles
    leftovers = candles

    while leftovers >= make_new:
        new_candles = leftovers // make_new
        total_burned += new_candles
        leftovers = leftovers % make_new + new_candles

    return total_burned



if __name__ == "__main__":

    print(burn_candles(7,2))