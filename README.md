# Overview

In this game, a player has 5 chances to correctly guess letters and reveal the hidden word. The 
GUI interface has an input box that will allow a player to enter a letter to make a guess. The 
game will keep track of the number of words completed, what round the player has reached, 
and their score. 

Random words are selected from a text file containing a pool of words over 6 characters and 
each game the user makes will be logged detailing the current round and the word being 
solved. By clicking the “reveal word” button, a hint will be given at the top

![Final Project SS1](https://github.com/ElliotKyei/Hangman-Application/assets/73500548/24433c2f-4879-4457-b722-53bb486b8ef4)

# Losing The Game

A player only has 5 lives. A wrong guess will display a different hangman region
(5) and deduct 20 points from their score. The player loses the game if all 5 hangman parts are shown. The player can play again by
entering any key. However, the player’s score resets to 0 and must start over from Round 1. 

![Final Project SS3](https://github.com/ElliotKyei/Hangman-Application/assets/73500548/1562c0c0-fba8-471f-9316-8277cd105f90)

# Winning The Game

Each correct guess of a letter in the hidden word earns the player 20 points. If the player is able
to correctly guess all the letters in the word without losing their 5 lives, they win. Each round
consists of 5 words, and the player can keep playing to earn more points and see how many
words they can complete.
The game will also notify the player of repeated guesses and will not deduct any points

After the player successfully guesses all letters correctly, they may enter ‘y’ to play again for a
better score (revoking the completed word), or enter ‘n’ to keep their score. Both options will
generate a new word for the player to solve

![Final Project SS7](https://github.com/ElliotKyei/Hangman-Application/assets/73500548/b4e540d8-9459-4033-a355-a017bfbba35a)
