import unittest
from SentenceCapitalizer import capitalize_user

class SentenceCapitalizerText(unittest.TestCase):

    def test1(self):
        self.assertEqual(capitalize_user("this is a simple sentence."),"This is a simple sentence.")


    def test2(self):
        self.assertEqual(capitalize_user("hello world. how are you?"),"Hello world. How are you?")

    def test3(self):
        self.assertEqual(capitalize_user("i did today's coding challenge... it was fun!!"),"I did today's coding challenge... It was fun!!")

    def test4(self):
        self.assertEqual(capitalize_user("crazy!!!strange???unconventional...sentences."),"Crazy!!!Strange???Unconventional...Sentences.")

    def test5(self):
        self.assertEqual(capitalize_user("there's a space before this period . why is there a space before that period ?"),"There's a space before this period . Why is there a space before that period ?")


if __name__ == "__main__":

    unittest.main()