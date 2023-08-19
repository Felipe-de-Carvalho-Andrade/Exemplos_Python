class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

class profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    
    def info_profissional(self):
        return f"Sou uma {self.profissao}."

class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
    
    def depositar(self, valor):
        self._saldo += valor
    
    def obter_saldo(self):
        return self._saldo

# Criando objetos
pessoa1 = Pessoa("Bia", 30)
pessoa2 = Pessoa("Matheus", 25)

profissional1 = profissional("Lucas", 21, "Dentinsta")

conta1 = ContaBancaria(1000)
conta1.depositar(500)

# Utilizando os objetos
print(pessoa1.nome)  
print(pessoa2.saudacao()) 

print(profissional1.info_profissional())  

print(conta1.obter_saldo())  
