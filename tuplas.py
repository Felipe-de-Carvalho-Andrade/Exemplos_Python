# Fomas de se criar Tuplas
tupla1 = (1, 2, 3, 4, 5)  # Usando parênteses
tupla2 = 1, 2, 3, 4, 5  # Sem parênteses

lista = [10, 20, 30]
tupla3 = tuple(lista)  # Usando a função tuple()

tupla_vazia = ()  # Tupla vazia

tupla_um_elemento = (42,)  # Tupla de um elemento
tupla_um_elemento = "Felipe"  # Tupla de um elemento

tupla_pares = tuple(x for x in range(10) if x % 2 == 0) # Compreensão de tupla

# Acessar seus elementos
elemento = tupla2[2] # Através do índice
print(elemento)

a, b, c, d, e =  tupla1 # Através do Desempacotamento da Tupla
print(a, b, c, d)