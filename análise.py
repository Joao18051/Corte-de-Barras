import random
import time

def corteBarrasAux(Precos, n):
    Resultados = [0] *len(Precos)
    Cortes = [0] *len(Precos)
    corteBarrasRec(Precos, Resultados, n, Cortes)
    print("Valor máximo: ", Resultados[n])
    print("Primeiro corte: ", Cortes[n])

    return Resultados, Cortes

def corteBarrasRec(Precos, Resultados, n, Cortes):
    if Resultados[n] != 0:
        return Resultados[n]
    
    if n == 1:
        Resultados[n] = Precos[n]
        Cortes[n] = n
        return Resultados[n]
    
    lucroMax = Precos[n]
    melhorCorte = 0

    for i in range(1, n-1):
        lucro = Precos[i] +corteBarrasRec(Precos, Resultados, n -i, Cortes)

        if lucro > lucroMax:
            lucroMax = lucro
            melhorCorte = i

    Resultados[n] = lucroMax
    Cortes[n] = melhorCorte

    return Resultados[n]

def corteBarrasIte(Precos, n):
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

    print("Valor máximo: ", resultados[n])
    print("Primeiro corte: ", cortes[n])
    return resultados, cortes

def criarEntrada(tam):
    Precos = [0]
    while len(Precos) < tam:
        Precos.append(random.randint(1, tam *10))

    Precos.sort()
    return Precos

tempoRec = []
tempoIte = []
for i in range(0, 1000):
    tam = 100
    Precos = criarEntrada(tam)
    #Para testes
    #Precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    inicio = time.perf_counter()
    corteBarrasAux(Precos, 6)
    fim = time.perf_counter()

    # Tempo em microsegundos
    tempoRec.append((fim - inicio) * (10**6))
    print()


    inicioIte = time.perf_counter()
    corteBarrasIte(Precos, 6)
    fimIte = time.perf_counter()
    # Tempo em microsegundos
    tempoIte.append((fimIte - inicioIte) * (10**6))
    print()

tRecursivo = 0
for i in range(len(tempoRec)):
    tRecursivo += tempoRec[i]

tRecursivo = tRecursivo/1000
print("Tempo médio Recursivo: %.2f" % (tRecursivo))
print()

tIterativo = 0
for i in range(len(tempoIte)):
    tIterativo += tempoIte[i]

tIterativo = tIterativo/1000
print("Tempo médio Iterativo: %.2f" % (tIterativo))
print()
