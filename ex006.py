numero = int(input("Digite um número inteiro: "))
primos = [1,2,3,5,7,11]
divisores = 1
contador = 0
while contador < 6:
    if numero % primos[contador] == 0:
        divisores += 1
    contador += 1
if divisores == 2:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")
