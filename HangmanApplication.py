# -*- coding: utf-8 -*-
# @author: Elliot Kyei
# @date: 01/22/2024

# Main Application
# Used Qt Designer to create most QWidgets
# Used PyQt5 UI code generator 5.15.7 to convert GUI to py
# 


import Hangman
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    # Initial values for hangman game
    
    __lives = 5
    __guesses = 0
    __currentRound = 1
    __score = 0
    __numWordsCompleted = 0
    __gameLost = False
    __newWord = False
        
    __HangmanGame = Hangman.Hangman(__lives, __guesses, __currentRound, __score, __numWordsCompleted)
        
    def setupUi(self, MainWindow):

        # Creating QTWidget objects
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(976, 756)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setWindowTitle("Elliot Kyei's Hangman")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Labels and Input
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 390, 71, 41))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        
        self.hangmanWord = QtWidgets.QLabel(self.centralwidget)
        self.hangmanWord.setGeometry(QtCore.QRect(390, 270, 1031, 41))
        self.hangmanWord.setObjectName("hangmanWord")
        
        self.welcomeMessage = QtWidgets.QLabel(self.centralwidget)
        self.welcomeMessage.setGeometry(QtCore.QRect(270, 30, 401, 41))
        self.welcomeMessage.setScaledContents(False)
        self.welcomeMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeMessage.setObjectName("welcomeMessage")
        
        self.RoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.RoundLabel.setGeometry(QtCore.QRect(290, 70, 401, 41))
        self.RoundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RoundLabel.setObjectName("RoundLabel")
        
        # Hangman Graphic
        self.hangmanPole2 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanPole2.setGeometry(QtCore.QRect(40, 130, 101, 16))
        self.hangmanPole2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanPole2.setLineWidth(4)
        self.hangmanPole2.setMidLineWidth(5)
        self.hangmanPole2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hangmanPole2.setObjectName("hangmanPole2")
        self.hangmanPole1 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanPole1.setGeometry(QtCore.QRect(30, 140, 20, 331))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanPole1.setFont(font)
        self.hangmanPole1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanPole1.setLineWidth(4)
        self.hangmanPole1.setMidLineWidth(5)
        self.hangmanPole1.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanPole1.setObjectName("hangmanPole1")
        self.hangmanPole3 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanPole3.setGeometry(QtCore.QRect(130, 140, 20, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanPole3.setFont(font)
        self.hangmanPole3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanPole3.setLineWidth(4)
        self.hangmanPole3.setMidLineWidth(5)
        self.hangmanPole3.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanPole3.setObjectName("hangmanPole3")
        self.hangmanHead = QtWidgets.QLabel(self.centralwidget)
        self.hangmanHead.setGeometry(QtCore.QRect(120, 180, 51, 100))
        self.hangmanHead.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hangmanHead.setFont(font)
        self.hangmanHead.setLineWidth(1)
        self.hangmanHead.setScaledContents(False)
        self.hangmanHead.setObjectName("hangmanHead")
        self.hangmanNeck = QtWidgets.QFrame(self.centralwidget)
        self.hangmanNeck.setGeometry(QtCore.QRect(129, 260, 31, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanNeck.setFont(font)
        self.hangmanNeck.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanNeck.setLineWidth(6)
        self.hangmanNeck.setMidLineWidth(6)
        self.hangmanNeck.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanNeck.setObjectName("hangmanNeck")
        self.hangmanLArm1 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanLArm1.setGeometry(QtCore.QRect(110, 250, 41, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanLArm1.setFont(font)
        self.hangmanLArm1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanLArm1.setLineWidth(6)
        self.hangmanLArm1.setMidLineWidth(6)
        self.hangmanLArm1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hangmanLArm1.setObjectName("hangmanLArm1")
        self.hangmanRArm1 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanRArm1.setGeometry(QtCore.QRect(140, 250, 41, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanRArm1.setFont(font)
        self.hangmanRArm1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanRArm1.setLineWidth(6)
        self.hangmanRArm1.setMidLineWidth(6)
        self.hangmanRArm1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hangmanRArm1.setObjectName("hangmanRArm1")
        self.hangmanLLeg = QtWidgets.QFrame(self.centralwidget)
        self.hangmanLLeg.setGeometry(QtCore.QRect(120, 360, 31, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanLLeg.setFont(font)
        self.hangmanLLeg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanLLeg.setLineWidth(6)
        self.hangmanLLeg.setMidLineWidth(6)
        self.hangmanLLeg.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanLLeg.setObjectName("hangmanLLeg")
        self.hangmanRLeg = QtWidgets.QFrame(self.centralwidget)
        self.hangmanRLeg.setGeometry(QtCore.QRect(140, 360, 31, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanRLeg.setFont(font)
        self.hangmanRLeg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanRLeg.setLineWidth(6)
        self.hangmanRLeg.setMidLineWidth(6)
        self.hangmanRLeg.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanRLeg.setObjectName("hangmanRLeg")
        self.hangmanLArm2 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanLArm2.setGeometry(QtCore.QRect(100, 280, 31, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanLArm2.setFont(font)
        self.hangmanLArm2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanLArm2.setLineWidth(6)
        self.hangmanLArm2.setMidLineWidth(6)
        self.hangmanLArm2.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanLArm2.setObjectName("hangmanLArm2")
        self.hangmanRArm2 = QtWidgets.QFrame(self.centralwidget)
        self.hangmanRArm2.setGeometry(QtCore.QRect(160, 280, 31, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hangmanRArm2.setFont(font)
        self.hangmanRArm2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hangmanRArm2.setLineWidth(6)
        self.hangmanRArm2.setMidLineWidth(6)
        self.hangmanRArm2.setFrameShape(QtWidgets.QFrame.VLine)
        self.hangmanRArm2.setObjectName("hangmanRArm2")
        
        # More Labels
        
        self.GuessLabel = QtWidgets.QLabel(self.centralwidget)
        self.GuessLabel.setGeometry(QtCore.QRect(400, 390, 200, 41))
        self.GuessLabel.setObjectName("GuessLabel")
        
        self.MessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.MessageLabel.setGeometry(QtCore.QRect(410, 490, 335, 81))
        self.MessageLabel.setObjectName("MessageLabel")
        
        self.MessageLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.MessageLabel2.setGeometry(QtCore.QRect(410, 550, 275, 41))
        self.MessageLabel2.setObjectName("MessageLabel2")
        
        self.DisplayWordButton = QtWidgets.QPushButton('Reveal Word', self.centralwidget)
        self.DisplayWordButton.setGeometry(QtCore.QRect(375, 650, 275, 41))
        self.DisplayWordButton.setObjectName("DisplayWordButton")
        self.DisplayWordButton.clicked.connect(self.onClicked)
        
        self.ScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScoreLabel.setGeometry(QtCore.QRect(290, 100, 401, 41))
        self.ScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.WordsCompletedLabel = QtWidgets.QLabel(self.centralwidget)
        self.WordsCompletedLabel.setGeometry(QtCore.QRect(20, 30, 200, 41))
        self.WordsCompletedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WordsCompletedLabel.setObjectName("WordsCompletedLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.startHangmanGame(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       

    def startHangmanGame(self, MainWindow):
        
        # get new hangman game
        
        self.newHangman()
        
        # Binding "enter" to user input
        
        self.lineEdit.returnPressed.connect(self.onEntered)
        
    def onEntered(self):
        
            
        _translate = QtCore.QCoreApplication.translate
        letterGuess = self.lineEdit.text().lower()
        
        # Logic to restart game if player loses
        
        if self.__gameLost == True:
            self.__HangmanGame.logGameLost()
            self.__HangmanGame.restartGame(1, 0, 0)
            self.__gameLost = False
            self.newHangman()
        
        # Logic to generate a new word if player wins
        
        # Player wishes to retry to get a better score
        elif self.__newWord == True and letterGuess == "y":
                    currentRound = self.__HangmanGame.get_round()
                    numWordsCompleted = self.__HangmanGame.get_numWordsCompleted()
                    initialRoundScore = self.__HangmanGame.get_initialRoundScore()
                    self.__HangmanGame.restartGame(currentRound, initialRoundScore, numWordsCompleted)
                    self.__newWord = False
                    self.newHangman()
                    
        # Player does not wish to get a better score
        
        elif self.__newWord == True and letterGuess == "n":
                currentRound = self.__HangmanGame.get_round()
                numWordsCompleted = self.__HangmanGame.get_numWordsCompleted() + 1
                self.__HangmanGame.set_numWordsCompleted(numWordsCompleted)
                currentScore = self.__HangmanGame.get_score()
                
                if self.__HangmanGame.get_numWordsCompleted() % 5 == 0:
                    currentRound += 1
                    self.__HangmanGame.set_newRound(True)
                
                self.__HangmanGame.logNumWordCompleted()
                self.__HangmanGame.restartGame(currentRound, currentScore, numWordsCompleted)
                self.__newWord = False    
                self.newHangman()
                
        # If player hasn't lost or won, check if input matches word
        
        elif self.__gameLost == False and self.__newWord == False:
            
            if letterGuess.isdigit():
                self.MessageLabel.setText(_translate("MainWindow", "Please enter a valid letter"))
            else:
                
                # Check letter through Hangman class
                
                guessResult = self.__HangmanGame.playerGuess(letterGuess.lower())
                
                # Word does not contain letter
                
                if guessResult == 0:
                    self.MessageLabel.setText(_translate("MainWindow", f'Oops, the letter "{letterGuess}" is not in this word'))
                    currentScore = self.__HangmanGame.get_score() - 10
                    self.__HangmanGame.set_score(currentScore)
                    totalScore = self.__HangmanGame.get_score()
                    self.ScoreLabel.setText(_translate("MainWindow", f'Score: {totalScore}'))
                    
                    # Sequentially set hangman parts visible
                    
                    if self.hangmanHead.isVisible() == False:
                        self.hangmanHead.show()
                        self.hangmanHead.setText(_translate("MainWindow", "O"))
                        self.hangmanNeck.show()
                    elif self.hangmanLArm1.isVisible() == False:
                        self.hangmanLArm1.show()
                        self.hangmanLArm2.show()
                    elif self.hangmanRArm1.isVisible() == False:
                        self.hangmanRArm1.show()
                        self.hangmanRArm2.show()
                    elif self.hangmanLLeg.isVisible() == False:
                        self.hangmanLLeg.show()
                        
                    # If the right leg is revealed, player has lost the game
                    
                    elif self.hangmanRLeg.isVisible() == False:
                        self.hangmanRLeg.show()
                        self.MessageLabel.setText(_translate("MainWindow", 'You have Lost. Enter any key to play again'))
                        self.__gameLost = True
                 
                # Word contains letter
                
                elif guessResult == 1:
                    self.MessageLabel.setText(_translate("MainWindow", "Correct Guess!"))
                    currentScore = self.__HangmanGame.get_score() + 10
                    self.__HangmanGame.set_score(currentScore)
                    totalScore = self.__HangmanGame.get_score()
                    self.ScoreLabel.setText(_translate("MainWindow", f'Score: {totalScore}'))
                
                # Player guess in already revealed
                
                elif guessResult == 2:
                    self.MessageLabel.setText(_translate("MainWindow", f'You have already guessed the letter {letterGuess}'))
            
            self.lineEdit.setText("")
            
            # Updating masked word every input
            
            maskedWord = self.__HangmanGame.printMaskedWord()
            self.hangmanWord.setText(_translate("MainWindow", f'{maskedWord}'))  
            
            # Check if player has won game
            
            if self.__HangmanGame.checkIfGameWon():
                self.MessageLabel.setText(_translate("MainWindow", 'Nice work! You have solved the word'))
                self.MessageLabel2.setText(_translate("MainWindow", 'Try again for a better score? (y or n)'))   
                self.__newWord = True
    
    def onClicked(self):
        
        # Reveal Word in "Round Label"
        
        _translate = QtCore.QCoreApplication.translate
        
        currentRound = self.__HangmanGame.get_round()
        selectedWord = self.__HangmanGame.get_word()
        self.RoundLabel.setText(_translate("MainWindow", f'Round: {currentRound} - {selectedWord}'))
        self.lineEdit.setFocus()
        
    def newHangman(self):
        
        initialRoundScore = self.__HangmanGame.get_score()
        self.__HangmanGame.set_initialRoundScore(initialRoundScore)
        self.__HangmanGame.set_newWord(True)
        _translate = QtCore.QCoreApplication.translate
        
        # Hide hangman and all game messages 
        
        self.lineEdit.setText("")
        self.hangmanHead.hide()
        self.hangmanHead.setText(_translate("MainWindow", ""))
        self.hangmanNeck.hide()
        
        self.hangmanLArm1.hide()
        self.hangmanLArm2.hide()
        
        self.hangmanRArm1.hide()
        self.hangmanRArm2.hide()
        
        self.hangmanLLeg.hide()
        self.hangmanRLeg.hide()
        
        
        self.MessageLabel.setText(_translate("MainWindow", ''))
        self.MessageLabel2.setText(_translate("MainWindow", ''))
        
        self.welcomeMessage.setText(_translate("MainWindow", "Welcome to Elliot Kyei's Hangman Game"))
        self.GuessLabel.setText(_translate("MainWindow", "Guess a letter:"))
        # Getting game data from Hangman class and setting them to QWidgets
        
        currentRound = self.__HangmanGame.get_round()
        self.RoundLabel.setText(_translate("MainWindow", f'Round: {currentRound}'))
        numWordsCompleted = self.__HangmanGame.get_numWordsCompleted()
        self.WordsCompletedLabel.setText(_translate("MainWindow", f'Word Completed: {numWordsCompleted}'))
        totalScore = self.__HangmanGame.get_score()
        self.ScoreLabel.setText(_translate("MainWindow", f'Score: {totalScore}'))
        maskedWord = self.__HangmanGame.printMaskedWord()
        self.hangmanWord.setText(_translate("MainWindow", f'{maskedWord}'))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
