""" 

QR Decoder
Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation.
For example, given:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]
or given the same code with a different orientation:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]
Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.
"""
import unittest

class QRDecoderTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]), "000000000000000000000001")

    def test2(self):
        self.assertEqual(decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"]), "000000000000000000000001")

    def test3(self):
        self.assertEqual(decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]), "001101000011000000110100")

    def test4(self):
        self.assertEqual(decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]), "010001000100010101010110")

    def test5(self):
        self.assertEqual(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]), "010000100100100101001110")



def rotate(matrix):
    # Rotate 90 clockwise
    return ["".join(row[i] for row in reversed(matrix)) for i in range(len(matrix))]

    # We can also write it as
    # ["".join(row) for row in zip(*matrix[::-1])]
    """
    The zip usually takes two iterables. But with the * unpacking operator, it can take N iterables. here, each row string is an iterable
    of characters. so zip is aligning characters column-wise across all rows, which is exactly what we need for rotation.

    => [::-1] flips rows.
    => zip(*...) transposes( columns become rows).
    => join rebuilds strings.
    
    Together, they give you a clean 90 roatation
    for the anti-clock wise we use the ["".join(row) for row in zip(*matrix)][::-1]
    zip(*matrix) transposes the matrix (columns become rows).

    ["".join(row) for row in zip(*matrix)] builds the transposed matrix.

    [::-1] flips the order of rows (top ↔ bottom).

    That combination gives a 90° counter‑clockwise rotation.
    Both use the same idiom(zip(*...)) for transpose), but differ in whether you reverse rows before or after transposing.
    """

def has_markers(m):
    n = len(m)

    # top-left
    if not(m[0][0] == m[0][1] == m[1][0] == m[1][1] == "1"):
        return False
    
    # top-right
    if not(m[0][n-2] == m[0][n-1] == m[1][n-2] == m[1][n-1] == "1"):
        return False

    # bottom-left
    if not(m[n-2][0] == m[n-2][1] == m[n-1][0] == m[n-1][1] == "1"):
        return False
    
    return True

def decode_qr(matrix):
    # Try all 4 orientations

    for _ in range(4):
        if has_markers(matrix):
            break
        matrix = rotate(matrix)
    
    n = len(matrix)
    bits = []
    for i in range(n):
        for j in range(n):
            # skipping orientation markers
            if (i < 2 and j < 2) or (i < 2 and j >= n-2) or (i >= n-2 and j < 2):
                continue
            bits.append(matrix[i][j])

    return "".join(bits)

from utils.benchmark import benchmark
if __name__ == "__main__":
    TESTCASES = [
    ((["110011", "110011", "000000", "000000", "110000", "110001"],), "000000000000000000000001"),
    ((["100011", "000011", "000000", "000000", "110011", "110011"],), "000000000000000000000001"),
    ((["110011", "111111", "010000", "110000", "110011", "110100"],), "001101000011000000110100"),
    ((["011011", "101011", "101000", "100010", "110011", "111011"],), "010001000100010101010110"),
    ((["111100", "110001", "100011", "001101", "110011", "110011"],), "010000100100100101001110")
]
    scores = benchmark(
        {"optimal": decode_qr},
        TESTCASES,
        10000
    )

    print(scores)
    print(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]))

    unittest.main()
                

