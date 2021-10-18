# 2) Faça um programa que receba dez números inteiros. Calcule e mostre:
# • A soma dos números primos
# • A média dos números múltiplos de 3 que são maiores que 10
# • A média dos números que são maiores ou iguais a 10 e menores ou iguais a 30
import random
somapri=contador=soma=contadornum=somanum=somanumtotal=totalsoma=0
for x in range(10):
    numero=random.randint(10, 40)
    print("Número inteiro aleatório: ",numero)
    contador=0
    for i in range(1, numero+1):
        if numero % i == 0:
            contador+=1
            
    if contador == 2:
        somapri+=numero
    if numero % 3 == 0 and numero > 10:
        contador+=1
        soma+=numero
    if numero >= 10 and numero <= 30:
        contadornum+=1
        somanum+=numero
if contador > 0:
    totalsoma=soma/contador
if contadornum > 0:
    somanumtotal=somanum/contadornum
print("A soma dos números primos: ",somapri)
print("A média dos números múltiplos de 3 que são maiores que 10: ",round(totalsoma))
print("A média dos números que são maiores ou iguais a 10 e menores ou iguais a 30: ",round(somanumtotal))

