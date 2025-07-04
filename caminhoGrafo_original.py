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
                                                        # Contudo, essa diferença não é significativa na execução exponencial.
                verticesVisitados.append(vizinho) # O(1)
                
                if(busca(grafo, vizinho, k, verticesVisitados)): # O(n^n)
                    return True
                
                verticesVisitados.remove(vizinho) # O(1)

    return False

# Complexidade do algoritmo -> O(n^n), ou seja, é um algoritmo exponencial

# Teste do algoritmo

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

resultado = existeCaminho(grafo, 10)

print(resultado)

# Gráfico de crescimento no tempo de execução do algoritmo

import random

def gerarMatrizArestas(quantVertices):
    arestas = [[0 for _ in range(quantVertices)] for _ in range(quantVertices)]

    for i in range(quantVertices):
        for j in range(quantVertices):
            if(i != j):
                if(random.random() > 0.5):
                    arestas[i][j] = arestas[j][i] = 1

    return arestas