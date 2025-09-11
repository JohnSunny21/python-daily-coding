import unittest
from ReverseSentece import reverse_sentence

class ReverseSentenceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(reverse_sentence("world hello"),"hello world")
        
    def test2(self):
        self.assertEqual(reverse_sentence("push commit git"),"git commit push")

    def test3(self):
        self.assertEqual(reverse_sentence("npm  install   apt    sudo"),"sudo apt install npm")

    def test4(self):
        self.assertEqual(reverse_sentence("import    default   function  export"),"export function default import")


if __name__ == "__main__":
    unittest.main()