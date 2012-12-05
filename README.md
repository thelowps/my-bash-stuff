my-bash-stuff
=============

David's bash scripts and settings.

/**------------------------------------------------------------
-- agenda -- 
A simple agenda script to keep track of things to do, with due 
dates and tags for each item, as well as an importance level 
and a completion flag. Nowhere near done

FEATURES:
-> Tasks can be added with the + option. Usage is:
   agenda + task [date] [flags] [importance]
-> All tasks can be viewed in an organized form if script is
   called with no arguments.

TODO:
-> Ability to check tasks off
-> Ability to remove tasks
-> Ability to selectively view tasks by date, tag or importance

NOTES:
-> Might want to scrap this project in favor of emacs org mode
   or simply using a Google calendar more efficiently.


/**------------------------------------------------------------
-- clean --
"Cleans" the current directory by removing "stain" files.

FEATURES:
-> Removes files specified in the GLOBAL_STAINS variable.
   Typically this includes *~ and #*# files (backups created
   by some text editors).
-> Reads a directory's .stains file (if it exists) and "cleans"
   the files specified in it as well. File should be a space-
   separated list
-> Can be called recursively.

TODO:
-> Allow user to select director(y|ies) to clean
-> Allow option to append a directory's custom stains to its
   subdirectory's custom stains when cleaning recursively.
-> Allow option to NOT run 'make clean', something like -n


/**------------------------------------------------------------
-- makeclass --
Create c++ classes with the given name based on the templates
in the .makeclass_templates directory.

FEATURES:
-> Creates .h and .cpp files with header comments
-> Implements an empty constructor and destructor

TODO:
-> Change header guards to account for camelcase classnames,
   eg. MyClass should have a MY_CLASS_H header guard, not
   MYCLASS_H.
-> Allow comments to be passed as argument to be placed at the
   top of each file. This might be hard due to word wrapping.
-> Allow option to template the class
-> Maybe allow for specification of getters and setters?
   Although I hate nitpickity data encapsulation...

NOTES:
-> I can't think of much else to implement that will actually
   be useful...


/**------------------------------------------------------------
-- goto --
Super simple shortcut to ssh into an ND machine.

FEATURES:
-> Allows user to pass in host to ssh into. Default  is 
   student00.cse.

TODO:
-> Allow user to pass in flags (I'm looking at you, -X)


/**------------------------------------------------------------
-- drop --
Just an idea for a script that would copy given files into a 
specified dropbox. Pretty useless, honestly. 
Usage: drop FILE1, FILE2 ... DROPBOX[/subdirectory]
Example: drop file.h file.cpp Graphics/hw10

I need to think bigger.

/**------------------------------------------------------------
-- TODO --
- Make a .bashrc file