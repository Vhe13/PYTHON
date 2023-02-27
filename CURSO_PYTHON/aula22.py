# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira. 
# se qualqeur valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também Existe o tipo None que é 
# usado para representar um não valor

# entrada = input('[E]Entrar [S]air')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if (entrada == 'E' or entrada== 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
#print(True and 0 and True)
#senha = 0 or False or 0 or 'abc' or True
#print(senha)

senha = input('Senha: ') or 'Sem senha'
print(senha) 
