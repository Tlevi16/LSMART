import termcolor 

# programming language: LSMART
# front end: python
# created date: 12:28 pm, 28.10.2020
# author(s): Levi Israel .T
# copyright 2020 

# console class
# functions: printvl, 
class console(): 
    def printvl(self, value):
        print(value) 

    def printcvl(self, value, color):
        termcolor.cprint(value, color)

    class error():
        def syntaxError(self, error):
            raise SyntaxError(f'syntaxError - {error}') 

        def NullValueError(self, error):
            raise ValueError(f'NullValueError - {error}') 

    class debug():
        def d(self, tag, message):
            termcolor.cprint(f'debug - {tag}: {message}', 'green') 

    class warn():
        def w(self, tag, message):
            termcolor.cprint(f'warning - {tag}: {message}', 'yellow')       

    