"""  

2026 Winter Games Day 17: Closing Day
Given a 2D array of medal winners, return a medal count for each country as a CSV string.

In the given array, each sub-array represents a single event: [gold_winner, silver_winner, bronze_winner]

The returned CSV string should have the following format, with the first line being headers:

Country,Gold,Silver,Bronze,Total
country_name,gold_count,silver_count,bronze_count,total_medals
Separate new lines with the new line character ("\n").
Do not include spaces around commas or at the end of lines.
Sort the returned CSV by gold medal count, highest first. If two countries have the same gold medal count, sort the tied ones alphabetically.
For example, given:

[
  ["USA", "CAN", "NOR"],
  ["NOR", "USA", "CAN"],
  ["USA", "NOR", "SWE"]
]
Return:

"Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"
Which looks like this when printed:

Country,Gold,Silver,Bronze,Total
USA,2,1,0,3
NOR,1,1,1,3
CAN,0,1,1,2
SWE,0,0,1,1
"""

import unittest


class ClosingDayTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]), "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1")

      def test2(self):
          self.assertEqual(count_medals([["NOR","SWE","FIN"]]), "Country,Gold,Silver,Bronze,Total\nNOR,1,0,0,1\nFIN,0,0,1,1\nSWE,0,1,0,1")

      def test3(self):
          self.assertEqual(count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]), "Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2")

      def test4(self):
          self.assertEqual(count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]]), "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nFRA,1,1,0,2\nGER,1,1,0,2\nJPN,1,0,0,1\nSWE,1,0,1,2\nUSA,1,1,0,2\nCHN,0,0,1,1\nFIN,0,1,0,1\nITA,0,0,2,2\nKOR,0,1,0,1\nNOR,0,0,2,2") 

      def test5(self):
          self.assertEqual(count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]), "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nCHN,1,0,1,2\nESP,1,1,0,2\nFIN,1,0,1,2\nITA,1,1,0,2\nJPN,1,1,0,2\nNOR,1,1,0,2\nUSA,1,1,0,2\nFRA,0,0,1,1\nGER,0,0,1,1\nKOR,0,1,1,2\nMEX,0,0,2,2\nSWE,0,1,1,2")

      def test6(self):
          self.assertEqual(count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]), "Country,Gold,Silver,Bronze,Total\nUSA,3,1,0,4\nGER,2,2,1,5\nJPN,2,0,0,2\nSWE,2,1,1,4\nCAN,1,1,1,3\nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2")




def count_medals(winners):
    countries = {country for countries in winners for country in countries}
    medal_table = []

    for country in countries:
        gold = silver = bronze = 0
        for stat in winners:
            if country in stat:
                index = stat.index(country) + 1
                if index == 1:
                    gold += 1
                elif index == 2:
                    silver += 1
                elif index == 3:
                    bronze += 1
        total_count = gold + silver + bronze
        medal_table.append((country,gold,silver,bronze,total_count))
    
    medal_table.sort(key=lambda x: (-x[1], x[0]))
    result = ["Country,Gold,Silver,Bronze,Total"]
    for country,g,s,b,total in medal_table:
        result.append(f"{country},{g},{s},{b},{total}")

    return "\n".join(result)


""" 
=> If we continue with the above solution will only work for the scenario where stat has unique countries
=> If we consider a country has won botn Gold and bronze then the index() method will only return the 1st index not the second one so the solution
    will be wrong for some testcases
    
    
    => like this
              self.assertEqual(count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]), "Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2")

    so in the below solution i checked each position for a country so that the stat for each country is calculated properly
    """

def count_medals(winners):

    countries = {country for event in winners for country in event}

    medal_table = []
    for country in countries:
        gold = silver = bronze = 0
        for event in winners:
            if event[0] == country:
                gold += 1
            if event[1] == country:
                silver += 1
            if event[2] == country:
                bronze += 1
        
        total = gold + silver + bronze
        medal_table.append((country, gold, silver, bronze, total))

    
    medal_table.sort(key=lambda x: (-x[1], x[0]))

    result = ["Country,Gold,Silver,Bronze,Total"]
    for country,g,s,b,total in medal_table:
        result.append(f"{country},{g},{s},{b},{total}")
    

    return "\n".join(result)



def count_medals(events):
    from collections import defaultdict

    medals = defaultdict(lambda: {"Gold": 0, "Silver":0, "Bronze":0})

    for gold, silver, bronze in events:
        medals[gold]["Gold"] += 1
        medals[silver]["Silver"] += 1
        medals[bronze]["Bronze"] += 1


    medal_list = []
    for country, counts in medals.items():
        total = counts["Gold"] + counts["Silver"] + counts["Bronze"]
        medal_list.append((country, counts["Gold"], counts["Silver"],counts["Bronze"],total))


    medal_list.sort(key=lambda x: (-x[1], x[0]))

    lines = ["Country,Gold,Silver,Bronze,Total"]
    for country,g,s,b,total in medal_list:
        lines.append(f"{country},{g},{s},{b},{total}")

    return "\n".join(lines)





if __name__ == "__main__":
    unittest.main()