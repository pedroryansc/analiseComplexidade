# Implementação original do problema

def existeCaminho(grafo, k):
    vertices = grafo[0]

    for verticeAtual in vertices: # O(n)
        verticesVisitados = [verticeAtual]

        if(busca(grafo, verticeAtual, k, verticesVisitados)): # O(n^n)
            return True
    
    return False

def busca(grafo, verticeAtual, k, verticesVisitados):
    if(len(verticesVisitados) == k): # O(1)
        return True
    
    vertices = grafo[0]
    arestas = grafo[1]

    for vizinho in vertices: # O(n)
        if(arestas[verticeAtual][vizinho]): #O(1)
            if(vizinho not in verticesVisitados): # O(1)
                # A partir que os vizinhos são visitados, os passos a seguir são executados cada vez
                # menos. Contudo, essa diferença não é significativa no tempo de execução exponencial.
                
                verticesVisitados.append(vizinho) # O(1)
                
                if(busca(grafo, vizinho, k, verticesVisitados)): # O(n^n)
                    return True
                
                verticesVisitados.remove(vizinho) # O(1)

    return False

# Complexidade do algoritmo -> O(n^n), ou seja, é um algoritmo exponencial

# Teste do algoritmo original

vertices = [0, 1, 2]
arestas = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

grafo = [vertices, arestas]

k = 3

resultado_original = existeCaminho(grafo, k)

print(f"Algoritmo original: {resultado_original}")

# ------------------------------------------------------

# Implementação otimizada do problema

def existeCaminho_otimizado(grafo, k):
    vertices = grafo[0]
    memoizacao = {}

    for verticeAtual in vertices: # O(n)
        bitmaskVisitados = 1 << verticeAtual # Começa apenas com o vértice atual como visitado

        if(busca_otimizada(grafo, verticeAtual, k, bitmaskVisitados, memoizacao, 1)): # O(2^n)
            return True
        
    return False

def busca_otimizada(grafo, verticeAtual, k, bitmaskVisitados, memoizacao, contador):
    # Se a quantidade k de vértices foi visitada, o caminho existe
    if(contador == k): # O(1)
        return True
    
    # Se um caminho já foi verificado, o resultado salvo é retornado
    if((verticeAtual, bitmaskVisitados) in memoizacao): # O(1)
        return memoizacao[(verticeAtual, bitmaskVisitados)]
    
    vertices = grafo[0]
    arestas = grafo[1]

    for vizinho in vertices: # O(n), mas, graças à máscara de bits e à memoização,
                                    # os passos a seguir são executados cada vez menos.
        if(arestas[verticeAtual][vizinho]): # O(1)
            if not (bitmaskVisitados & (1 << vizinho)): # Se o vizinho ainda não foi visitado
                # O vizinho é marcado como visitado na máscara de bits
                novaBitmaskVisitados = bitmaskVisitados | (1 << vizinho)

                if(busca_otimizada(grafo, vizinho, k, novaBitmaskVisitados, memoizacao, contador + 1)): # O(2^n)
                    return True
                
    memoizacao[(verticeAtual, bitmaskVisitados)] = False
    return False

# Complexidade do algoritmo -> O(n * 2^n)

# Teste do algoritmo otimizado

resultado_otimizado = existeCaminho_otimizado(grafo, k)

print(f"Algoritmo otimizado: {resultado_otimizado}")

# ------------------------------------------------------

# Gráficos

import time, matplotlib.pyplot as plt

def gerarVertices(quantVertices):
    vertices = [i for i in range(quantVertices)]

    return vertices

def gerarArestas(quantVertices):
    arestas = [[1 for _ in range(quantVertices)] for _ in range(quantVertices)]

    for i in range(quantVertices):
        for j in range(quantVertices):
            if(i == j):
                arestas[i][j] = arestas[j][i] = 0

    return arestas

def calcularTemposExecucao(intervaloVertices, algoritmo):
    temposExecucao = []
    
    for quantVertices in intervaloVertices:
        vertices = gerarVertices(quantVertices)
        arestas = gerarArestas(quantVertices)

        grafo = [vertices, arestas]

        k = quantVertices + 1

        if(algoritmo == 1):
            inicio = time.time()
            existeCaminho(grafo, k)
            fim = time.time()
        else:
            inicio = time.time()
            existeCaminho_otimizado(grafo, k)
            fim = time.time()

        tempo = fim - inicio

        temposExecucao.append(tempo)

    return temposExecucao

def gerarGrafico(intervaloVertices, tempos, titulo):
    plt.plot(intervaloVertices, tempos)

    plt.title(titulo)
    plt.xlabel("Quantidade de vértices")
    plt.ylabel("Tempo de execução (s)")

    plt.show()

intervalo_original = [i for i in range(2, 12)]
intervalo_otimizado = [i for i in range(2, 22)]

tempo_original = calcularTemposExecucao(intervalo_original, 1)
print(f"Tempos de execução do algoritmo original: {tempo_original}")

tempo_otimizado = calcularTemposExecucao(intervalo_otimizado, 2)
print(f"Tempos de execução do algoritmo otimizado: {tempo_otimizado}")

# Gráfico do desempenho do algoritmo original

gerarGrafico(intervalo_original, tempo_original, "Desempenho do algoritmo original")

# Gráfico do desempenho do algoritmo otimizado

gerarGrafico(intervalo_otimizado, tempo_otimizado, "Desempenho do algoritmo otimizado")