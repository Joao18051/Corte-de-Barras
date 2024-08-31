import time
import random

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

def criarEntrada(tam):
    Precos = [0]
    while len(Precos) < tam:
        Precos.append(random.randint(1, tam *10))

    Precos.sort()
    return Precos

t = 0
for i in range(0, 1000):
    tam = 100
    #Precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    Precos = criarEntrada(tam)
    n = 5

    inicio = time.perf_counter()
    print(corteBarras(Precos, n))
    fim = time.perf_counter()

    tempo_execucao = (fim - inicio) * (10**6)
    t += tempo_execucao
    print(f"Tempo de execução: {tempo_execucao:.2f} microssegundos")

t = t/1000
print("Tempo médio: %.2f" % (t))
print()