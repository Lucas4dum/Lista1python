# 7) Faça um programa que calcule e mostre na tela a tabuada de 1 a 10.
import random
total=0
for i in range(1,11):
    for j in range(1,11):
        total=i*j
        print(total,end=" ")
        
    print("")