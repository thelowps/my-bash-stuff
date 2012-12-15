import sys
from Canvas import Canvas

# SET PARAMETERS

# INITIALIZE STUFF
canvas = Canvas()
message = 0

# USER MESSAGES

def printHelp () :
    print( "Flags:" )
    print( "-box   :: must enter four values corresponding to the x and y coordinates of the top left and bottom right vertices, respectively" )
    print( "-row   :: enter the row number to be filled " )
    print( "-col   :: enter the col number to be filled " )
    print( "-coord :: enter the coordinates of the pixel to be colored " )
    print( "-color :: enter the ascii character to be colored in with " )

def indexErrorMessage () :
    print( "ERROR -- USER IS A DUMBASS" )

def valueErrorMessage () :
    print( "ERROR -- BAD VALUE " )


# MAIN LOOP
while True:

    # DRAWING
    canvas.draw()
    print
    if message:
        message()
        message = 0
        print

    # EVENT HANDLING
    inp = raw_input( "Enter prompt: " )
    inp = inp.split()
    try:
        params = {}
        values = []
        flag = "default"
        for tok in inp:
            if tok[0] == '-':  # INPUT IS A FLAG
                params[flag] = values  # Set the values of the previous flag
                flag = tok
                values = []

            else:
                values.append( tok )
        params[flag] = values
        
        if tok == "help":
            message = printHelp
        else: 
            canvas.handleInput( params )
            

    except IndexError as ex :
        message = indexErrorMessage

    except ValueError as ex :
        message = valueErrorMessage
