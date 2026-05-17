""" 


Mongo ID Date
Given a MongoDB ID string, return its creation time as an ISO 8601 string.

A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a base-16 integer.
For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which is 1778994000 in decimal, representing a creation time of "2026-05-17T05:00:00.000Z".
"""



import unittest



class MongoIdDateTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(mongo_id_to_date("6a094b50bcf86cd799439011"), "2026-05-17T05:00:00.000Z")

    def test2(self):
        self.assertEqual(mongo_id_to_date("695344eb1f4a4c1123042128"), "2025-12-30T03:20:11.000Z")

    def test3(self):
        self.assertEqual(mongo_id_to_date("386da62df34123ac54617e56"), "2000-01-01T07:01:01.000Z")

    def test4(self):
        self.assertEqual(mongo_id_to_date("69f571c3d7711807afd3dd55"), "2026-05-02T03:38:43.000Z")

    def test5(self):
        self.assertEqual(mongo_id_to_date("68adce01c0e1144d0a90295a"), "2025-08-26T15:08:49.000Z")


TESTCASES = [
    (("6a094b50bcf86cd799439011",), "2026-05-17T05:00:00.000Z"),
    (("695344eb1f4a4c1123042128",), "2025-12-30T03:20:11.000Z"),
    (("386da62df34123ac54617e56",), "2000-01-01T07:01:01.000Z"),
    (("69f571c3d7711807afd3dd55",), "2026-05-02T03:38:43.000Z"),
    (("68adce01c0e1144d0a90295a",), "2025-08-26T15:08:49.000Z")
]




from datetime import datetime

def mongo_id_to_date(s):

    # First 8 characters  -> hex timestamp
    timestamp_hex = s[:8]
    timestamp = int(timestamp_hex, 16)  # converting the hex to decimal

    # Convert to UTC datetime

    dt = datetime.utcfromtimestamp(timestamp)

    return dt.isoformat() + ".000Z"







from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": mongo_id_to_date},
        TESTCASES,
        10000
    )

    unittest.main()
