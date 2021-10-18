# 4) Faça um programa que receba dez números inteiros. Calcule e mostre:
# • A quantidade de números primos
# • A soma dos números múltiplos de 3
# • A média dos pares que são maiores que 20
import random

soma3=con=total=primo=conpri=qtd=h=par=0
for i in range(10):
    numero=random.randint(1,50)    
    print("número inteiro: ",numero)    
    if numero % 3 == 0:
        soma3+=numero
    if numero % 2 == 0 and numero > 20:
        con+=1
        total+=numero
    conpri=0
    for j in range(1, numero+1):
        if numero % j == 0:
            conpri+=1
    if conpri == 2:
        qtd+=1
        print("Número primo")
print("A quantidade de números primos: ",qtd)
print("A soma dos números múltiplos de 3: ",soma3)
print("A média dos pares que são maiores que 20: ",round(total/con))
        
