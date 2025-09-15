"""
Thermostat Adjuster
Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

Return "heat" if the current temperature is below the target.
Return "cool" if the current temperature is above the target.
Return "hold" if the current temperature is equal to the target.
"""

def adjust_thermostat(temp, target):

    if temp < target:
        temp = "heat"
    elif temp > target:
        temp = "cool"
    else:
        temp = "hold"

    return temp


if __name__ == "__main__":

    print(adjust_thermostat(68,72))
    print(adjust_thermostat(75,72))