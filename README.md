Hangman Game




![Beige Illustrated Volunteers Day Flyer  (פוסט של פייסבוק)](https://github.com/maorkris/Hangman/assets/142143890/d60cc5cc-d0f1-4ef9-af0f-f69b7997cfb7)


### Description:

This Python game challenges you to guess a secret word letter by letter. Be careful, you only have 6 tries before the hangman is complete!

Features:

Choose from three word categories: Animals, Names, or Countries.
Colorful text output for a visually engaging experience.
Tracks guessed letters and displays progress towards guessing the word.
Provides feedback on correct and incorrect guesses.
Fun hangman graphics to illustrate the number of remaining tries.
How to Play:

Run the game from the command line using python hangman.py (or the appropriate filename).
Select a word category by entering the corresponding number.
Begin guessing letters one at a time.
Correct guesses will reveal letters in the secret word.
Incorrect guesses will add a body part to the hangman.
Win the game by guessing the word before the hangman is complete.
Dependencies:

Python 3.x
colorama library (install using pip install colorama)
Additional Notes:

The game uses three text files (Animal.txt, countries.txt, and names.txt) to store words for each category. Ensure these files are present in the same directory as the game script.
The game features ASCII art graphics for the hangman, which may not display correctly in all terminal environments.
Enjoy the game!


 Here is a summary of the functions in your hangman game code:

 

The `print_welcome` function prints the opening screen of the game. It sets the maximum number of attempts to 6 and prints the game logo and number of attempts remaining for the player.

The `print_hangman` function prints the hangman image corresponding to the number of attempts the player has tried.

The `guess_a_letter` function asks the player to guess a letter. If the player enters more than one letter or a non-English letter, it prints an error and asks the player to guess again.

The `check_valid_input` function checks if the player's input is valid. It checks for more than one letter, non-English letters, or letters already guessed. If the input is invalid, it returns False.

The `try_update_letter_guessed` function tries to add the letter the player guessed to the list of letters already guessed. If the letter is invalid, it prints an error. If the letter is not in the secret word, it returns True.

The `show_hidden_word` function prints the secret word with underscores instead of letters not yet guessed.

The `check_win` function checks if the player has guessed all the letters in the secret word. If so, it returns True.

The `choose_word` function takes a file path and index, and returns the word at the given index from the file.

The `main` function runs the game. It prints the opening screen, asks the player to choose a category, picks a random word from that category, and runs the game. At the end, it prints the secret word and a message if the player won or lost.
