# This is a linting tool that can be given various specifications and will find errors based on them. 
# This is a generic linter that can be customized and set up to lint any file format
class lintFile():

    # Check to make sure code is indented up to standard
    def checkIndents(self, fileType):
        print ("Checked indents")
        
    # Check to make sure all lines end in a semicolon or don't end in one based on coding style
    def checkEndings():
        print ("Checked endings")
    
    # Check for spacing inbetween brackets for example if ( statements ) { } where it spaces individually
    def checkSpacing():
        print ("Checked spacing")

# Specific linting for python
class lintPython():
    def checkIndents():
        print ("Checked indents")
        
# Specific linting for javascript    
class lintJS():
    def checkIndents():
        print ("Checked indents")
    
    