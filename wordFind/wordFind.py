import os
import json
for language in os.listdir("languages"):
    print(language)
file = ""    
while not file in os.listdir("languages"):
    file = input("Select Language: ")    
letters = input("Enter Letters: ")
outputList = []
originalLetterList = []
for letter in letters:
    originalLetterList.append(letter)
for word in json.loads(open('Languages/'+file, 'r').read().splitlines()[0]):
    letterList = originalLetterList[:]
    fails = 0
    for letter in word:
        if letter in letterList:
            letterList.remove(letter)
        else:
            fails += 1
    if fails == 0:
        outputList.append(word)
for item in sorted(outputList, key=len):
    if item != letters:
        print(item)

