"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for vendadeira
loop Infinito -> Quando o código não tem fim.
"""
contador = 0 

while contador <= 100: 
    contador += 1
    print(contador)

    if contador == 6:
        continue
    
    if contador == 40: 
        break

print('Acabou')
