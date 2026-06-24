""" 


DNA Mutations
Given two DNA strands of equal length, return an array of indexes where the strands differ (mutations).

DNA strands are strings made up of the characters "A", "T", "C", and "G"
Return the indexes in ascending order
If there are no mutations, return an empty array
"""



import unittest

class DnaMutationTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(detect_mutations("ATCG", "ATGG"), [2])

    def test2(self):
        self.assertEqual(detect_mutations("ATGCGTACGTTAGC", "ATGCATACGATTGC"), [4, 9, 11])

    def test3(self):
        self.assertEqual(detect_mutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG"), [])

    def test4(self):
        self.assertEqual(detect_mutations("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG"), [15, 16, 17, 18])

    def test5(self):
        self.assertEqual(detect_mutations("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT"), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, 27, 28])


TESTCASES = [
    (("ATCG", "ATGG",), [2]),
    (("ATGCGTACGTTAGC", "ATGCATACGATTGC",), [4, 9,11]),
    (("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG",), []),
    (("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG",), [15, 16, 17, 18]),
    (("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT",), [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, 27, 28])
]



def detect_mutations(strand1, strand2):

    mutations = []

    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            mutations.append(i)

    return mutations




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": detect_mutations},
        TESTCASES, 
        10000
    )


    unittest.main()