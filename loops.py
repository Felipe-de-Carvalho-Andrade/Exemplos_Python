# Exemplo de uso de loops

# Usando um loop for para imprimir os números pares de 0 a 10
print("Números pares usando loop for:")
for numero in range(0, 11, 2):
    print(numero)

print("\n")

# Usando um loop while para calcular a soma dos primeiros números inteiros positivos
limite = 5
soma = 0
contador = 1

while contador <= limite:
    soma += contador
    contador += 1

print(f"A soma dos primeiros {limite} números inteiros positivos é {soma}")

# Exemplo de uso do loop for com uma lista
nomes = ["Alice", "Bob", "Charlie", "David", "Emily"]

print("Nomes usando loop for:")
for nome in nomes:
    print(nome)
    
# Exemplos de loops com break e continue

# Usando break para encontrar o primeiro múltiplo de 7 entre 1 e 100
print("Usando break para encontrar o primeiro múltiplo de 7:")
for numero in range(1, 101):
    if numero % 7 == 0:
        print(f"O primeiro múltiplo de 7 é: {numero}")
        break

print("\n")

# Usando continue para imprimir números pares entre 1 e 10
print("Usando continue para imprimir números pares:")
for numero in range(1, 11):
    if numero % 2 != 0:
        continue
    print(numero)
