"""
Email Sorter
On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

Sorting should be case-insensitive.
If more than one email has the same domain, sort them by their username.
Return an array of the sorted addresses.
Returned addresses should retain their original case.
For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].

"""

import unittest

class EmailSorterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(sort_email(["jill@mail.com", "john@example.com", "jane@example.com"]),["jane@example.com", "john@example.com", "jill@mail.com"])

    def test2(self):
        self.assertEqual(sort_email(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]),["bob@mail.com", "carol@mail.com", "alice@zoo.com"])

    def test3(self):
        self.assertEqual(sort_email(["user@z.com", "user@y.com", "user@x.com"]),["user@x.com", "user@y.com", "user@z.com"])
    
    def test4(self):
        self.assertEqual(sort_email(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]),["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"])

    def test5(self):
        self.assertEqual(sort_email(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]),["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"])


def sort_email(emails):

    sorted_emails = sorted(emails, key= lambda x: x.split("@")[-1].lower())
    
    
    count = 1

    for i in range(len(sorted_emails) - 1):
        if sorted_emails[i].split('@')[-1].lower() == sorted_emails[i+1].split('@')[-1].lower():
            count += 1
        elif sorted_emails[i].split('@')[-1].lower() != sorted_emails[i+1].split('@')[-1].lower():
            break
    
    sorted_emails2 = sorted(sorted_emails[:count], key= lambda x: x.split('@')[0].lower())
    
    final_sort = sorted_emails2 + sorted_emails[count:]
    
    return final_sort

def sort_email(emails):
    emails.sort(key=lambda email: email.split('@')[0].lower())
    emails.sort(key=lambda email: email.split('@')[1].lower())
    return emails
    

if __name__ == "__main__":
    # print(sort_email(["jill@mail.com", "john@example.com", "jane@example.com","sunny@gmail.com"]))
    # print(sort_email_refined(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]))
    unittest.main()
  