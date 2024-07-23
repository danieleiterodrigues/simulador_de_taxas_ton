def calcular_valores_parcelas(valor_recebido, bandeira):
    # Definindo as taxas e valores para cada bandeira e número de parcelas
    taxas = {
        'Visa/Master': {
            1: 0.0079,
            2: 0.0399,
            3: 0.0499,
            4: 0.0599,
            5: 0.0699,
            6: 0.0699,
            7: 0.0699,
            8: 0.0699,
            9: 0.0699,
            10: 0.0699,
            11: 0.0699,
            12: 0.0699,
        },
        'Elo/Hipercard/Amex': {
            1: 0.0434,
            2: 0.0702,
            3: 0.0758,
            4: 0.0838,
            5: 0.0938,
            6: 0.1038,
            7: 0.1098,
            8: 0.1138,
            9: 0.1238,
            10: 0.1288,
            11: 0.1374,
            12: 0.1378,
        }
    }

    if bandeira not in taxas:
        return "Bandeira inválida."

    valores_parcelas = {}
    for parcelas, taxa in taxas[bandeira].items():
        valor_original = valor_recebido / (1 - taxa)
        valores_parcelas[parcelas] = round(valor_original, 2)

    return valores_parcelas

# Exemplo de uso:
valor_recebido = 200.00
bandeira = 'Visa/Master'

valores_parcelas = calcular_valores_parcelas(valor_recebido, bandeira)
print(f"Para o valor recebido de R${valor_recebido:.2f} com a bandeira {bandeira}, o cliente pagará:")
for parcelas, valor in valores_parcelas.items():
    print(f"{parcelas}x: R${valor:.2f}")
