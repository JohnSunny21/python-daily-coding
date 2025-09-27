"""
Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).




 Step 1: digits_only = re.sub(r'\D', '', phone)
What it does:
- re.sub() is a regex-based substitution function.
- r'\D' means “any character that is NOT a digit”.
- '' means we replace those non-digit characters with nothing (i.e., remove them).
- So this line strips out all formatting characters like +, (, ), -, and spaces.
Example:
phone = "+91 (999) 123-4567"
digits_only = re.sub(r'\D', '', phone)
# Result: '919991234567'


This cleaned version is used later to check for repeated digits.

🔍 Step 2: match = re.match(r'^\+(\d+)\((\d{3})\)(\d{3})-(\d{4})$', phone.replace(' ', ''))
What it does:
- re.match() checks if the string matches a pattern from the beginning.
- The pattern is a regular expression that defines the phone format.
- phone.replace(' ', '') removes spaces before matching.
Regex Breakdown:
^\+(\d+)       # Starts with '+' followed by one or more digits (country code)
\((\d{3})\)    # Then a 3-digit area code inside parentheses
(\d{3})        # Then 3 digits (local start)
-(\d{4})$      # Then a dash and 4 digits (local end), and end of string


What are "groups"?
- The parts inside parentheses () are called groups.
- re.match(...).groups() returns a tuple of matched values.
Example:
phone = "+91 (999) 123-4567"
match.groups() → ('91', '999', '123', '4567')


These are assigned to:
country_code = '91'
area_code = '999'
local_start = '123'
local_end = '4567'



🔍 Step 3: Rule Checks
Rule 1: Country code
if len(country_code) > 2 or not country_code.startswith('0'):


- Spam if country code is too long or doesn’t start with '0'
Rule 2: Area code
if area > 900 or area < 200:


- Spam if area code is out of range
Rule 3: Local number sum
local_sum = sum(int(d) for d in local_start)
if str(local_sum) in local_end:


- Spam if sum of first 3 digits appears in last 4 digits
Rule 4: Repeated digits
if re.search(r'(\d)\1{3,}', digits_only):


- (\d)\1{3,} means: a digit repeated 4 or more times in a row
- Spam if this pattern is found



Pattern: r'(\d)\1{3,}'
This is a regular expression used to find four or more of the same digit in a row.

🧠 Breakdown
|  |  | 
| (\d) |  | 
| \1 |  | 
| {3,} |  | 
| \1{3,} |  | 
|  | (\d)\1{3,} | 


This pattern is used to detect spam numbers that have suspicious repetition like '1111' or '9999' — which are often used in fake or bot-generated numbers.



"""


import re
def is_spam(number):

    # Remove formatting characters like '+,-,' ',etc.'
    digits_only = re.sub(r'\D','',number)

    match = re.match(r'^\+(\d+)\((\d{3})\)(\d{3})-(\d{4})$',number.replace(' ',''))

    if not match:
        return False
    
    country_code, area_code, local_start, local_end = match.groups()

    # Rule 1: Country code > 2 digits or doesn't start with '0'

    if len(country_code) > 2 or not country_code.startswith('0'):
        return True
    
    area = int(area_code)

    # Rule 2: Area code > 900 or < 200

    if area > 900 or area < 200:
        return True
    

    # Rule 3: Sum of CCC appears in DDDD
    local_sum = sum(int(d) for d in local_start)
    if str(local_sum) in local_end:
        return True
    

    # Rule 4: Same digit 4+ times in a row
    if re.search(r'(\d)\1{3,}',digits_only):
        return True
    
    return False
    



    



if __name__ == "__main__":
   print(is_spam("+0 (200) 234-0182"))
   print(is_spam("+091 (555) 309-1922"))
   print(is_spam("+1 (555) 435-4792"))
   print(is_spam("+0 (955) 234-4364"))
   print(is_spam("+0 (155) 131-6943"))