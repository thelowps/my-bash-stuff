import sys
from glob import glob

PLUGINS = {}

class Canvas:
    
    def __init__ ( self, width = 30, height = 30 ) :
        #IMPORT THE PLUGINS
        plugNames = glob( "plugins/*.py" )
        
        for plugin in plugNames:
            print "Importing ", plugin
            plugin = plugin.split( '/' )
            plugin = plugin[1].split('.')
            plugin = plugin[0]
            print "Importing ", plugin
            try:
                mod = __import__( "plugins." + plugin, fromlist=[plugin] )
                
            except ImportError:
                print "IMPORT ERROR"
                
        mod = __import__( "plugins.Box", fromlist = ['Box'] )
        Box = mod.Box
        box = Box()
        box.drawBox( [1,1], [1,1], 1 )
        self.width = width
        self.height = height
        self.pixels = [ [' ']*self.height for x in range(0, self.width) ]
        self.color = ['#']

    def handleInput ( self, params ) :
        
        # Run through the keys, creating an object for each 

        # CLEAR CANVAS -- clear
        if params.has_key( "-clear" ):
            self.clear()

        # SET COLOR -- color
        if params.has_key( "-color" ):
            self.setColor( params["-color"][0] )

        # SINGLE PIXEL -- coord
        if params.has_key( "-coord" ):
            self.setPixel( self.color[0], params["-coord"][0], params["-coord"][1] )

        # PIXEL ROW -- row
        if params.has_key( "-row" ):
            self.drawRow( params["-row"][0] )

        # PIXEL COLUNM -- col
        if params.has_key( "-col" ):
            self.drawCol( params["-col"][0] )

        # PIXEL BOX -- box
        if params.has_key( "-box" ):
            topLeft  = (int( params["-box"][0] ), int( params["-box"][1] ))
            botRight = (int( params["-box"][2] ), int( params["-box"][3] ))
            fill = True
            if params.has_key( "-nofill" ):
                fill = False
            self.drawBox( topLeft, botRight, fill )

        # PIXEL LINE -- line
        if params.has_key( "-line" ):
            start = (int(params["-line"][0]), int(params["-line"][1]))
            end   = (int(params["-line"][2]), int(params["-line"][3]))
            self.drawLine( start, end )
                
        # RESIZE CANVAS
        if params.has_key( "-resize" ):
            self.resizeCanvas( params["-resize"][0], params["-resize"][1] )


    def setColor ( self, color ) :
        self.color = color

    def clear ( self ) :
        self.pixels = [ [' ']*self.height for x in range(0, self.width) ]

    def drawCol ( self, colNum ):
        cols = []
        rows = []
        for i in range( 0, self.height ):
            rows.append( i )
            cols.append( colNum )
        self.setPixels( cols, rows )

    def drawRow ( self, rowNum ):
        cols = []
        rows = []
        for i in range( 0, self.width ):
            cols.append( i )
            rows.append( rowNum )
        self.setPixels( cols, rows )

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

        self.setPixels( cols, rows )


    def drawLine ( self, start, end ):
        cols = []
        rows = []
        width  = end[0] - start[0]
        height = end[1] - start[1]
        slope = 0
        try:
            slope = float(height)/width
        except:
            slope = 0
        print ("%2.4f" % slope)
        for i in range( 0, abs(width)+1 ): #for each x, find y, and round
            cols.append( start[0]+i )
            rows.append( start[1]+i*slope )

        self.setPixels( cols, rows )


    def setPixel ( self, color, col, row ) :
        self.pixels[int(col)][int(row)] = color

    def setPixels ( self, cols, rows ) :
        colorIndex = 0
        for col, row in zip( cols, rows ):
            self.setPixel( self.color[colorIndex], col, row )
            colorIndex += 1
            if colorIndex >= len( self.color ):
                colorIndex = 0

    def resizeCanvas ( self, width, height ):
        self.width = width
        self.height = height
        self.pieces

    def draw ( self ) :
        # PRINT NUMBERS ON TOP
        print( "  " ),
        for i in range(0, self.width):
            print( "%2.f" % i ),
        print
 
        
        for i in range(0, self.height):
            # PRINT NUMBERS ON LEFT
            print( "%2.f" % i ),
            for j in range(0, self.width):
                print( " " + self.pixels[j][i] ),
            print
