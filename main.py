import phoenixProduction.enxLexer
import phoenixProduction.enxParser
import phoenixProduction.enxExec

if __name__ == '__main__':
    lexer = phoenixProduction.enxLexer.BasicLexer()
    parser = phoenixProduction.enxParser.BasicParser()
    print('phoenixInt')
    env = {}

    while True:
        
        try:
            text = input('phoenixInt > ')
        
        except EOFError:
            break

        if text:
            tree = parser.parse(lexer.tokenize(text))
            phoenixProduction.enxExec.BasicExecute(tree, env)