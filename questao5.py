def inverter_palavras_na_frase(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase

frase = input("Digite uma frase: ")
nova_frase = inverter_palavras_na_frase(frase)

print(f"A nova frase com as palavras invertidas é: {nova_frase}")