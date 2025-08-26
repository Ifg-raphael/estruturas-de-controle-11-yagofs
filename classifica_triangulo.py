nome = ["a", "b", "c"]
valores = []
for numero in nome:
    valor = int(input(f"Digite o valor de {numero}: "))
    valores.append(valor)
if len(set(valores)) == 1:
    print ("é um triângulo equilátero")
elif len(set(valores)) == 2:
    print ("é um triângulo isósceles")
elif len(set(valores)) == 3:
    print ("é um triângulo escaleno")
else:
    print ("não é um triângulo")
