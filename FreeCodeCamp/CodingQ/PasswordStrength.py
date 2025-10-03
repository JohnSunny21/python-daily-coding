"""
P@ssw0rd Str3ngth!
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
"""

def check_strength(password):

    rules_met = 0
    punctuation = "!@#$%^&*"

    if len(password) >= 8:
        rules_met += 1

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        rules_met += 1

    if any(c.isdigit() for c in password):
        rules_met += 1

    
    if any(c in punctuation for c in password):
        rules_met += 1


    if rules_met < 2:
        return "weak"
    elif rules_met < 4:
        return "medium"
    else:
        return "strong"
    


if __name__ == "__main__":
    print(check_strength("123456"))