"""
Exercício
Peca ao usuario para digitar seu nome
Peca ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é
        Seu nome invertido é 
        Se o nome contem (ou nao) espacos
        Seu nome tem (n) letras
        A primeira letra do seu nome é 
        A ultima letra do seu nome é
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, voce deixou campos vazios"
"""

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome:
    print('Seu nome é ', nome)
    print('Seu nome invertido é ', nome[::-1]) # pega a string invertida
    print('Sua idade é ', idade)
    if ' ' in nome: # Verificado se tem espaco ou nao / ' ' = se tem espaco ou nao
        print('O nome contém espaços.')
    else:
        print('O nome nao contém espacos')
    print(f'Seu nome tem {len(nome)} letras') # Quantidade de caractere
    print(nome[0]) # Primeira letra
    print(nome[-1]) # Ultima letra

else:
    print('Desculpe, voce deixou campos vazios')