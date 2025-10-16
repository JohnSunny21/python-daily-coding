"""
Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.


"""
import unittest

class EmailValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(validate("a@b.cd"),True)

    def test2(self):
        self.assertEqual(validate("hell.-w.rld@example.com"),True)

    def test3(self):
        self.assertEqual(validate(".b@sh.rc"),False)

    def test4(self):
        self.assertEqual(validate("example@test.c0"),False)

    def test5(self):
        self.assertEqual(validate("freecodecamp.org"),False)

    def test6(self):
        self.assertEqual(validate("develop.ment_user@c0D!NG.R.CKS"),True)

    def test7(self):
        self.assertEqual(validate("hello.@wo.rld"),False)
    
    def test8(self):
        self.assertEqual(validate("hello@world..com"),False)

    def test9(self):
        self.assertEqual(validate("git@commit@push.io"),False)



def validate(email):


    if  email.count('@') != 1:
        return False
    
    local, domain = email.split('@')

    if not local or local[0] == '.' or local[-1] == '.':
        return False
    
    for i in range(len(local)):
        if local[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-':
            return False
        
        if i > 0 and local[i] == '.' and local[i-1] == '.':
            return False
        
    

    if '.' not in domain:
        return False
    
    if domain.count('.') < 1:
        return False
    
    if domain.endswith('.') or len(domain.split('.')[-1]) < 2:
        return False
    
    for i in range(len(domain)):
        if domain[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!.-_':

            return False
        
        if i > 0 and domain[i] == '.' and domain[i-1] == '.':
            return False
    
    tld = domain.split('.')[-1]

    if not tld.isalpha() or len(tld) < 2:
        return False
    
    return True



if __name__ == "__main__":

    # print(validate("example@test.c0"))
    print(validate("a@b.cd"))
    unittest.main()

    

    

        
    


