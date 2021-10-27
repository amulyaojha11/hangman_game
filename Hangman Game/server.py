import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#To start the server
serversocket.bind(('localhost', 8089))
serversocket.listen(1)  #Become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()#To connect to the client
    buf = connection.recv(64)#To accept the message from the client-side
    # print(str(buf, "utf-8"))
    word = str(buf, "utf-8")
    word, hint = word.split(',')#To extract the word and the hint from message received
    break

word = word.lower()
# print(word,hint)

#ASCII ART FOR EVERY GUESS
HANGMANPICS = [''' 
+-----+
|     |
|
|
|
|
======= ''', '''
+-----+
|     |
|     0
|
|
|
======= ''', '''
+-----+
|     |
|     0
|     |
|
|
======= ''', '''
+-----+
|     |
|     0
|    /|
|
|
======= ''', '''
+-----+
|     |
|     0
|    /|\ 
|
|
======= ''', '''
+-----+
|     |
|     0
|    /|\ 
|    / 
|
======= ''', '''
+-----+
|     |
|     0
|    /|\ 
|    / \ 
|
======= ''']

#To display the current status of the game
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    #To display the ASCII art and Hint
    print(HANGMANPICS[len(missedLetters)])
    print('Hint : ', end=" ")
    print(hint)
    print()

    #To display the missed letters
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)

    # Replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    # Show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()

#To check the validity of the guess
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


#GAME START POINT
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = word
gameIsDone = False

while True:
    #Calling displayBoard function
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    #Calling guess function
    guess = getGuess(missedLetters + correctLetters)

    #To check the guess
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            #On winning
            gameIsDone = True
            break
    #If the guess is Incorrect
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            #On Losing
            gameIsDone = True
            break