#  Liskov Substitution principle
from single_responsobility_principle import User


#  Принцип подстановки Лисков

class User():
    def __init__(self, color, board):
        create_pieces()
        self.color = color
        self.board = board
    def move(self, piece:Piece, position:int):
        piece.move(position)
        chessmate_check()
    board = ChessBoard()
    user_white = User('white', board)
    user_black = User('black', board)
    pieces = user_white.pieces
    horse = helper.getHorse(user_white, 1)
    user.move(horse)

