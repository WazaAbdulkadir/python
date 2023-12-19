import random

#CURRENT SITUATION 
    #Giving same true letter more than one cause issue 
    #Underscores with spaces need to be displayed instead of letters 

wordArray = ['apple','car','banana']
#print(wordArray[2])

x = random.randint(0,len(wordArray)-1)
#print(x)
#print(wordArray[x])
#print(len(wordArray[x]))
selectedWord = wordArray[x] 

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5

declareStrWord = ''
for i in range(len(wordArray[x])): 
    declareStrWord += ' _ '

liarStrWord = ''
for i in range(len(declareStrWord)):
    if(declareStrWord[i]=='_'):
        liarStrWord += '_'

print('\n')
print('Guess The Word:')
print('\n')
print(declareStrWord)
print('\n\n')

guessWord = ''
guessLetter = ''
copyWord = ''
storeLetter = []
storeIndex = [] 

#for i in range(len(selectedWord)):
#    print(selectedWord[i])
#print('\n')

while selectedWord != copyWord:

    copyWord = None
    copyWord = ''
    print('guess letter:')
    guessLetter = input()
    print('\n')

    for i in range(len(selectedWord)):
        if(guessLetter==selectedWord[i]):
            storeIndex.append(i)

    if(len(storeIndex)==0):
        print('this letter in not in the word! Try different letter please.')

    #for i in range(len(storeIndex)):
    #    print(storeIndex[i])
    #print('\n')

    if (len(storeIndex) > 0):
        print('Good guess this letter is in the word.')
        print(f'This letter appears in this word {len(storeIndex)} times')
        for i in range(len(storeIndex)):
            storeLetter.insert(storeIndex[i],guessLetter)

    #for i in range(len(storeLetter)):
    #    print(storeLetter[i])
    #print('\n')
    for i in range(len(storeLetter)):
        copyWord += storeLetter[i] 

    #to remove letter according to index use array.pop(index)
    for i in range(len(storeIndex)):
        #declareStrWord.pop(storeIndex[i])
        #declareStrWord.insert(storeIndex[i],guessLetter) 
        declareStrWord = declareStrWord[:storeIndex[i]] + guessLetter+ declareStrWord[storeIndex[i] + 1:]
    
    
    #print(declareStrWord)
    
    #storeLetter.clear()
    storeIndex.clear()
    print(copyWord)

    
if (copyWord==selectedWord):
    print("!!!!Well done your guess is correct!!!!")