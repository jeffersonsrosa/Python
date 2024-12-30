# Operadores in e not in
# Strings sap iteraveis
# 0 1 2 3 4 5 6 7 8 
# J e f f e r s o n
# -9 -8 -7 -6 -5 -4 -3 -2 -1 

# nome = 'Jefferson'
# print(nome[4])
# print(nome[-4])
# print('f' in nome)
# print('a' in nome)
# print('r' not in nome)

nome =  input('Digite seu nome: ')
encontrar  = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar}nao está em {nome}')