""" This module determines the rules of the game.

It defines the valid moves for each piece. Call is_valid( piece, (col,row) ) to check if it is valid for
the given piece to move to the given location.

"""

def pawn_move ( pawn ):
    return []

def rook_move ( rook ):
    return []

def bishop_move ( bishop ):
    return []

def knight_move ( knight ):
    return []

def queen_move ( queen ):
    return []

def king_move ( king ):
    return []

# Key unit types to movement pattern functions
MOVEMENTS = {} 
MOVEMENTS["PAWN"]   = pawn_move
MOVEMENTS["ROOK"]   = rook_move
MOVEMENTS["BISHOP"] = bishop_move
MOVEMENTS["KNIGHT"] = knight_move
MOVEMENTS["QUEEN"]  = queen_move
MOVEMENTS["KING"]   = king_move

BOARD = 0

def set_board ( b ):
    """ Set the board reference. """
    BOARD = b

def move_is_valid ( col, row, toCol, toRow ):
    """ Check if the piece at [col][row] can legally move to [toCol][toRow] """

    # bounds check #
    if col < 0 or row < 0 or toCol < 0 or toRow < 0:
        return False
    if col >= BOARD.width or row >= BOARD.height or toCol >= BOARD.width or toRow >= BOARD.height:
        return False

    piece = BOARD.pieces[col][row]
    
    #call the corresponding piece's movement function, check list to see if it contains the spot.
    #more efficient way?

    return True

if __name__ == "__main__":
    initialize( 1 )
