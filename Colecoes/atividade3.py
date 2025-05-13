
# a) Criação e exibição de uma tupla
# Criando uma tupla com dados de coordenadas geográficas
coordenadas = (-23.5505, -46.6333)  # Tupla com latitude e longitude de São Paulo

# Mostrando o resultado
print("Coordenadas:", coordenadas)  # Exibe a tupla completa
print("Latitude:", coordenadas[0])  # Acessa o primeiro elemento (índice 0)
print("Longitude:", coordenadas[1]) # Acessa o segundo elemento (índice 1)

# b) Demonstração dos métodos principais (já feito na Atividade 2)

# c) Diferença entre lista e tupla
"""
Principais diferenças entre listas e tuplas:

1. Mutabilidade:
   - Listas são mutáveis (podem ser alteradas após criação)
   - Tuplas são imutáveis (não podem ser alteradas após criação)

2. Sintaxe:
   - Listas usam colchetes: [1, 2, 3]
   - Tuplas usam parênteses: (1, 2, 3)

3. Desempenho:
   - Tuplas são mais eficientes em termos de memória e velocidade

4. Casos de uso:
   - Listas: para coleções que podem mudar
   - Tuplas: para dados constantes (coordenadas, configurações, etc.)
"""
