def calcular_media(valores):
    tamanho = 0
    soma = 0.0

    for i, valor_a_somar in enumerate(valores):
        soma += valor_a_somar
        tamanho += 1

    media_valores = soma / tamanho
    return media_valores


valores_recebidos = []

while True:
    valor = input("Digite um valor ou 'ok' para sair: ")
    if valor.lower() == "ok":
        break
    else:
        valores_recebidos.append(float(valor))

media = calcular_media(valores_recebidos)

print(f"A média dos valores é {media}")
