# Operações lógicas 
# and (e) or (ou) not (não)
# and- todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo none é
# usado para representar um não valor


#-- Exerciocio Comentado --#
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'
# # if true: 
# # ...
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrou')
# else:
#     print('Saiu')
#-- Final de exercicio --#

# Availiação de curto circuito
print(True and True and True)
print(bool(0.0))
print(bool(''))
print(bool(' '))
print(True and 0 and True)