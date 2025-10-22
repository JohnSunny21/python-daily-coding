"""
Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."
"""

import unittest

class SpeakWiselyTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(wise_speak("You must speak wisely."),"Speak wisely, you must.")
      
    def test2(self):
        self.assertEqual(wise_speak("You can do it!"),"Do it, you can!") 

    def test3(self):
        self.assertEqual(wise_speak("Do you think you will complete this?"),"Complete this, do you think you will?")

    def test4(self):
        self.assertEqual(wise_speak("All your base are belong to us."),"Belong to us, all your base are.")
    
    def test5(self):
        self.assertEqual(wise_speak("You have much to learn."), "Much to learn, you have.")







def wise_speak(sentence):

    words = sentence.split(" ")
    last_punctuation = sentence[-1]
    end_string = [] 
    first_string = []

    for i in range(len(words)):
        if words[i] in ["have","must","are","will","can"]:
            end_string = words[:i+1] # You must
            
            first_string = words[i+1:]  # speak wisely.

    end_string[0] = ", " + end_string[0].lower()
    first_string[0] = first_string[0].capitalize()
    first_string[-1] = first_string[-1].strip(last_punctuation)


    return ' '.join(first_string) + ' '.join(end_string) + last_punctuation


"""
Need to improve the above code for the edge cases and improvements.
1. No trigger word found
==> If no trigger word is present, the loop won't assing anything to end_string or first_string, and the code will crash or misbehave.
we need add the guard clause:

if not end_string:
    return sentence;


2. Trigger word is the last word
Example: "They can."
==> end_string = ['They', 'can']
==> first_string = []
==> when trying to access the first_string[0] ==> Index Error


Fix: Add a check before modifying first_string[0]:

if first_string:
    first_string[0] = first_string[0].capitalize()
    first_string[-1] = first_string[-1].strip(last_puntuation)


3. Trigger word is the first word
Example: "Must you listen."
end_string = ["Must"]
first_string = ['you','listen']

==> Works fine, but make sure punctuation is stripped from the last word correctly.


4. Multiple trigger words
-> This code finds the last trigger word, not the first.
Example : "You must have courage."
Expected: "Have courage, you must"
Your code: "Courage, you must have"


Fix: Break the loop after the first match:

for i in range(len(words)):
    if words[i] in ["have","must","are","will","can"]:
        end_string = words[:i+1]
        first_string = words[i+1:]
        break
        
5. Punctuation inside sentence
The previous code assumes that last character is punctuation, which is fine per the spec. But if someone passes "You must, speak wisely.", It will misbehave.
Optional enhancement : for this problem can be
Validate that sentence[-1] is in ".!?" before treating it as punctuation.

"""

def wise_speak_optimized(sentence):
    trigger_words = {"have","must","are","will","can"}
    punctuation = sentence[-1]
    

    words = sentence.split(' ')
    end_string = []
    first_string = []

    for i in range(len(words)):
        if words[i].lower() in trigger_words:
            end_string = words[:i+1]
            first_string = words[i+1:]
            break

    if not end_string:
        return sentence
    
    end_string[0] = ", " + end_string[0].lower()

    if first_string:
        first_string[0] = first_string[0].capitalize()
        first_string[-1] = first_string[-1].strip(punctuation)

    return ' '.join(first_string) + ' '.join(end_string) + punctuation


def wise_speak_refined(sentence):

    trigger_words = {"have","must","are","will","can"}

    # Separate punctuation
    punctuation = sentence[-1]
    sentence = sentence[:-1]

    words = sentence.split(" ")

    # Find the first trigger word
    for i, word in enumerate(words):
        if word.lower() in trigger_words:
            split_index = i
            break
    else:
        return sentence + punctuation # means no trigger found.
    

    # Rearrange parts

    front = words[:split_index+1]
    back = words[split_index+1:]


    # Build new sentence


    new_sentence = ' '.join(back)
    if new_sentence:
        new_sentence = new_sentence[0].upper() + new_sentence[1:]
    else:
        new_sentence = ''
    
    tail = ', ' + ' '.join(front).lower()

    return new_sentence + tail + punctuation





if __name__ == "__main__":

    # print(wise_speak("You must speak wisely."))
    # print(wise_speak("You can do it!"))
    # print(wise_speak("You must have courage."))
    print(wise_speak("You must speak wisely."))

    unittest.main()

    