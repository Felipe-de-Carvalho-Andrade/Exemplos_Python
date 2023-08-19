# Criando um Set
frutas = {"maçã", "banana", "laranja", "laranja"}

# Adicionando elementos ao Set
frutas.add("uva")
frutas.add("maçã")
print(frutas + "\n")

# Removendo um elemento do Set
frutas.remove("banana")
print(frutas + "\n")

# Verificando a existência de um elemento no Set
if "laranja" in frutas:
    print("Laranja está no conjunto de frutas\n")

# Iterando através dos elementos do Set
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)
print("\n")

# Tamanho do Set
num_frutas = len(frutas)
print(f"Total de frutas: {num_frutas}")
print("\n")

# Criando um novo Set a partir de uma lista
outros_frutas = set(["pera", "abacaxi", "uva"])

# Realizando operações de conjuntos (união, interseção, diferença)
frutas_comuns = frutas.intersection(outros_frutas)
frutas_diferentes = frutas.difference(outros_frutas)
todas_as_frutas = frutas.union(outros_frutas)

print("Frutas em comum:", frutas_comuns + "\n")
print("Frutas diferentes:", frutas_diferentes + "\n")
print("Todas as frutas:", todas_as_frutas + "\n")