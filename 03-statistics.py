import statistics

list_mean = [1, 2, 3, 4, 5, 6]
list_median01 = [1, 2, 5, 6, 10]
list_median02 = [1, 2, 4, 6, 8, 10]
list_mode = [1, 2, 4, 6, 8, 10, 1, 2, 5, 6, 10, 1, 2, 3, 4, 5, 6 ]

# 1 - Média de uma lista
print(f"A média é: {statistics.mean(list_mean)}")

# 2 - Mediana de uma lista
print(statistics.median(list_median01))
print(statistics.median(list_median02))

# 3 - Aplicando o mode, que resulta no número que mais se repete
print(statistics.mode(list_mode))

# 4 - Desvio padrão
'''
Quanto mais próximo de 0 for o desvio padrão, 
significa que os dados do conjunto estão menos dispersos

'''
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))