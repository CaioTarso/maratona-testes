import sys

dados = list(map(int, sys.stdin.read().split()))
n = dados[0]
numeros = dados[1:n+1]

pares = sorted([x for x in numeros if x % 2 == 0])
impares = sorted([x for x in numeros if x % 2 == 1], reverse=True)

for x in pares:
    print(x)
for x in impares:
    print(x)
