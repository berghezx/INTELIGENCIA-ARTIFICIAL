"""
Demonstração dos principais métodos de tuplas em Python
"""

# Criando uma tupla de exemplo
frutas = ('maçã', 'banana', 'laranja', 'maçã', 'uva')

# Método count() - conta ocorrências de um elemento
quantidade_maca = frutas.count('maçã')
print(f"A palavra 'maçã' aparece {quantidade_maca} vezes na tupla")

# Método index() - encontra o índice da primeira ocorrência
indice_laranja = frutas.index('laranja')
print(f"A palavra 'laranja' aparece primeiro no índice {indice_laranja}")

# Tentativa de usar index() com elemento inexistente (com tratamento de erro)
try:
    indice_melancia = frutas.index('melancia')
except ValueError:
    print("'melancia' não encontrada na tupla - isso gera um ValueError")