import re # Expressões regulares (Regular Expression)

line = '*'

text = "Giant Technology Solution - Uma empresa com soluções em tecnologia"
# 1 - Índice inicial e final de palavras
# O r significa uma raw string (string bruta)
match = re.search(r'Uma empresa', text)
print(f"Índice inicial: {match.start()}")
print(f"Índice final: {match.end()}")

# 2 - Buscando o Índice que possuí o ponto
site = 'https://giant-tech-solution.web.app'
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase
pattern = "[g-h]"
result = re.findall(pattern, text)
print(result)

# 4 - Verificando o ínicio de uma string
rule = r'^O'
phrases = ['A casa está suja','Vamos passear no parque', 'O rato roeu a roupa do rei de roma']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não Corresponde: {f}")

print(line*70)

# 5 - Verificando o final de uma string
rule_end = r'[!]$'
phrases2 = ['A casa está suja?', 'O rato roeu a roupa do rei de roma$', 'Vamos passear no parque!']
for p in phrases2:
    if re.search(rule_end, p):
        print(f"Sim, corresponde: {p}")
    else:
        print(f"Não, corresponde: {p}")