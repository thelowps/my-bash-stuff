from pieces import Piece

class Board:
    
    def __init__ ( self, width = 8, height = 8 ):
        self.width = width
        self.height = height
        self.pieces = [ [0]*self.height for ix in range(0,self.width) ]
        self.initialize_pieces();

    def initialize_pieces ( self ):

        # How to set up the board. Should be easier to edit than loops...
        # NOTE: the game's structure is [col][row]. This list is [row][col] for editing ease.
        boardSettings = [["ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING", "BISHOP", "KNIGHT", "ROOK"],
                         ["PAWN"]*8,
                         [0]*8, [0]*8, [0]*8, [0]*8,
                         ["PAWN"]*8,
                         ["ROOK", "KNIGHT", "BISHOP", "QUEEN", "KING", "BISHOP", "KNIGHT", "ROOK"]]

        for row in range(0, self.height):
            for col in range(0, self.width):
                if boardSettings[row][col] != 0:
                    piece = Piece(col, row, boardSettings[row][col], "blue", self)
                    self.pieces[col][row] = piece

    def move ( self, col, row, toCol, toRow ):
        piece = self.pieces[col][row]       # The piece to be moved
        if piece != 0:
            self.pieces[col][row] = 0           # Erase the piece's previous position
            self.pieces[toCol][toRow] = piece   # Place the piece at its new location on the board
            piece.move( toCol, toRow )          # update the piece's data

    def capture ( self, piece ):
        self.pieces[piece.col][piece.row] = 0

    def draw ( self ):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if not self.pieces[col][row]:
                    print( "--" ),
                else:
                    self.pieces[col][row].draw()
            print  #print newline


if __name__ == "__main__" :
    board = Board()
    board.draw()
