# if / elif ... / else
# se / se nao se / se nao

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1: 
    print('Código para condicao 1')
elif condicao2:
    print('Código para condicao 2')
    # pass # olha e pular o código
elif condicao3:
    print('Código para condicao 3')
elif condicao4:
    print('Código para condicao 4')
else:
    print('Nenhuma codicao foi satisfeita')

if 10 == 10:
    print('outro if')

print ('Fora do if')