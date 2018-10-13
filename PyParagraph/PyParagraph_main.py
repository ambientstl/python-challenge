import os
import re

##note: this code works better with paragraph_1.txt than paragraph_2.txt 
# because of paragraph 1's "regular" formatting 
# (paragraph 2 has no spaces after it's periods).
# I am having trouble finding a good explanation of regular expressions.

#set path to txt file
paragraphFile = os.path.join("paragraph_1.txt")

#read txt file
with open(paragraphFile) as paragraphText:
    paragraph = paragraphText.read()

    #split paragraph into a list of words
    wordList = paragraph.split()

    #split paragraph into list of sentences
    sentenceList = re.split("(?<=[.!?]) +", paragraph)
    ##note:the following code "works" for paragraph_2, but not paragraph_1
    #it is an attempt to split the paragraph by any amount of characters (.*) followed by a period (\.)
    #the list seems to be populated by spaces or quote marks
    #sentenceList = re.split(".*\.", paragraph)

    #find words per sentence using the length of the word and sentence lists
    wordsPerSentence = len(wordList) / len(sentenceList)

    #find total # of characters in word list
    ##note: this # only excludes spaces in the paragraph, includes commas, periods, etc
    totalCharacters = 0
    for i in range(len(wordList)):
        totalCharacters += len(wordList[i])

#find approximate letters per word
lettersPerWord = totalCharacters / len(wordList)

#truncate all but 3 decimals in letters per word
lettersPerWord = float('%.2f'%(lettersPerWord))
    
#print analysis
print(f"""Paragraph Analysis
------------------
Approximate Word Count: {len(wordList)}
Approximate Sentence Count: {len(sentenceList)}
Average Letter Count: {lettersPerWord}
Average Sentence Length: {wordsPerSentence}
""")