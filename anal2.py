import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = ['Numero', 'Suma', 'Resta', 'Multi', 'Divi', 'Igual']

# Expresiones regulares para tokens nuestros tokens 
t_Suma = r'\+'
t_Resta = r'\-'
t_Multi = r'\*'
t_Divi = r'\/'
t_Igual = r'\='

# Expresión regular que reconoce números enteros
def t_Numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Unicamente esta linea evita los espacios en blanco y/o saltos de linea 
t_ignore = ' \t'

# Regla para manejar los saltos de línea y actualizar el número de línea
def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# En este apartado es en donde nosotros manejamos los errores 
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Aqui vamos a construir nuestro analizador léxico
lexer = lex.lex()

# Definir las reglas de precedencia y asociatividad
precedence = (
    ('left', 'Suma', 'Resta'),
    ('right', 'Multi', 'Divi'),
)

# Escribir las reglas de producción para nuestra gramática
def p_expresion_suma(p):
    'expresion : expresion Suma termino'
    p[0] = p[1] + p[3]

def p_expresion_resta(p):
    'expresion : expresion Resta termino'
    p[0] = p[1] - p[3]

def p_expresion_termino(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_multi(p):
    'termino : termino Multi factor'
    p[0] = p[1] * p[3]

def p_termino_divi(p):
    'termino : termino Divi factor'
    p[0] = p[1] / p[3]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_factor_numero(p):
    'factor : Numero'
    p[0] = p[1]

def p_expresion_error(p):
    'expresion : error'
    print("Error de sintaxis en la entrada!")

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Probar el analizador sintáctico con la entrada
data = " "
lexer.input(data)

# Función personalizada creada por el usuario para imprimir los tokens
def imprimir_token(token):
    print(f"Mi Token (tipo = {token.type}, valor = {token.value}, Linea Del Token = {token.lineno}, Posicion del token = {token.lexpos})")

# Imprimir tokens
while True:
    token = lexer.token()
    if not token:
        break
    imprimir_token(token)

# Parsear cada línea individualmente
for line in data.split('\n'):
    result = parser.parse(line, lexer=lexer)
   
