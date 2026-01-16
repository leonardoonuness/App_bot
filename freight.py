from pricing import TABELA_FRETE

def calcular_frete(distancia, veiculo="carro"):
    distancia = float(distancia)

    v = TABELA_FRETE.get(veiculo)

    if not v:
        raise ValueError(f"Veículo inválido: {veiculo}")

    valor = v["base"] + distancia * v["km"]

    if distancia > 50:
        valor *= 1.15  # adicional longa distância

    return round(valor, 2)

