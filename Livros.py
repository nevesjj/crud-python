livros = [
    {"titulo": "O senhor dos anéis", "genero": "Fantasia"},
    {"titulo": "Harry Potter e a pedra filosofal", "genero": "Fantasia"},
    {"titulo": "Dom Casmurro", "genero": "Romance"},
    {"titulo": "Orgulho e preconceito", "genero": "Romance"},
    {"titulo": "1984", "genero": "Ficção Científica"},
    {"titulo": "Duna", "genero": "Ficção Científica"},
    {"titulo": "A menina que roubava livros", "genero": "Drama"},
    {"titulo": "O pequeno príncipe", "genero": "Fábula"},
    {"titulo": "O código da vinci", "genero": "Suspense"},
    {"titulo": "It a coisa", "genero": "Terror"}
]

livrosPorGenero = {}

for livro in livros:
    genero = livro["genero"]
    titulo = livro["titulo"]

    if genero not in livrosPorGenero:
        livrosPorGenero[genero] = []
        
    livrosPorGenero[genero].append(titulo)

for genero, titulos in livrosPorGenero.items():
    print(f"{genero}: {titulos}")