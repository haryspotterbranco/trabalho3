# === EXERCÍCIO 1: Criação básica e append() ===
print("--- Exercício 1 ---")
filmes = ["Matrix", "O Senhor dos Anéis", "De Volta para o Futuro"]
filmes.append("Interestelar")
print(filmes)
print()

# === EXERCÍCIO 2: Lista de Listas ===
print("--- Exercício 2 ---")
livros = [
    [1, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
    [2, "1984", "George Orwell", 1949],
    [3, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954]
]
print(livros)
print()

# === EXERCÍCIO 3: Acesso a Índices ===
print("--- Exercício 3 ---")
print("Autor do segundo livro:", livros[1][2])
print()

# === EXERCÍCIO 4: Iteração e f-strings ===
print("--- Exercício 4 ---")
for livro in livros:
    print(f'ID: {livro[0]} | O livro "{livro[1]}" foi escrito por {livro[2]} em {livro[3]}.')
print()

# === EXERCÍCIO 5: Alteração Direta ===
print("--- Exercício 5 ---")
livros[0][3] = 2024
print("Registro alterado (ano 2024):", livros[0])
print()

# === EXERCÍCIO 6: Busca Simples ===
print("--- Exercício 6 ---")
titulo_procurado = "1984"
for livro in livros:
    if livro[1] == titulo_procurado:
        print(f"Livro localizado! ({titulo_procurado})")
        break
print()

# === EXERCÍCIO 7: Tratamento de 'Não Encontrado' ===
print("--- Exercício 7 ---")
id_procurado_livro = 99
encontrado = False
for livro in livros:
    if livro[0] == id_procurado_livro:
        print("Livro localizado!")
        encontrado = True
        break
if not encontrado:
    print("Livro não encontrado")
print()

# === EXERCÍCIO 8: Remoção de Registro ===
print("--- Exercício 8 ---")
id_remover = 2
for indice, livro in enumerate(livros):
    if livro[0] == id_remover:
        livros.pop(indice)
        break
print("Lista de livros após a remoção:")
for livro in livros:
    print(livro)
print()

# === EXERCÍCIO 9: Operações Combinadas (Cadastro) ===
print("--- Exercício 9 ---")
funcionarios = []
funcionarios.append([1, "Ana Silva", "Analista", 4500.00])
funcionarios.append([2, "Carlos Souza", "Desenvolvedor", 6000.00])
for func in funcionarios:
    print(f"ID: {func[0]} | Nome: {func[1]} | Cargo: {func[2]} | Salário: R$ {func[3]}")
print()

# === EXERCÍCIO 10: Desafio de Atualização Condicional ===
print("--- Exercício 10 ---")
id_procurado_func = 2
for indice, func in enumerate(funcionarios):
    if func[0] == id_procurado_func:
        funcionarios[indice][3] += 500  
        print(f"Aumento aplicado! O novo salário de {func[1]} é R$ {funcionarios[indice][3]}")
        break