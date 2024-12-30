"""
Fatiamento de strings
0123456789
Olá Mundo
-987654321
Fatiamento [i:f:p] [: :]
    i: Índice inicial (inclusive).
    f: Índice final (exclusive).
    p: Passo (opcional)
obs.: a funcao len retorna a quantidade de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[4:7:]) # Escolhe onde comeca e onde termina

# len é para contar a quantidade de caracteres
variavel1 = 'Jefferson'
print(len(variavel1))

variavel2 = 'Jefferson'
print(variavel2[0:len(variavel2):1]) # Verificar cada caracter
print(variavel2[0:9:3]) # conta de 3 em 3 caracteres
print(variavel2[-1:-10:-1]) # pega a string invertida