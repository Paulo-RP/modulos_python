from collections import Counter, namedtuple, deque
from operator import itemgetter

line = "-"

# 01 - Lista compras (Para contagem)
list_compras = ["Macarrão", "Banana", "Miojo", "Café", "Banana", "Arroz", "Feijão", "Banana", "Macarrão", "Refrigerante", "Banana", "Uva"]
print(list_compras)
print(Counter(list_compras))

print(line*70)

# 02 - Nomeando Tupla
games = namedtuple('games', ['nome', 'preco', 'nota'])
g1 = games("FIFA 26", 90.50, 8.5)
g2 = games("SKYRIM V", 115.50, 9.5)
print(g1)
print(g2)

print(line*70)

# 03 - Ordenando dicionários
estudantes = {"Paulo": 31, "Bruna": 29, "Sebastian": 2, "Floki": 4 }
ordem = sorted(estudantes.items(), key = itemgetter(0)) # Se colocar o parametro no itemgetter (0) irá chamar por chaves, se for (1) organiza por ordem númerica
print(ordem)

print(line*70)

# 4 - Acrescentando valores a fila em ambas extermidades com deque
deq = deque([20, 40, 80, 120, 140])
deq.appendleft(5) # Acrescentando a esquerda o valor
print(deq)
deq.append(160) # Acrescenta na outra extremidade no caso a direita o valor
deq.popleft()
deq.pop
print(deq)
