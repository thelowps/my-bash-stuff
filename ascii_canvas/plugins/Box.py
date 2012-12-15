class Box :
    """
    Draws a box at the specified top left and bottom right coordinates.
    """
    
    def __init__ ( self ):
        pass

    def drawBox ( self, topLeft, botRight, fill ):
        cols = []
        rows = []
        if not fill:
            width = botRight[0] - topLeft[0] + 1
            height = botRight[1] - topLeft[1] + 1
            cols += range( topLeft[0], botRight[0]+1 ) * 2 + [topLeft[0]]*width + [botRight[0]]*height
            rows += [topLeft[1]]*width + [botRight[1]]*height + range( topLeft[1], botRight[1]+1 ) * 2
        
        else:
            for j in range( topLeft[1], botRight[1]+1 ):
                for i in range( topLeft[0], botRight[0]+1 ):
                    rows.append( j )
                    cols.append( i )
                
        return cols, rows
                
