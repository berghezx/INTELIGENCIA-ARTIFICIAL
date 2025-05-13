# Exemplo do método upper() para strings

texto = "Python é incrível!"

# Convertendo para maiúsculas
texto_maiusculo = texto.upper()
print("Original:", texto)
print("Maiúsculas:", texto_maiusculo)

# Aplicação prática: comparação case-insensitive
entrada_usuario = "SIM"
if entrada_usuario.upper() == "SIM":
    print("\nUsuário disse SIM!")

# Exemplo do método split() para strings

frase = "Python é uma linguagem poderosa"

# Split padrão (por espaços)
palavras = frase.split()
print("Frase dividida por espaços:", palavras)

# Split com separador específico
dados = "nome,idade,profissao,cidade"
campos = dados.split(',')
print("\nDados divididos por vírgula:", campos)

# Limitando o número de splits
endereco = "Rua das Flores, 42, Centro, São Paulo, SP"
partes = endereco.split(',', 2)
print("\nEndereço com split limitado:", partes)

# Exemplo do método strip() para strings

# String com espaços extras
texto = "   Olá, Mundo!   "
print(f"Original: '{texto}'")

# Removendo espaços das extremidades
texto_limpo = texto.strip()
print(f"Após strip(): '{texto_limpo}'")

# Removendo caracteres específicos
url = "www.exemplo.com.br"
dominio = url.strip("w.mocbr")
print(f"\nURL original: '{url}'")
print(f"Domínio extraído: '{dominio}'")

# Exemplo do método replace() para strings

texto = "O gato preto cruzou a rua"

# Substituição simples
novo_texto = texto.replace("gato", "cachorro")
print("Substituição simples:", novo_texto)

# Substituição múltipla
texto_formatado = texto.replace("a", "@").replace("e", "3")
print("\nSubstituição múltipla:", texto_formatado)

# Limitando o número de substituições
texto_limitado = texto.replace("a", "@", 2)
print("\nSubstituição limitada:", texto_limitado)

# Exemplo do método startswith() para strings

nomes = ["Ana Silva", "Carlos Souza", "Maria Santos", "Antônio Pereira"]

# Verificando prefixos
print("Nomes que começam com 'A':")
for nome in nomes:
    if nome.startswith('A'):
        print("-", nome)

# Verificando com tupla de prefixos
print("\nNomes que começam com 'A' ou 'M':")
for nome in nomes:
    if nome.startswith(('A', 'M')):
        print("-", nome)

# Verificando com índice inicial
texto = "Python é ótimo"
print("\nTexto começa com 'é' a partir do índice 7?", texto.startswith('é', 7))

# Exemplo do método count() para strings

texto = "O rato roeu a roupa do rei de Roma"

# Contando ocorrências de uma substring
print("Quantidade de 'ro':", texto.count('ro'))
print("Quantidade de 'a':", texto.count('a'))

# Contando com limites
print("\nQuantidade de 'r' nos primeiros 10 caracteres:", texto.count('r', 0, 10))

# Caso de substring não encontrada
print("Quantidade de 'z':", texto.count('z'))

# Exemplo do método format() para strings

# Formatação básica
mensagem = "Olá, {}! Você tem {} anos.".format("Ana", 30)
print("Formatação básica:", mensagem)

# Formatação com índices
mensagem = "Olá, {1}! Você tem {0} anos.".format(30, "Ana")
print("\nCom índices:", mensagem)

# Formatação com nomes
dados = {"nome": "Carlos", "idade": 25}
mensagem = "Olá, {nome}! Você tem {idade} anos.".format(**dados)
print("\nCom nomes:", mensagem)

# Formatação de números
valor = 1234.5678
print("\nFormatação numérica: {:.2f}".format(valor))