# 8) Em um campeonato de futebol existem cinco times e cada um possui onze jogadores. Faça 
# um programa que receba a idade, o peso e a altura de cada um dos jogadores, calcule e 
# mostre:
# • A quantidade de jogadores com idade inferior a 18 anos
# • A média das idades dos jogadores de cada time
# • A média das alturas de todos os jogadores do campeonato
# • A percentagem de jogadores com mais de 80 quilos entre todos os jogadores 
# do campeonato
import random
inf18=timeidade=timepeso=timealtura=time1=time2=time3=time4=time5=pesoacima=0

for i in range(5):
    timeidade=0
    for j in range(11):
        idade=random.randint(15, 20)        
        peso=round(random.uniform(60.0,90.0),1)     
        altura=round(random.uniform(1.6, 2.0),1)        
        if idade < 18:
            inf18+=1
        if peso > 80:
            pesoacima+=1
        timeidade+=idade
        timealtura+=altura
        timepeso+=peso
        if 10 == j:
            if 0 == i:
                time1=timeidade
            elif 1 == i:
                time2=timeidade
            elif 2 == i:
                time3=timeidade
            elif 3 == i:
                time4=timeidade
            elif 4 == i:
                time5=timeidade    
print("quantidade de jogadores com idade inferior a 18 anos: ",inf18)
print("A média das idades dos jogadores do time 1: ",round(time1/11))
print("A média das idades dos jogadores do time 2: ",round(time2/11))
print("A média das idades dos jogadores do time 3: ",round(time3/11))
print("A média das idades dos jogadores do time 4: ",round(time4/11))
print("A média das idades dos jogadores do time 5: ",round(time5/11))
print("A média das alturas de todos os jogadores do campeonato: ",round(timealtura/55,2))
print("A percentagem de jogadores com mais de 80 quilos entre todos os jogadores do campeonato: ",round(pesoacima*100/55,1))
