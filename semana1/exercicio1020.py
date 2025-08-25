idade = int(input())

anos = idade // 365
idade_restante = idade % 365
meses = idade_restante // 30
dias = idade_restante % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)") 