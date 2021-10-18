# 1) Escreva um programa que leia um conjunto de 10 números inteiros. Calcule e mostre:
# a) o menor número
# b) a soma dos números pares e maiores que 10
# c) a quantidade de números ímpares
# d) a média dos números maiores que 20
import random
menor=somanum=contadorimp=contador=somamaior=0
for i in range(10):
    numero=random.randint(10, 30)
    print("Número inteiro aleatório: ",numero)
    if i ==0:
        menor=numero    
    if menor > numero:
        menor=numero
    if numero % 2 == 0 and 10 < numero:
        somanum+=numero
    if numero % 2 == 1:
        contadorimp+=1
    if numero > 20:
        contador+=1
        somamaior+=numero
if contador > 0:
    somamaior=somamaior/contador
print("O menor número: ",menor)
print("A soma dos números pares e maiores que 10: ",somanum)
print("a quantidade de números ímpares: ",contadorimp)
print("A média dos números maiores que 20: ",round(somamaior))

