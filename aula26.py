"""
Formatacao brasica de strings
s - strings
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -   Ex.: 0>-100f,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # comeca da esquerda
print(f'{variavel: <10}.') # comeca da direita
print(f'{variavel: ^10}.') # centraliza