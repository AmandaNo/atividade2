
def converter_idade_em_dias_para_anos_meses_dias(idade_em_dias):
    anos = idade_em_dias // 365
    meses = (idade_em_dias % 365) // 30
    dias = (idade_em_dias % 365) % 30

    return anos, meses, dias

idade_em_dias = int(input("Digite a idade em dias: "))
anos, meses, dias = converter_idade_em_dias_para_anos_meses_dias(idade_em_dias)

print(f"A idade é {anos} anos, {meses} meses e {dias} dias.")