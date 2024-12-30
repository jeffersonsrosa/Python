"""
Interpolocao basica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)"""

nome = 'Jefferson'
preco = 1000.05897643
variavel = '%s, o preco é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadeciaml de %d é %x' % (15, 15))