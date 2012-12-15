class Piece:
    def __init__ ( self, col, row, type, color, board ):
        self.col = col
        self.row = row
        self.color = color
        self.board = board
        self.type = type;
        
    def move ( self, col, row ):   
        self.col = col
        self.row = row

    def draw ( self ):
        print( self.color[0] + self.type[0] ),


"""
class Pawn ( Piece ) :    
    def __init__ ( self, col, row, player, board, dir ):
        Piece.__init__ ( self, col, row, player, board )
        self.dir = dir;
        self.hasMoved = False;

    def draw ( self ):
        print( "P" ),

    # We override the move function to set the hasMoved flag
    def move ( self, col, row ):
        Piece.move( self, col, row ) #superclass function call
        self.hasMoved = True;

    def get_possibles ( self ):
        moves = [(self.col, self.row+dir)]
        if not hasMoved:
            moves += (self.col, self.row+2*dir)


class Rook ( Piece ):
    def __init__ ( self, col, row, player, board ):
        Piece.__init__ ( self, col, row, player, board )

    def draw ( self ):
        print( "R" ),

class Bishop ( Piece ):
    def __init__ ( self, col, row, player, board ):
        Piece.__init__ ( self, col, row, player, board )

    def draw ( self ):
        print( "B" ),

class Knight ( Piece ):
    def __init__ ( self, col, row, player, board ):
        Piece.__init__ ( self, col, row, player, board )

    def draw ( self ):
        print( "K" ),

class Queen ( Piece ):
    def __init__ ( self, col, row, player, board ):
        Piece.__init__ ( self, col, row, player, board )

    def draw ( self ):
        print( "Q" ),

class King ( Piece ):
    def __init__ ( self, col, row, player, board ):
        Piece.__init__ ( self, col, row, player, board )

    def draw ( self ):
        print( "B" ),
"""


if __name__ == "__main__":
    p = Pawn (1,1,1,1)
