# Tic Tac Toe
import random
import time

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Player2'
    else:
        return 'Player1'

def inputPlayer1Letter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the other player's letter as the second.
    name= whoGoesFirst()
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Does '+ name + ' want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player1's letter, the second is the player2's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')






class Board:
    def __init__(self, size):
        self.board = [' '] * size

        def __repr__(self):
            return ("<" + self.__class__.__name__ +
            " [' '] * size =" + str(self.board) +     
            ">")



    def drawBoard(self):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')


    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
        (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal
     
    def getBoardCopy(self):
    # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
    # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '


    def getPlayer1Move(self, Player2Letter):
    # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print("What is Player1's next move? (1-9)")
            move = input()
        return int(move)



    def getPlayer2Move(self, Player1Letter):
    # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print("What is Player2's next move? (1-9)")
            move = input()
        return int(move)


    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True
    







print('Welcome to Tic Tac Toe!')
print('This is a two player game. The computer will randomly choose \nwhich player gets to pick X or O and which player will go \nfirst.')
print()
time.sleep(1)


while True:
    # Reset the board
    
    theBoard = Board(10)
    Player1Letter, Player2Letter = inputPlayer1Letter()
    name = whoGoesFirst()
    print(name + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if name == 'Player1':
            # Player1's turn.
            theBoard.drawBoard()
            move = theBoard.getPlayer1Move(Player2Letter)
            theBoard.makeMove(Player1Letter, move)

            if theBoard.isWinner(Player1Letter):
                theBoard.drawBoard()
                print('Hooray! Player1 has won the game!')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    name = 'Player2'

        else:
            # Player2's turn.
            theBoard.drawBoard()
            move = theBoard.getPlayer2Move(Player1Letter)
            theBoard.makeMove(Player2Letter, move)

            if theBoard.isWinner(Player2Letter):
                theBoard.drawBoard()
                print('Hooray! Player2 has won the game!')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    name = 'Player1'

    if not playAgain():
        break
    
    
