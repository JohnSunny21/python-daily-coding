"""

Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].
"""

def speeding(speeds, limit):

    count = 0
    avg = 0
    result = []

    for speed in speeds:
        if speed > limit:
            count += 1
            result.append(speed)

    if len(result) >=1:
        over_speed = [speed - limit for speed in result]
        avg = sum(over_speed) / len(over_speed)

    
    return [count, avg]



def speeding_optimized(speeds, limit):

    overages = [speed - limit for speed in speeds if speed > limit]

    if not overages:
        return [0,0]
    
    return [len(overages), sum(overages)/len(overages)]



if __name__ == "__main__":
    print(speeding([50, 60, 55], 60))
    print(speeding([58,50,60,55],55))
    print(speeding([61,81,74,88,65,71,68],70))