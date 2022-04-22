import os

name = str(input("Nome da vendedora: "))

calVal = float(input("Qual o valor da Calça: R$"))
calQtd = int(input("Qual a quantidade de Calça: "))
bluVal = float(input("Qual o valor da Blusa: R$"))
bluQtd = int(input("Qual a quantidade de Blusa: ")) 
saiVal = float(input("Qual o valor da Saia: R$"))
saiQtd = int(input("Qual a quantidade de Saia: ")) 
os.system('clear')

calcCal = calVal*calQtd
calcBlu= bluVal*bluQtd
calcSai = saiVal*saiQtd

soma = calcCal+calcBlu+calcSai

result = 0.12*soma
print("Nome da Vendedora: ",name)
print("Comissão: R$",result)