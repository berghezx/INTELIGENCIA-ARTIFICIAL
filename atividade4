# Exemplo de uso da função built-in len()

# Com lista
numeros = [1, 2, 3, 4, 5]
print("Tamanho da lista:", len(numeros))  # Retorna 5

# Com string
nome = "Python"
print("Tamanho da string:", len(nome))  # Retorna 6

# Com tupla
coordenadas = (10, 20)
print("Tamanho da tupla:", len(coordenadas))  # Retorna 2

# Exemplo de uso da função built-in sum()

# Soma de lista de inteiros
valores = [10, 20, 30, 40]
total = sum(valores)
print("Soma dos valores:", total)  # 100

# Soma com valor inicial
total_com_inicio = sum(valores, 100)  # Começa com 100
print("Soma com valor inicial:", total_com_inicio)  # 200

# Exemplo de uso da função built-in sorted()

numeros = [3, 1, 4, 1, 5, 9, 2]

# Ordem crescente (padrão)
ordenados = sorted(numeros)
print("Ordenados crescente:", ordenados)  # [1, 1, 2, 3, 4, 5, 9]

# Ordem decrescente
ordenados_desc = sorted(numeros, reverse=True)
print("Ordenados decrescente:", ordenados_desc)  # [9, 5, 4, 3, 2, 1, 1]

# Com strings
palavras = ["banana", "abacaxi", "laranja"]
print("Palavras ordenadas:", sorted(palavras))  # ['abacaxi', 'banana', 'laranja']

# Exemplo de uso da função built-in enumerate()

frutas = ['maçã', 'banana', 'morango']

# Uso básico em loop
print("Enumerate em loop:")
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

# Com start personalizado
print("\nEnumerate com start=1:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"Posição {indice}: {fruta}")

# Exemplo de uso da função built-in zip()

nomes = ['Ana', 'João', 'Carlos']
idades = [25, 30, 35]
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

# Zip básico
print("Pares nome-idade:")
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# Zip com múltiplas listas
print("\nDados completos:")
for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome}, {idade} anos, mora em {cidade}")

# Convertendo para lista de tuplas
pessoas = list(zip(nomes, idades, cidades))
print("\nLista de tuplas:", pessoas)
