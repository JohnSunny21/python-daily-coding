"""
Sentence Capitalizer
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

All other characters should be preserved.
Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

"""

import re

def capitalize_user(paragraph):

    

    """
    Here in the re.split() method there will some extra '' strings or empty strings because that's how the re.split() works when 
    capturing groups are used in the regex.

    🔍 Why It Happens
        Your pattern:
        re.split(r'([.?!]+)(\s*)', paragraph)


        has two capturing groups:
        - ([.?!]+) → captures punctuation
        - (\s*) → captures the whitespace after it
        When you use capturing groups in re.split(), the matched delimiters are included in the result. If there's no match for a group (like no whitespace after a punctuation), it returns an empty string ''.

        🧪 Example Breakdown
        For this input:
        paragraph = "hello world. how are you?  "



        The split result:
        [
        'hello world',  # sentence before first punctuation
        '.',            # punctuation
        ' ',            # space after '.'
        'how are you',  # next sentence
        '?',            # punctuation
        '',             # no space after '?'
        ''              # trailing empty string from end of input
        ]


        - The '' after ? → because (\s*) matched zero spaces
        - The final '' → because there's nothing left after the last match

        ✅ How to Clean It Up
        If you want to remove empty strings from the result:
        sentences = [s for s in re.split(r'([.?!]+)(\s*)', paragraph) if s.strip()]


        Or if you're reconstructing sentences, use a loop that groups every 3 items:
        for i in range(0, len(parts) - 2, 3):
            sentence = parts[i] + parts[i+1] + parts[i+2]



     The code explanation

     
     What re.split(r'([.?!]+)(\s*)', paragraph) Produces
This regex splits the paragraph at sentence-ending punctuation, but also keeps the punctuation and the space after it by using capturing groups.
So for:
paragraph = "hello world. how are you? really!"


You get:
parts = [
  'hello world',  # sentence
  '.',            # punctuation
  ' ',            # space
  'how are you',  # sentence
  '?',            # punctuation
  ' ',            # space
  'really',       # sentence
  '!',            # punctuation
  ''              # no space after '!'
]



🧠 Why range(0, len(parts) - 2, 3)?
You're processing the list in groups of 3:
- parts[i] → sentence
- parts[i+1] → punctuation
- parts[i+2] → space
So:
for i in range(0, len(parts) - 2, 3):


means:
- Start at index 0
- Go up to len(parts) - 2 so you don’t overshoot the list
- Step by 3 to process each sentence group
This lets you safely grab i, i+1, and i+2 without index errors.

🧾 What Does if len(parts) % 3 != 0 Do?
This checks if there’s leftover data at the end of the list that wasn’t part of a complete 3-item group.
In our example:
len(parts) = 9
9 % 3 == 0 → no leftover


But if the list had 10 items (say, an extra word at the end without punctuation), then:
len(parts) % 3 == 1 → leftover exists


So:
if len(parts) % 3 != 0:
    result.append(parts[-1])


adds that final fragment to the result so nothing gets lost.

🧪 Summary
|  |  | 
| range(0, len(parts) - 2, 3) |  | 
| sentence[0].upper() + sentence[1:] |  | 
| result.append(...) |  | 
| if len(parts) % 3 != 0 |  | 

    """

    # Split the paragraph into sentences using puncuatoin followed by space.
    parts = re.split(r'([.?!]+)(\s*)',paragraph)

    result = []
    for i in range(0, len(parts) -2, 3):
        sentence = parts[i]
        punctuation = parts[i + 1]
        space = parts[i + 2]

        if sentence:
            # Capitalize first character of the sentence

            sentence = sentence[0].upper() + sentence[1:]
        result.append(sentence + punctuation + space)

    # Handle any trailing text that wasn't followed by punctuation

    if len(parts) % 3 != 0:
        result.append(parts[-1])

    return ''.join(result)


    



if __name__ == "__main__":
    print(capitalize_user("this is a simple sentence."))
    print(capitalize_user("hello world. how are you?"))

    print(capitalize_user("i did today's coding challenge... it was fun!!"))

    print(capitalize_user("crazy!!!strange???unconventional...sentences."))

    print(capitalize_user("there's a space before this period . why is there a space before that period ?"))