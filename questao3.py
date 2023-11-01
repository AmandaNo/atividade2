def encontrar_menor_numero(a, b, c):
    return min(a, b, c)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

menor_numero = encontrar_menor_numero(a, b, c)

print(f"O menor número entre {a}, {b} e {c} é {menor_numero}.")