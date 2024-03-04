from random import randint
futebol = ['Botafogo', 'Flamengo','São Paulo','Corithians','Grêmio','Chapecoense','Atlético-Paranaense']
lista = list()
count = 1
while count < 6:
    escolhido = randint(0,6)
    if escolhido not in lista:
        lista.append(escolhido)
        print(f"{futebol[escolhido]}")
        count+=1
