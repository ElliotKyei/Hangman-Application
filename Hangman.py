# -*- coding: utf-8 -*-
"""
@author: Elliot Kyei
@date: 01/22/2024

Hangman Class
"""

import random

class Hangman:
    
    __newRound = True
    __newWord = True
    __initialRoundScore = 0
    
    def __init__(self, lives, guesses, newRound, score, numWordsCompleted):
        self.__lives = lives
        self.__guesses = guesses
        self.__round = newRound
        self.__score = score
        self.__numWordsCompleted = numWordsCompleted
        self.__wordPool = self.create_wordPool()
        self.__word = self.generate_word()
        self.__maskedWord = self.set_maskedWord(self.__word)
        
        playerGuessFile = open("PlayerGuesses.txt", "w").close()
        
    def get_lives(self):
        return self.__lives
    
    def get_guesses(self):
        return self.__guesses
    
    def get_round(self):
        return self.__round
    
    def get_score(self):
        return self.__score
    
    def get_initialRoundScore(self):
        return self.__initialRoundScore
    
    def get_numWordsCompleted(self):
        return self.__numWordsCompleted
    
    def get_word(self):
        return self.__word
    
    def get_maskedWord(self):
        return self.__maskedWord
    
    def get_newRound(self):
        return self.__newRound
    
    def get_newWord(self):
        return self.__newWord
    
    def create_wordPool(self):
        wordPoolFile = open("WordPool.txt", "r")
        wordPool = wordPoolFile.readlines()
        wordPoolFile.close()
        return wordPool
        
    def get_wordPoolLen(self):
        if self.__wordPool:
            return len(self.__wordPool)
        return -1
        
    def get_wordFromPool(self, ind):
        if self.__wordPool:
            return self.__wordPool[ind]
        return -1
        
    def set_lives(self, lives):
        self.__lives = lives
        
    def set_guesses(self, guesses):
        self.__guesses = guesses 
        
    def set_round(self, newround):
        self.__round = newround
    
    def set_score(self, score):
        self.__score = score
        
    def set_initialRoundScore(self, score):
        self.__initialRoundScore = score
    
    def set_numWordsCompleted(self, num):
        self.__numWordsCompleted = num
    
    def set_word(self, word):
        self.__word = word
    
    def set_maskedWord(self, word):
        if word:
            maskedWord = ["_"] * (len(word)-1)
        return maskedWord
    
    def set_newRound(self, nRound):
        self.__newRound = nRound
        
    def set_newWord(self, nWord):
        self.__newWord = nWord
    
    def generate_word(self):
        
        wordPoolLen = self.get_wordPoolLen()
        
        # Word Pool has been generated
        
        if wordPoolLen > 0:
            
            # Get random index to choose from Word Pool
            ranNum = random.randint(0, wordPoolLen-1)
            newWord = self.get_wordFromPool(ranNum)
            self.set_word(newWord)
            return self.get_word()
        
        return -1
    
    # Reveal the entire masked word
    
    def reveal_maskedWord(self):
        word = self.get_word()
        
        # Iterating through masked word and setting each character to real letter
        
        for ind in len(word)-1:
            self.__maskedWord[ind] = word[ind]
        
    # Reveal letter from masked word
    
    def reveal_maskedLetter(self, ind, letter):
        if self.__maskedWord[ind] == "_":
            self.__maskedWord[ind] = letter
            return 1
        else:
            return 2
    
    # Converting masked word to string for better GUI display
    
    def displayMaskedWord(self):
        maskedWord = self.get_maskedWord()
        count = 0
        for letter in maskedWord:
            if count == len(maskedWord)-1:
                print(letter)
            else:
                print(letter, end="  ")
                
            count += 1
    
    def printMaskedWord(self):
        maskedWord = self.get_maskedWord()
        maskedWordStr = ""
        
        for letter in maskedWord:
            maskedWordStr += (letter + "     ")
            
        return maskedWordStr
    
    # Check if player guess matches a letter in word
    # Return 0 = letter not found
    # Return 1 = letter found
    # return 2 = letter guessed already
    
    def playerGuess(self, guess):
        
        foundLetter = 0 # Return placeholder
        word = self.get_word()
        
        # Iterate through word letter by letter to verify guess
        
        ind = 0
        for letter in word:
            if guess == letter:
                foundLetter = self.reveal_maskedLetter(ind, letter)
                
            ind += 1
        
        # Player letter is not found within word
        
        if foundLetter == 0:
            playerLives = self.get_lives()
            self.set_lives(playerLives-1)
            
            playerScore = self.get_score()
            self.set_score(playerScore-10)
       
        # Player letter is not found within word
        
        if foundLetter == 1:
            
            playerScore = self.get_score()
            self.set_score(playerScore+10)
         
        # Logging player guesses in text file
        
        playerGuessFile = open("PlayerGuesses.txt", "a")
        if self.get_newRound() == True:
            self.set_newRound(False)
            currentRound = self.get_round()
            playerGuessFile.write(f'Round {currentRound} \n')
        if self.get_newWord() == True:
            self.set_newWord(False)
            currentWord = self.get_word()
            playerGuessFile.write(f'\nWord: {currentWord}\nGuesses:\n')

        playerGuessFile.write(f'{guess}\n')
        playerGuessFile.close()
        
        return foundLetter
    
    def checkIfGameWon(self):
        maskedWord = self.get_maskedWord()
        
        for letter in maskedWord:
            if letter == "_":
                return False
    
        return True
    
    def logNumWordCompleted(self):
        numWordsCompleted =  self.get_numWordsCompleted()
        playerGuessFile = open("PlayerGuesses.txt", "a")
        playerGuessFile.write(f'\nNumber of words completed: {numWordsCompleted}\n')
        playerGuessFile.close()
    
    def logGameLost(self):
        playerGuessFile = open("PlayerGuesses.txt", "a")
        playerGuessFile.write('\nPlayer has lost. Progress Restarted\n')
        playerGuessFile.close()
        
    def restartGame(self, currentRound, score, numWordsCompleted):
        self.set_lives(5)
        self.set_guesses(0)
        self.set_round(currentRound)
        self.set_score(score)
        self.set_numWordsCompleted(numWordsCompleted)
        self.__word = self.generate_word()
        self.__maskedWord = self.set_maskedWord(self.__word)
                
    def printRoundDetails(self):
                    print("\n")
                    print("Round: ", self.get_round())
                    print("Words Completed: ", self.get_numWordsCompleted())    
                    print("\n")