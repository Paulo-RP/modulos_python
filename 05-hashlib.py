import hashlib
line = "*"

#Hash é usado para criar dados criptográficos
# 1 - Verificar quais algoritmos estão disponiveis
print(hashlib.algorithms_available)

print(line*50)

# 2 - Verificar de acordo com o sistema operacional
print(hashlib.algorithms_guaranteed)

print(line*50)

# 3 - Depois de visualizado de acordo com o sistema operacional (S.O), utilizando o SHA256
algoritmo = hashlib.sha256()
print(algoritmo.digest())
msg = "Não fique em lágrimas ou se entristeça, o fluxo do tempo não para e não vai te esperar!".encode()
algoritmo.update(msg)
print(algoritmo.hexdigest())

print(line*50)

# 4 - Usando outro, o MD5
md5 = hashlib.md5()
md5.update(msg)
print(f"Mensagem Criptografada: {md5.hexdigest()}")