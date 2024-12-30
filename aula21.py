# Operadores lógicos
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser verdadeiras
# Se qualquer valor for considerado falsy, a expressao inteira sera avaliada naquele valor
# Sao considerados false (que voce ja viu)
# 0 0 0 False
# Tambem existe o tipo None que é usado para representar um nao valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)