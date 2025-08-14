"""
=====================================================>      S P A C E J A M     <==================================================

Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces).

======================================================================================================================================
O/P : =>>>

1. space_jam("freeCodeCamp") should return "F  R  E  E  C  O  D  E  C  A  M  P".
2. space_jam("   free   Code   Camp   ") should return "F  R  E  E  C  O  D  E  C  A  M  P".
3. space_jam("Hello World?!") should return "H  E  L  L  O  W  O  R  L  D  ?  !".


"""

def space_jam_first(s):
    res = list(s.strip().replace(" ",""))

    return '  '.join(res).upper()

"""
In the above example
there's a subtle issue in how you're applying .upper() that affects non-alphabetical characters. Let's break it down:

The .upper() call at the end applies to the entire joined string, which means it also affects non-alphabetical characters 
if they have case variants (e.g., accented letters or Unicode symbols). While most symbols like @, #, ! remain unchanged, 
it's safer and more precise to only uppercase alphabetic characters before joining.

Accented Letters and Unicode Symbols Are
- Accented letters are characters with diacritical marks, commonly used in languages like French, Spanish, German, etc.
- Examples: é, ñ, ü, ç, ø
- Unicode symbols include a vast range of characters beyond basic ASCII — emojis, currency signs, math symbols, and more.
- Examples: ©, €, ✓, π, ∑, 😀

How Does .upper() Affect Them?
Python’s .upper() method is Unicode-aware, meaning it will attempt to convert any lowercase letter — including accented ones 
— to its uppercase equivalent if one exists.


print("é".upper())   # ➜ É
print("ñ".upper())   # ➜ Ñ
print("ü".upper())   # ➜ Ü
print("ç".upper())   # ➜ Ç
print("ø".upper())   # ➜ Ø

These are all valid transformations -- .upper() knows how to handle them.



Examples of Unicode Symbols that stay the same

print("©".upper())   # ➜ ©
print("✓".upper())   # ➜ ✓
print("π".upper())   # ➜ Π (Greek lowercase pi → uppercase Pi)
print("∑".upper())   # ➜ ∑ (already uppercase)
print("😀".upper()) 

- Some symbols do change (like Greek letters).
- Others stay the same (like emojis, currency signs, math symbols).


The problem with the first approach is  we might unintentionally transform the characters
we didn't expect - especailly in multilinqual symbol-rich input.


"""
# This is the improvised version
def space_jam(s):
    cleaned = s.replace(" ","")
    transformed = [char.upper() if char.isalpha() else char for char in cleaned]

    return '  '.join(transformed)



if __name__ == "__main__":

    print(space_jam("freeCodeCamp"))
    print(space_jam("   free   Code   Camp   "))