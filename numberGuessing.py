import random

print("\nWelcome to number guessing game!!!") 

print("\nInput lower bound:") 
lowerBound = int(input())

print("\nInput upper bound:") 
upperBound = int(input()) 
      
print("\nlower bound is:", lowerBound)
print("\nupper bound is:", upperBound)

print("\nSystem will initialize random value between lower and upper bound try to guess it:\n")

systemInitializedNumber = random.randint(lowerBound,upperBound)

GuessedNumber = 0
while systemInitializedNumber != GuessedNumber : 

    GuessedNumber=int(input())
    
    if (systemInitializedNumber==GuessedNumber):
        print("Your guess is correct! Well Done!!!!")
    elif((GuessedNumber<lowerBound) or (GuessedNumber>upperBound)): 
        print("Guess is not in the boundary")
    elif(systemInitializedNumber > GuessedNumber):
        print("Take another guess your gues is smaller than the random number")
    elif(systemInitializedNumber < GuessedNumber):
        print("Take another guess your gues is bigger than the random number")
    
