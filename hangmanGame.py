import random
import cv2
from matplotlib import pyplot as plt

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

# Note that range(6) is corresponds to values 0 to 5 not 0 to 6 or 1 to 6 

declareStrWord = ''
for i in range(len(wordArray[x])): 
    declareStrWord += ' _ '

liarStrWord = ''
for i in range(len(declareStrWord)):
    if(declareStrWord[i]=='_'):
        liarStrWord += '_'

print('\n')
print('Guess The Fruit:')
print('\n')
print(declareStrWord)
print('\n\n')

guessWord = ''
guessLetter = ''
copyWord = ''
storeLetter = []
storeIndex = [] 

#img = cv2.imread("hangmanImages/1head.png")
#cv2.imshow("head",img) 
#cv2.waitKey()

#imgHead = plt.imread("hangmanImages/1head.png")
#plt.imshow(imgHead)


for i in range(len(selectedWord)):
    guessWord+='_'

#for i in range(len(selectedWord)):
#    print(selectedWord[i])
#print('\n')
drawFlag = 0 
numberOfGuess = 7
while (selectedWord != guessWord) and (numberOfGuess>0) :

    
    #copyWord = None
    #copyWord = ''
    print('You have seven guess chance! use them wisely.')
    print('guess letter:')
    guessLetter = input()
    print('\n')

        # Checking if the guessed letter is not in the selected word
    if guessLetter not in selectedWord:
        numberOfGuess -= 1
        print(f'Incorrect! You have {numberOfGuess} guesses left.\n')

        # Displaying hangman images based on the number of guesses left
        img = cv2.imread(f"hangmanImages/{7 - numberOfGuess}.png", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Hangman", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    # Checking if the guessed letter has already been guessed before
    elif guessLetter in storeLetter:
        print("You've already guessed this letter. Try a different one.\n")
    #if(drawFlag==1):
    #    drawFlag = 0

    #    if(numberOfGuess)

    if guessLetter in storeLetter:
        print("You gave this guess before. Please try different letter.")

    else:
        for i in range(len(selectedWord)):
            if(guessLetter==selectedWord[i]):
                storeIndex.append(i)

        if(len(storeIndex)==0):
            print('this letter in not in the word! Try different letter please.')

        #for i in range(len(storeIndex)):
        #    print(storeIndex[i])
        #print('\n')

        if ((len(storeIndex) > 0)):
            print('Good guess this letter is in the word.')
            print(f'This letter appears in this word {len(storeIndex)} times')
            for i in range(len(storeIndex)):
                storeLetter.insert(storeIndex[i],guessLetter)
            
            #for i in range(len(selectedWord)):
            #    if i in storeIndex:
            #        guessWord.insert()
            #    else:
            #        guessWord+= '_'

        #for i in range(len(storeLetter)):
        #    print(storeLetter[i])
        #print('\n')
        #for i in range(len(storeLetter)):
        #    copyWord += storeLetter[i] 

        #to remove letter according to index use array.pop(index)
        #for i in range(len(storeIndex)):
            #declareStrWord.pop(storeIndex[i])
            #declareStrWord.insert(storeIndex[i],guessLetter) 
            #declareStrWord = declareStrWord[:storeIndex[i]] + guessLetter+ declareStrWord[storeIndex[i] + 1:]
         
        for i in range(len(storeIndex)):
            #declareStrWord.pop(storeIndex[i])
            #declareStrWord.insert(storeIndex[i],guessLetter) 
            guessWord = guessWord[:storeIndex[i]] + guessLetter+ guessWord[storeIndex[i] + 1:]
         
        print(guessWord)
        #print(declareStrWord)
        
    #storeLetter.clear()
    storeIndex.clear()
    #print("You found this much of the word:" + copyWord)

'''
    if not(guessLetter in selectedWord):
        numberOfGuess-=1
        print(f'You can have {numberOfGuess} more guess')
        drawFlag = 1 

        if(numberOfGuess==6):
            imgHead = cv2.imread("hangmanImages/1.png", cv2.IMREAD_ANYCOLOR) 
            cv2.imshow("head",imgHead)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            #imgHead = plt.imread("hangmanImages/1head.png")
            #plt.imshow(imgHead)

        elif(numberOfGuess==5):
            imgBody = cv2.imread("hangmanImages/2.png", cv2.IMREAD_ANYCOLOR)
            cv2.imshow("body",imgBody)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            
        elif(numberOfGuess==4):
            imgArmLeg = cv2.imread("hangmanImages/3.png", cv2.IMREAD_ANYCOLOR)
            cv2.imshow("arm and leg",imgArmLeg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
        elif(numberOfGuess==3):
            imgRope = cv2.imread("hangmanImages/4.png", cv2.IMREAD_ANYCOLOR)
            cv2.imshow("rope",imgRope)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)

        elif(numberOfGuess==2):
            imgceil = cv2.imread("hangmanImages/5.png", cv2.IMREAD_ANYCOLOR)
            cv2.imshow("ceil",imgceil)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
        elif(numberOfGuess==1):
            imgColumn = cv2.imread("hangmanImages/6.png", cv2.IMREAD_ANYCOLOR)
            cv2.imshow("column",imgColumn)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
        elif(numberOfGuess==0):
            imgBase = cv2.imread("hangmanImages/7.png", cv2.IMREAD_ANYCOLOR)
            cv2.imshow("base",imgBase)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            print("YOU DIED")
'''

    
if (guessWord==selectedWord):
    print("!!!!Well done your guess is correct!!!!")

if (numberOfGuess==0):
    print("You couldn't find the word it was:" + selectedWord)