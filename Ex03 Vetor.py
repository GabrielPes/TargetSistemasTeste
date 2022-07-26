"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal."""

from statistics import mean

faturamento_mensal = {
    'Dia 01': 2580.52,
    'Dia 02': 1250.89,
    'Dia 03': 569.99,
    'Dia 04': 789.50,
    'Dia 05': 5269.15,
    'Dia 06': 10121.87,
    'Dia 07': 2000.45,
    'Dia 08': 1223.48,
    'Dia 09': 7898.21,
    'Dia 10': 1058.20,
    'Dia 11': 3669.30,
    'Dia 12': 960.65,
    'Dia 13': 4009.78,
    'Dia 14': 7852.00,
    'Dia 15': 2780.00,
    'Dia 16': 5785.40,
    'Dia 17': 6300.55,
    'Dia 18': 3000.12,
    'Dia 19': 1489.00,
    'Dia 20': 15689.87,
    'Dia 21': 12569.65,
    'Dia 22': 4500.00,
    'Dia 23': 7400.65,
    'Dia 24': 6300.20,
    'Dia 25': 9005.30,
    'Dia 26': 2789.99,
    'Dia 27': 6002.10,
    'Dia 28': 4100.00,
    'Dia 29': 1300.00,
    'Dia 30': 850.50
}

print(f'O MENOR valor de faturamento diário foi: R${min(faturamento_mensal.values())}')
print(f'O MAIOR valor de faturamento diário foi: R${max(faturamento_mensal.values())}')
media_mensal = mean(faturamento_mensal.values())
cont = 0
for v in faturamento_mensal.values():
    if v >= media_mensal:
        cont += 1
print(f'Média mensal: R${media_mensal:.2f}')
print(f'Quantidade de dias em que o valor de faturamento diário foi superior à média mensal: {cont}')
