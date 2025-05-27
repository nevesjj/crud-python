produtos = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Óleo de soja",
    "Açúcar",
    "Café",
    "Sal",
    "Farinha de trigo",
    "Molho de tomate",
    "Sabonete",
    "Detergente",
    "Papel higiênico",
    "Shampoo",
    "Escova de dentes",
    "Creme dental",
    "Sabão em pó",
    "Leite",
    "Queijo",
    "Presunto",
    "Manteiga"
]
valores= [
    8.50,
    8.30,
    4.99,
    7.25,
    3.80,
    12.00,
    2.50,
    5.40,
    3.00,
    1.90,
    4.20,
    15.00,
    10.50,
    6.00,
    7.00,
    18.90,
    4.50,
    25.00,
    22.00,
    12.50
]

total = dict(zip(produtos,valores))

for produtos, valores in total.items():
    print(f"{produtos}: R${valores}")