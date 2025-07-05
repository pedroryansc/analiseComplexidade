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
            if(vizinho not in verticesVisitados): # O(1) <- A partir que os vizinhos são visitados, esse passo é executado cada vez menos. 
                                                        # Contudo, essa diferença não é significativa no tempo de execução exponencial.
                verticesVisitados.append(vizinho) # O(1)
                
                if(busca(grafo, vizinho, k, verticesVisitados)): # O(n^n)
                    return True
                
                verticesVisitados.remove(vizinho) # O(1)

    return False

# Complexidade do algoritmo -> O(n^n), ou seja, é um algoritmo exponencial

# Teste do algoritmo original

vertices = [0, 1, 2, 3, 4, 5]
arestas = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

grafo = [vertices, arestas]

resultado_original = existeCaminho(grafo, 6)

print(f"Algoritmo original: {resultado_original}")

# ------------------------------------------------------

# Implementação otimizada do problema

def existeCaminho_otimizado(grafo, k):
    vertices = grafo[0]
    memoizacao = {} # Dicionário para memoização

    for verticeAtual in vertices:
        if(busca_otimizada(grafo, verticeAtual, k, 1 << verticeAtual, memoizacao, 1)): # Começa com apenas o vértice atual como visitado
            return True
        
    return False

def busca_otimizada(grafo, verticeAtual, k, bitmaskVisitados, memoizacao, contador):
    # Se a quantidade k de vértices foi visitada, o caminho existe
    if(contador == k):
        return True
    
    # Se um "subproblema" já foi resolvido, o resultado salvo é retornado
    if((verticeAtual, bitmaskVisitados) in memoizacao):
        return memoizacao[(verticeAtual, bitmaskVisitados)]
    
    vertices = grafo[0]
    arestas = grafo[1]

    # Para cada vizinho do vértice atual
    for vizinho in vertices:
        if(arestas[verticeAtual][vizinho]): # Se há uma aresta entre o vértice atual para o outro
            if not (bitmaskVisitados & (1 << vizinho)):
                if(busca_otimizada(grafo, vizinho, k, bitmaskVisitados | (1 << vizinho), memoizacao, contador + 1)): # Se o vizinho ainda não foi visitado
                    # O vizinho é visitado e é adicionado à máscara de bits
                    memoizacao[(verticeAtual, bitmaskVisitados)] = True
                    return True
                
    memoizacao[(verticeAtual, bitmaskVisitados)] = False
    return False

# Teste do algoritmo otimizado

resultado_otimizado = existeCaminho_otimizado(grafo, 6)

print(f"Algoritmo otimizado: {resultado_otimizado}")

# Criação aleatória de vértices e arestas

import random, time

def gerarVertices(quantVertices):
    vertices = [i for i in range(quantVertices)]

    return vertices

def gerarArestas(quantVertices):
    arestas = [[0 for _ in range(quantVertices)] for _ in range(quantVertices)]

    for i in range(quantVertices):
        for j in range(quantVertices):
            if(i != j):
                if(random.random() < 0.05):
                    arestas[i][j] = arestas[j][i] = 1

    return arestas

quantVertices = 10000

vertices = gerarVertices(quantVertices)
arestas = gerarArestas(quantVertices)

# print(arestas)

grafo = [vertices, arestas]

inicio = time.time()

print(inicio)

resultado_original = existeCaminho(grafo, 900)
fim = time.time()

print(fim)

tempo_original = fim - inicio

inicio = time.time()

print(inicio)

resultado_otimizado = existeCaminho_otimizado(grafo, 900)
fim = time.time()

print(fim)

tempo_otimizado = fim - inicio

print(f"Algoritmo original (com grafo aleatório): {resultado_original} - Tempo: {tempo_original}")
print(f"Algoritmo otimizado (com grafo aleatório): {resultado_otimizado} - Tempo: {tempo_otimizado}")

# Gráfico de crescimento no tempo de execução dos algoritmos