# 6) Faça um programa que receba várias idades. Para finalizar a entrada deve ser digitado 
# idade zero ou negativa. Calcule e mostre na tela:
# • A quantidade de pessoas que tem idade entre 20 e 40 anos
# • A maior idade
# • A menor idade
# • A média das idades
import random
con=maior=menor=contotal=total=0
idade=1
while idade > 0:
    idade=0     
    idade=random.randint(-5, 60)    
    print("Idade aleatória: ",idade)
    print("")
    if idade >= 0:
        if idade > 19 and idade < 41:
            con+=1
        if maior < idade:
            maior=idade
        if menor > idade or menor == 0:
            menor=idade
        contotal+=1
        total+=idade
if contotal != 0:
    print("A quantidade de pessoas que tem idade entre 20 e 40 anos: ",con)
    print("A maior idade: ",maior)
    print("A menor idade: ",menor)
    print("A média das idades: ",round(total/contotal))