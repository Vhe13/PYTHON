"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for vendadeira
loop Infinito -> Quando o código não tem fim.
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome?')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
print('Acabou')