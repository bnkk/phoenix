from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING }
    ignore = '\t '
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # Define tokens as regular expression
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    # Number token
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    
    # Comment token
    @_(r'//.*')
    def COMMENT(self, t):
        pass

    # Newline token
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')