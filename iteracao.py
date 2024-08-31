import time

def corteBarras(Precos, n):
    #O primeiro é 0 para trabalhar com índices de 1 à n
    resultados = [0] * (n + 1)
    cortes = [0] * (n + 1) 

    for j in range(1, n + 1):
        lucroMax = -1 
        melhorCorte = j
        
        for i in range(1, j +1):
            lucroAtual = Precos[i - 1] + resultados[j -i]

            if lucroAtual > lucroMax:
                lucroMax = lucroAtual
                melhorCorte = i
        
        resultados[j] = lucroMax
        cortes[j] = melhorCorte

    return resultados, cortes

Precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 5

inicio = time.perf_counter()
print(corteBarras(Precos, n))
fim = time.perf_counter()

tempo_execucao = (fim - inicio) * (10**6)
print(f"Tempo de execução: {tempo_execucao:.2f} microssegundos")