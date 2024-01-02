import random
import cv2

# List of words for the game
wordArray = ['apple', 'car', 'banana']

# Randomly selecting a word from the wordArray
selectedWord = random.choice(wordArray)

# Creating initial placeholders for the word to be guessed
declareStrWord = ['_' for _ in selectedWord]
liarStrWord = ' '.join(declareStrWord)

print('Guess The Word: ')
print(liarStrWord)
print('\n')

guessWord = ''
guessLetter = ''
storeLetter = []
storeIndex = []
drawFlag = 0
numberOfGuess = 7

# Loop to check the guessed word against the selected word
while (declareStrWord != list(selectedWord)) and (numberOfGuess > 0):

    print(f'You have {numberOfGuess} guesses remaining. Choose a letter: ')
    guessLetter = input().lower()  # Converting input to lowercase for consistency

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

    else:
        for i, letter in enumerate(selectedWord):
            if guessLetter == letter:
                declareStrWord[i] = guessLetter

        storeLetter.append(guessLetter)

        print('Good guess! This letter is in the word.')
        liarStrWord = ' '.join(declareStrWord)
        print(f'Word: {liarStrWord}\n')

# Displaying the result based on game outcomes
if declareStrWord == list(selectedWord):
    print("Congratulations! You've guessed the word correctly.")

if numberOfGuess == 0:
    print(f"Sorry, you couldn't guess the word. It was '{selectedWord}'.")