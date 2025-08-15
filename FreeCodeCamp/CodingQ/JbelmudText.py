"""
=================================================>      Jbelmud Text        <=========================================================
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.

==================================================================================================================================
O/P : ===>

1. jbelmu("hello world") should return "hello wlord".
2. jbelmu("i love jumbled text") should return "i love jbelmud text".
3. jbelmu("freecodecamp is my favorite place to learn to code") should return "faccdeeemorp is my faiortve pacle to laern to cdoe".
4. jbelmu("the quick brown fox jumps over the lazy dog") should return "the qciuk borwn fox jmpus oevr the lazy dog".
"""

def jbelmu_first(text):

    final = []
    for word in text.split(" "):
        res = word[0] + ''.join(sorted(word[1:len(word)-1])) + word[-1]
        final.append(res)
    return ' '.join(final)

"""
The solution is impressively close to perfect.
we will highlight both what’s working and where it can be improved.

What we Did Well
- Splitting words: text.split(" ") correctly separates the input into words.
- Preserving first and last letters: word[0] and word[-1] are used properly.
- Sorting middle letters: sorted(word[1:len(word)-1]) is accurate.
- Joining transformed words: ' '.join(final) reconstructs the sentence.



⚠️ Minor Edge Case to Improve
Current  code assumes every word has at least 2 characters. But what if the word is:
- A single letter (e.g. "i")
- Two letters (e.g. "to")
In these cases:
- "i" should stay "i"
- "to" should stay "to" (no middle letters to sort)
Your current code will still work, but it’s safer to explicitly handle these cases to avoid unnecessary slicing or sorting.

"""
def jbelmu(text):
    final = []
    for word in text.split(" "):
        if len(word) <= 2:
            final.append(word)
        else:
            #- word[1:-1] is cleaner than word[1:len(word)-1]
            middle = ''.join(sorted(word[1:-1]))
            final.append(word[0] + middle + word[-1])

    return ' '.join(final)



if __name__ == "__main__":
    print(jbelmu("hello world"))
    print(jbelmu("i love jumbled text"))