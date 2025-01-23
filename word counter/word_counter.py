WordToCount = input("enter a sentence and i will tell you how manny words are in the sentence: ")
SentenceInList = []
SentenceWithoutSpaces = []
SentenceInList.append(WordToCount)
for sliced_sentence in SentenceInList:
    SentenceWithoutSpaces.extend(sliced_sentence.split())
if len(SentenceWithoutSpaces) <= 1:
    print("this isn't a sentence")
if len(SentenceWithoutSpaces) >= 2:
    
    print(f'your sentence has {len(SentenceWithoutSpaces)} words')