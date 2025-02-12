import ply.lex as lex

# Procesa componentes basicos de una expresion matematica

# Definición de tokens
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE']

# Expresiones regulares para tokens nuestros tokens 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Expresión regular que reconoce números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Unicamente esta linea evita los espacios en blanco y/o saltos de linea 
t_ignore = ' \n'

# En este apartado es en donde nosotros manejamos los errores 
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Aqui vamos a construir nuestro analizador y poner los datos de los ejemplos de uso 
lexer = lex.lex()

data = ("3 + 4 * 2 x\n7-8")
lexer.input(data)

# Función personalizada para imprimir tokens
def print_custom_token(token):
    print(f"MyToken(type={token.type}, value={token.value}, lineno={token.lineno}, lexpos={token.lexpos})")

# Aqui se imprimen los tokens que reconoce nuestro analizador 
while True:
    token = lexer.token()
    if not token:
        break
    print_custom_token(token)