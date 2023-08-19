# Criando um dicionário de informações sobre uma pessoa
pessoa = {
    "Nome": "Lucas",
    "Idade": 22,
    "Profissão": "Engenheiro",
    "Cidade": "São Paulo"
}

# Acessando valores do dicionário
nome = pessoa["nome"]
idade = pessoa["idade"]
print("Nome: " + nome + "\n")
print("Idade: " + idade + "\n")

# Modificando valores no dicionário
pessoa["profissão"] = "Cientista da Computação"
print("Nova Profissão: " + pessoa["profissão"] + "\n")

# Adicionando um novo par chave-valor
pessoa["email"] = "lucas@gmail.com"

# Verificando a existência de uma chave no dicionário
if "cidade" in pessoa:
    print("Cidade:", pessoa["cidade"])
print("\n")

# Iterando através das chaves e valores do dicionário
print("Informações da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
print("\n")

# Removendo um par chave-valor do dicionário
if "email" in pessoa:
    del pessoa["email"]

# Tamanho do dicionário
num_campos = len(pessoa)
print(f"Total de campos: {num_campos}\n")

print("Informações da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
print("\n")