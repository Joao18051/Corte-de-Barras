import random
import time

def corteBarrasAux(Precos, n):
    Resultados = [0] *len(Precos)
    Cortes = [0] *len(Precos)
    corteBarras(Precos, Resultados, n, Cortes)
    print("Valor máximo: ", Resultados[n])
    print("Corte: ", Cortes[n])

    #while True:
        #print("Corte: ", Cortes[n])
        #n = Cortes[n]
        #if n == 0:
            #break

def corteBarras(Precos, Resultados, n, Cortes):
    if Resultados[n] != 0:
        return Resultados[n]
    
    if n == 1:
        Resultados[n] = Precos[n]
        Cortes[n] = n
        return Resultados[n]
    
    lucroMax = Precos[n]
    melhorCorte = 0

    for i in range(1, n-1):
        lucro = Precos[i] +corteBarras(Precos, Resultados, n -i, Cortes)

        if lucro > lucroMax:
            lucroMax = lucro
            melhorCorte = i

    Resultados[n] = lucroMax
    Cortes[n] = melhorCorte

    return Resultados[n]

def criarEntrada(tam):
    Precos = [0]
    while len(Precos) < tam:
        Precos.append(random.randint(1, tam *10))

    Precos.sort()
    return Precos

tempo = []
for i in range(0, 1000):
    tam = 30
    Precos = criarEntrada(tam)
    #Para testes
    #Precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    inicio = time.perf_counter()
    corteBarrasAux(Precos, 6)
    fim = time.perf_counter()

    # Tempo em microsegundos
    tempo.append((fim - inicio) * (10**6))
    print("Tempo entrada 10: %.2f" % (tempo[i]))
    print()

t = 0
for i in range(len(tempo)):
    t += tempo[i]

t = t/1000
print("Tempo médio: %.2f" % (t))
print()
