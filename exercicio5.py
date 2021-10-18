# 5) Faça um programa que receba 10 números inteiros. Calcule o fatorial de cada número e 
# mostre na tela.
import random
total=1
for i in range(10):
    numero=random.randint(1,20)
    for j in range(1, numero+1):       
        total = j*total        
    print("o fatorial de",numero,"é igual a",total)
    total=1

