"""
Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.

"""

import unittest

class ExtensionExtractorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_extension("document.txt"),"txt")




def get_extension(filename):
    if not '.' in filename:
        return "none"
    extension = filename.split(".")
    if not extension[-1]:
        return "none"
    else:
        return extension[-1]
    
def get_extension_optimized(filename):
    if not '.' in filename or filename.endswith('.'):
        return "none"
    return filename.rsplit('.',1)[1]
    
if __name__ == "__main__":
    print(get_extension("document.txt"))
    print(get_extension("README"))
    print(get_extension("final.draft."))
    print(get_extension_optimized("document.txt"))
    
