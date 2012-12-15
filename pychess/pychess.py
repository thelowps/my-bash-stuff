import sys
import rulebook
from board import Board

board = Board()
rulebook.set_board( board )

while True:
    print
    board.draw()
    inp = raw_input( "Enter move: " )
    inp = inp.split()
    
    """ # Check for four numbers
    if inp.size() != 4:
        print( "Enter four numbers. You entered " ),
        print inp.count()
        continue
        """

    if rulebook.move_is_valid( int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]) ):
        board.move( int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]) )
        
