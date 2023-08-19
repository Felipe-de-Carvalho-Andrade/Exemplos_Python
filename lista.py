# Criando uma lista
animals = ["elefante", "girafa", "leão", "tigre", "macaco"]

# Adicionando elementos no final da lista
animals.append("zebra")
animals.append("hipopótamo")
animals.append("rinoceronte")

# Imprimindo a lista
print(animals + "\n")

# Acessando um elemento da lista
first_animal = animals[0]

# Pegando o índice de um elemento
index = animals.index("girafa")

# Contando as ocorrências de um elemento
no_elephants = animals.count("elefante")

# Adicionando um elemento em uma posição específica da lista
animals.insert(2, "leopardo")

# Removendo um elemento da lista
animals.remove("girafa")

# Imprimindo a lista
print(animals + "\n")

# Remove um elemento de uma posição específica
# Se não passar argumento, remove o último elemento
animals.pop(4)
# Remove todos os elementos da lista em um certo intervalo
del animals[1:3]

# Imprimindo a lista
print(animals + "\n")

# Inverte a ordem dos elementos da lista
animals.reverse()

# Imprimindo a lista
print(animals + "\n")

# Ordena os elementos da lista alfabeticamente
animals.sort()

# Imprimindo a lista
print(animals + "\n")

# Remove todos os elementos da lista
animals.clear()

# Imprimindo a lista
print(animals + "\n")