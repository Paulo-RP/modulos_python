import math

# 1 - Acessando o número PI
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Utilizando Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondamento de números para cima ou para baixo
num = 18.3
print(math.ceil(num)) # Arredondamento para cima
print(math.floor(num)) # Arredondamento para baixo

# 4 - Fatorial de um número
num2 = 5
print(math.factorial(num2))

# 5 - Potência de números
num3 = int(input("Digite um número:\n"))
print(f"A potência do número {num2}, é: {math.pow(num2, num3)}")

# 6 - Raiz quadrada
print(f"A raiz quadrada de {num3}, é: {math.sqrt(num3)}")

# 7 - MDC
mdc = math.gcd(20, 100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))