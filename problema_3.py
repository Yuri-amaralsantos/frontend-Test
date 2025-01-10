import json

# Exemplo de dados (substitua pelo arquivo JSON real)
dados = {
    "dias": [
        {"dia": 1, "faturamento": 200.0},
        {"dia": 2, "faturamento": 0.0},
        {"dia": 3, "faturamento": 150.0},
        {"dia": 4, "faturamento": 300.0},
        {"dia": 5, "faturamento": 0.0},
        {"dia": 6, "faturamento": 400.0}
    ]
}

faturamentos = [dia["faturamento"] for dia in dados["dias"] if dia["faturamento"] > 0]
menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)
dias_acima_media = len([f for f in faturamentos if f > media])

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
