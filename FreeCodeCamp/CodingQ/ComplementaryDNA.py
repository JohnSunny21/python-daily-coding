"""
Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
"""

import unittest

class ComplementaryDNATest(unittest.TestCase):

    def test1(self):
        self.assertEqual(complementary_dna_refined("ACGT"),"TGCA")

    def test2(self):
        self.assertEqual(complementary_dna_refined("ATGCGTACGTTAGC"),"TACGCATGCAATCG")

    def test3(self):
        self.assertEqual(complementary_dna("GGCTTACGATCGAAG"),"CCGAATGCTAGCTTC")

    def test4(self):
        self.assertEqual(complementary_dna_refined("GATCTAGCTAGGCTAGCTAG"),"CTAGATCGATCCGATCGATC")



def complementary_dna(strand):
    result = ''
    for i in strand:
        if i == 'A':
            result += 'T'
        elif i == 'C':
            result += 'G'
        elif i == 'T':
            result += 'A'
        elif i == 'G':
            result += 'C'

    return result



def complementary_dna_optimized(strand):

    complementary = {'A':'T','C':'G','T':'A','G':'C'}

    return ''.join(complementary[nucleotide] for nucleotide in strand)


def complementary_dna_refined(strand):

    complementary = {'A':'T','C':'G','T':'A','G':'C'}
    result = ''

    for base in strand:
        if base in complementary:
            result += complementary[base]
        else:
            raise ValueError(f"Invalid DNA base: {base}")
        
    return result


if __name__ == "__main__":
    print(complementary_dna("ACGT"))
    unittest.main()
