from ply import lex, yacc

# Token definitions
tokens = (
    'SELECT', 'TRUNCATE', 'DROP',
    'IDENTIFIER', 'COMMA','SEMICOLON', 'FROM',
    'TABLE','COMMIT','RENAME', 'TO'
)

# Token regex patterns
def t_SELECT(t):
    r'\b(SELECT)\b'
    return t

def t_COMMIT(t):
    r'\b(COMMIT)\b'
    return t

def t_TRUNCATE(t):
    r'\b(TRUNCATE)\b'
    return t

def t_DROP(t):
    r'\b(DROP)\b'
    return t

def t_FROM(t):
    r'\b(FROM)\b'
    return t

def t_TABLE(t):
    r'\b(TABLE)\b'
    return t

def t_IDENTIFIER(t):
    r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
    return t

def t_RENAME(t):
    r'\b(RENAME)\b'
    return t

def t_TO(t):
    r'\b(TO)\b'
    return t


t_COMMA = r','
t_SEMICOLON = r';'
# Ignored characters
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parsing rules
def p_statement_select(p):
    'statement : SELECT select_list FROM IDENTIFIER SEMICOLON'
    print('Valid statement:','SELECT', ','.join(p[2]), 'FROM', p[4])

def p_select_list(p):
    '''
    select_list : IDENTIFIER
                | IDENTIFIER COMMA select_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_statement_truncate(p):
    'statement : TRUNCATE TABLE IDENTIFIER SEMICOLON'
    print('Valid statement: TRUNCATE', 'TABLE', p[3])

def p_statement_drop(p):
    'statement : DROP TABLE IDENTIFIER SEMICOLON'
    print('Valid statement:', p[4])

def p_statement_commit(p):
    'statement : COMMIT SEMICOLON'
    print('Valid statement: COMMIT;')

def p_statement_rename(p):
    'statement : RENAME IDENTIFIER TO IDENTIFIER SEMICOLON'
    print('Valid RENAME statement: RENAME', p[2], 'TO', p[4])

def p_error(p):
    print("Invalid statement")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the parser with user input
input_text = input("Enter SQL statement: ")
lexer.input(input_text)
try:
    parser.parse(input_text)
except:
    pass  # Ignore exceptions for invalid statements
