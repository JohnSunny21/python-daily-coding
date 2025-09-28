"""
CSV Header Parser
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading.
"""

def get_headings(csv):
    csv = csv.split(',')

    csv = [heading.strip() for heading in csv]

    return csv

def get_headings_optimized(csv):

    return [heading.strip() for heading in csv.split(',')]




if __name__ == "__main__":
    print(get_headings("name,age,city"))
    print(get_headings_optimized("name,age,city"))
    print(get_headings("first name,last name,phone"))
    print(get_headings("username , email , signup date "))