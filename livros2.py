from pprint import pprint

livros = [
    ("Dom Quixote", "Miguel de Cervantes", 1605),
    ("Orgulho e Preconceito", "Jane Austen", 1813),
    ("O Grande Gatsby", "F. Scott Fitzgerald", 1925),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
    ("1984", "George Orwell", 1949),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
    ("A Revolução dos Bichos", "George Orwell", 1945),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951),
    ("O Código Da Vinci", "Dan Brown", 2003),
]

catalogos = {}

for livro in livros:
    titulo = livro[0]
    autor = livro[1]
    ano = livro[2]

    catalogos[titulo] = {"autor": autor, "ano": ano }
print(catalogos, "\n")



# list comprehension
catalogo = {
    livro[0]: {"autor": livro[1], "ano": livro[2]}
    for livro in livros
}
print(f"Catálogo {catalogo}")

# import pprint (from pprint import pprint) - pretty print (impressão “bonita”)
pprint(catalogo)

# -------------------------------------------------------------------------------


catalogo_impresso = {
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 1605},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 1813},
    "O Grande Gatsby": {"autor": "F. Scott Fitzgerald", "ano": 1925},
    "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "ano": 1967},
    "1984": {"autor": "George Orwell", "ano": 1949},
    "Harry Potter e a Pedra Filosofal": {"autor": "J.K. Rowling", "ano": 1997},
    "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
    "A Revolução dos Bichos": {"autor": "George Orwell", "ano": 1945},
    "O Apanhador no Campo de Centeio": {"autor": "J.D. Salinger", "ano": 1951},
    "O Código Da Vinci": {"autor": "Dan Brown", "ano": 2003},
}

livros_antigos = {}

for titulo, info in catalogo_impresso.items():
    ano = info["ano"]

    if ano < 1950:
        livros_antigos[titulo] = info

print(f"\nLivros antigos: {livros_antigos}")




# list comprehension
livros_antigos = {
    titulo: info
    for titulo, info in catalogo_impresso.items()
    if info["ano"] < 1950
}

print("\nLivros antigos")
pprint(livros_antigos, sort_dicts=False)