import random

wordArray = ['apple','car','banana']
#print(wordArray[2])

x = random.randint(0,len(wordArray)-1)
print(x)
print(wordArray[x])
print(len(wordArray[x]))
selectedWord = wordArray[x] 

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5

declareStrWord = ''
for i in range(len(wordArray[x])): # will count up to 3 but not three 
    declareStrWord += ' _ '

print('guess the word:')
print(declareStrWord)
print('\n')

guessWord = ''
guessLetter = ''
copyWord = ''
storeLetter = []
storeIndex = [] 


for i in range(len(selectedWord)):
    print(selectedWord[i])
print('\n')

while selectedWord != copyWord:

    print('guess letter:')
    guessLetter = input()

    for i in range(len(selectedWord)):
        if(guessLetter==selectedWord[i]):
            storeIndex.append(i)
        else:
            print("This letter is not it the word! Guess another letter \n")

    for i in range(len(storeIndex)):
        print(storeIndex[i])
    print('\n')

    if (len(storeIndex) > 0):
        for i in range(len(storeIndex)):
            storeLetter.index(i,guessLetter)
         
    for i in range(len(storeLetter)):
        print(storeLetter[i])
    print('\n')

    #to remove letter according to index use array.pop(index)
    storeLetter.clear()
    storeIndex.clear()
    print(copyWord)

    
    