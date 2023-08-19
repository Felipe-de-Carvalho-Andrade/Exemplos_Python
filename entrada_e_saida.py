# ENTRADA
''' 
    Para inserir dados basta usar a função input, ou type(input()), no qual type
    é o tipo de váriavel qe deseja ser lida
'''

# Solicitando ao usuário para inserir um valor
nome = input("Digite o seu nome: ")

# Lendo um número inteiro
idade = int(input("Digite a sua idade: "))

# Lendo um número de ponto flutuante
altura = float(input("Digite a sua altura em metros: "))


# SAIDA
''' 
    Para imprimir dados basta usar a função print
'''
# Imprimindo uma mensagem simples
print("Olá, mundo!")

# Imprimindo variáveis formatadas
nome = "Alice"
idade = 25
print("Nome:", nome, "Idade:", idade)

# Imprimindo com formatação
valor = 42.56789
print("Valor formatado: {:.2f}".format(valor))  # Exibirá: "Valor formatado: 42.57"
print("Nome: %s, Idade: %d" % (nome, idade))


# Imprimindo com f-strings
produto = "Maçãs"
quantidade = 10
print(f"Comprei {quantidade} {produto} hoje.")

# Imprimindo múltiplas linhas
mensagem = """Esta é uma mensagem
com múltiplas linhas."""
print(mensagem)