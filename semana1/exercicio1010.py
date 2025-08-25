Entrada1 = input().split()
codigo1 = int(Entrada1[0])
quantidade1 = int(Entrada1[1])
valor1 = float(Entrada1[2])
total = quantidade1 * valor1

Entrada2 = input().split()
codigo2 = int(Entrada2[0])
quantidade2 = int(Entrada2[1])
valor2 = float(Entrada2[2])
total += quantidade2 * valor2
print(f"VALOR A PAGAR: R$ {total:.2f}")