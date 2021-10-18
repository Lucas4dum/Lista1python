# 3) Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e 
# sua opinião em relação ao filme (3- ótimo;2- bom;1-regular)
# Faça um programa que receba a idade e a opinião de um número indeterminado de 
# pessoas. Para finalizar a entrada deve ser digitado uma idade negativa ou zero. Calcule e 
# mostre:
# • A quantidade de pessoas que responderam ótimo
# • A quantidade de pessoas que responderam regular
# • A quantidade de pessoas que responderam bom
# • A média das idades das pessoas
import random
ot=re=bom=con=idadetotal=0
idade=1
while idade > 0:
    idade=0    
    opn=random.randint(1, 3)
    idade=random.randint(-5, 40)
    print("Entre as opções (3- ótimo;2- bom;1-regular) qual sua opnião: ",opn)
    print("Qual sua idade: ",idade)
    print("")    
    if idade > 0:
        con+=1
        idadetotal+=idade
        if opn == 1:
            re+=1
        elif opn == 2:
            bom+=1
        elif opn == 3:
            ot+=1   
if con != 0:    
    print("A quantidade de pessoas que responderam regular: ",re)
    print("A quantidade de pessoas que responderam bom: ",bom)
    print("A quantidade de pessoas que responderam ótimo: ",ot)
    print("A média das idades das pessoas: ",round(idadetotal/con))


    
    
   