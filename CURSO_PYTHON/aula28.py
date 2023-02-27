"""
Exercício
peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
se nome e idade forem digitados: 
    exiba:
    Seu nome é
    Seu nome invertido é  {nome invertido}
    seu nome contém (ou não) espaços
    seu nome tem {n} letras 
    a primeira letra do seu nome  é {Letra}
    A última letra do seu nome é {letra}
    se nada for digitado exiba "desculpa, você deixou cambos vazios."
"""

nome = input("Qual seu nome: ")
idade = input("Qual sua idade?: ")
nomeinvertido = (nome[::-1])
n = len(nome)
pletra = (nome[0:1:])
uletra = (nome[-1::])

if nome and idade:
    print(f'Seu nome é {nome} ')
    print(f'Sua idade é {idade}')
    print(f'Seu nome ínvertido fica {nomeinvertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {n} qtd de letras')
    print(f'Primeira letra do seu nome é {pletra} ')
    print(f'Ultima letra do seu nome é {uletra} ')
else:
    print('Desculpe você não prencheu corretamente!')