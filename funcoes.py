# Função built-in: print()
def print_hello():
    print("Olá, mundo!")

# Função user-defined: saudacao()
def saudacao(nome):
    return f"Olá, {nome}!"

# Função que retorna valor: dobro()
def dobro(numero):
    return numero * 2

# Função com número variável de argumentos: soma_variavel()
def soma_variavel(*args):
    total = 0
    for num in args:
        total += num
    return total

# Função recursiva: fatorial()
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Chamada das funções
print_hello()

print(saudacao("Alice"))

num = 5
dobro_num = dobro(num)
print(f"O dobro de {num} é {dobro_num}")

soma = soma_variavel(1, 2, 3, 4, 5)
print(f"A soma dos números é {soma}")

numero_fatorial = 5
fatorial_numero = fatorial(numero_fatorial)
print(f"O fatorial de {numero_fatorial} é {fatorial_numero}")
