import json

# Função para calcular o faturamento
def calcular_faturamento(dados):
    # Filtrando dias com faturamento
    faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

    if not faturamento:
        return {
            'menor_valor': None,
            'maior_valor': None,
            'dias_acima_media': 0
        }

    menor_valor = min(faturamento)
    maior_valor = max(faturamento)

    media_mensal = sum(faturamento) / len(faturamento)

    dias_acima_media = len([valor for valor in faturamento if valor > media_mensal])

    return {
        'menor_valor': menor_valor,
        'maior_valor': maior_valor,
        'dias_acima_media': dias_acima_media
    }

# Ler dados do arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Calcular e exibir resultados
resultados = calcular_faturamento(dados)
print(f"Menor valor de faturamento: {resultados['menor_valor']}")
print(f"Maior valor de faturamento: {resultados['maior_valor']}")
print(f"Número de dias com faturamento acima da média: {resultados['dias_acima_media']}")
