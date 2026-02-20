import random

# 1 - Escolhe um nome aleatório da lista
jogadores = ["Paulo", "Murilo", "Daniel", "Ari", "Luciano", "Rogério", "Vinicius", "José", "Flavio"]
print(random.choice(jogadores))

# 2 - Gera número aleatório entre um intervalo de valores
alea = random.randint(5, 15)
print (alea)

# 3 - Escolhe caracter aleatório de uma string
nome = "Technology"
alea2 = random.choice(nome)
print(alea2)

# 4 - Escolhe mais de um valor aleatório (Random)
# random.sample(sequencia.tamanho)
print(random.sample(jogadores, 2))
print(random.sample(jogadores, 4))