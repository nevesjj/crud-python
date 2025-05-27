produtos = [
    {'nome': 'Calça Jeans', 'preco': 180.0},
    {'nome': 'Bermuda', 'preco': 120.0},
    {'nome': 'Vestido', 'preco': 750.0},
    {'nome': 'Camiseta', 'preco': 85.0},
    {'nome': 'Terno', 'preco': 920.0},
    {'nome': 'Top', 'preco': 150.0},
    {'nome': 'Camisa Social', 'preco': 320.0},
    {'nome': 'Blazer', 'preco': 280.0},
    {'nome': 'Meias', 'preco': 45.0},
    {'nome': 'Short Alfaiataria', 'preco': 210.0}
]

filtro_produtos = []
preco_max = float(input("Digite o preço máximo: "))
preco_min = float(input("Digite o preço mínimo: "))

for produto in produtos:
    if preco_min <= produto['preco'] <= preco_max:
        filtro_produtos.append(produto)

print("Produtos na faixa de preço:")
for p in filtro_produtos:
    print(f"{p['nome']}: R$ {p['preco']:.2f}")