"""  

Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

* 
 *
* 
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 ** 
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.
"""

import unittest

class SnowflakeGeneratorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(generate_snowflake("* \n *\n* "),"*  *\n ** \n*  *")

    def test2(self):
        self.assertEqual(generate_snowflake("X=~"),"X=~~=X")
    
    def test3(self):
        self.assertEqual(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ")," X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ")

    def test4(self):
        self.assertEqual(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"),"*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *")

    def test5(self):
        self.assertEqual(generate_snowflake("*  -\n * -\n*  -"),"*  --  *\n * -- * \n*  --  *")


def generate_snowflake(crystals):

    lines = crystals.split("\n")

    for i in range(len(lines)):
        lines[i] = lines[i] + lines[i][::-1]
    

    return "\n".join(lines)

def snowflake_generator(crystals):

    lines = crystals.split("\n")

    mirrored_lines = [line + line[::-1] for line in lines]

    return "\n".join(mirrored_lines)

def snowflake_generator_oneliner(crystals):

    return "\n".join([line + line[::-1] for line in crystals.split("\n")])



if __name__ == "__main__":
    unittest.main()