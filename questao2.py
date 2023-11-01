def calcular_area_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

def verificar_formacao_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if verificar_formacao_triangulo(a, b, c):
    area = calcular_area_triangulo(a, b, c)
    print(f"Os valores formam um triângulo e sua área é {area}")
else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo.")