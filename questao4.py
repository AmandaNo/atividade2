def eh_primo(n):
    if 1 <= numero <= 100:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False

numero = int(input("Digite um número: "))

if eh_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")