## Hangman Game
The goal is to start with a word, represent that word as a series of blank spaces that hide the letters, and allow the player to guess one letter at a time while returning feedback on their guess and an updated representation of their progress in guessing the word.

### Goals
In this case, we were also asked to add an ASCII representation of the man “being hanged.” So the first goal was to develop an ASCII array (to form the ‘hang’ and the ‘man’) that would only require minimally modifications based on the number of guesses. 

### Notebook Sketching
![image](https://user-images.githubusercontent.com/72320197/139126334-4ee56621-d433-4b7d-9318-44f400631820.png)

### What does the code do?

It takes the word and the hint from the client side.
And the server side has to guess the word by the help of the hint.
The program prompts the user with the current ASCII based on the current number of incorrect guesses, along with a line of “blank spaces” (one for each letter in the word). As the user enters a guess (single letter), the program checks whether or not the guess is correct — whether it is in the word.
While coding this, I got concerned about the number of objects I was creating just for the word-related aspects. I ended up with one list to store the version of the current guess progress for printing, one list for the current progress without special formatting, and then also a string for the current guess progress for comparing directly to the word.

### Steps
* If the guess is correct then the letters wherever required is added.
* If not, the letters are added to missing letters.
* Whenever you run out of the guesses you lose the game.

### Module Implementation

#### Client Side
![image](https://user-images.githubusercontent.com/72320197/139127360-ce4910d9-3163-4352-82b7-144be6253772.png)

#### Server Side
![image](https://user-images.githubusercontent.com/72320197/139127416-ff50375a-1690-44e1-9da2-76605f3d027c.png)
![image](https://user-images.githubusercontent.com/72320197/139127435-696162aa-1bd0-4a95-bfa1-fc7ed226ce66.png)


![image](https://user-images.githubusercontent.com/72320197/139127515-8d677efb-dbc6-4534-a735-76acae9d62c3.png)
![image](https://user-images.githubusercontent.com/72320197/139127595-44818992-3e7a-4dfc-a3b9-1acc8fb1ed34.png)

Contributors
- Raghav Khatoria
- Siddharth Sawhney 
- Amulya
