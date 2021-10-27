## Hangman Game
The goal is to start with a word, represent that word as a series of blank spaces that hide the letters, and allow the player to guess one letter at a time while returning feedback on their guess and an updated representation of their progress in guessing the word.

### Goals
In this case, we were also asked to add an ASCII representation of the man “being hanged.” So the first goal was to develop an ASCII array (to form the ‘hang’ and the ‘man’) that would only require minimally modifications based on the number of guesses. 

### Notebook Sketching:
![image](https://user-images.githubusercontent.com/72320197/139126334-4ee56621-d433-4b7d-9318-44f400631820.png)

### What does the code do?

The program prompts the user with the current ASCII based on the current number of incorrect guesses, along with a line of “blank spaces” (one for each letter in the word). As the user enters a guess (single letter), the program checks whether or not the guess is correct — whether it is in the word.
While coding this, I got concerned about the number of objects I was creating just for the word-related aspects. I ended up with one list to store the version of the current guess progress for printing, one list for the current progress without special formatting, and then also a string for the current guess progress for comparing directly to the word.
