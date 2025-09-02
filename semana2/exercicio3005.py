N = int(input())
resultados = []  # lista para guardar os resultados

for _ in range(N):
    valores = list(map(int, input().split()))
    a1, b1, c1, a2, b2, c2 = valores

    faces1 = [(a1, b1), (a1, c1), (b1, c1)]
    faces2 = [(a2, b2), (a2, c2), (b2, c2)]

    pode1sobre2 = False
    pode2sobre1 = False

    for f1 in faces1:
        for f2 in faces2:
            if (f1[0] < f2[0] and f1[1] < f2[1]) or (f1[0] < f2[1] and f1[1] < f2[0]):
                pode1sobre2 = True
                break
        if pode1sobre2:
            break
    
    for f2 in faces2:
        for f1 in faces1:
            if (f2[0] < f1[0] and f2[1] < f1[1]) or (f2[0] < f1[1] and f2[1] < f1[0]):
                pode2sobre1 = True
                break
        if pode2sobre1:
            break

    if pode1sobre2 and pode2sobre1:
        resultados.append(3)
    elif pode1sobre2:
        resultados.append(1)
    elif pode2sobre1:
        resultados.append(2)
    else:
        resultados.append(0)

for r in resultados:
    print(r)
