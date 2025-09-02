def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        fila = list(map(int, input().split()))
        ordenada = sorted(fila, reverse=True)
        contador = sum(1 for i in range(M) if fila[i] == ordenada[i])
        print(contador)

if __name__ == "__main__":
    main()
