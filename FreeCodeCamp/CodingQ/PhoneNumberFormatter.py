"""

Phone Number Formatter
Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
"""

def format_number(number):

    country_code = number[0]

    area_code = number[1:4]

    local_start = number[4:7]
    local_end = number[7:]

    return f"+{country_code} ({area_code}) {local_start}-{local_end}"



def format_number_optimized(number):

    if len(number) != 11 or not number.isdigit():
        raise ValueError("Input must be  a string of exactly 10 digits.")
    

    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"


if __name__ == "__main__":
    print(format_number("05552340182"))
    print(format_number("15554354792"))
    a = "shdh."
    a = a.replace('.','')
    print(a)