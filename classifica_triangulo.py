"""ESTE CÓDIGO DEVE FAZER A VERIFICAÇÃO SE OS VALORES FORMAM UM TRIÂNGULO E DO TIPO DE TRIÂNGULO"""
# Inserção dos valores
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Condicional para verificar se forma triângulo
# Caso a condição de um valor ser menor que a soma dos outros dois valores seja verdadeira retorna o tipo de triângulo
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("equilátero")
    elif a == b or b == c or a == c:
        print("isósceles")
    else:
        print("escaleno")
# Caso falso retorna como não forma triângulo
else:
    print("Não forma triângulo")
