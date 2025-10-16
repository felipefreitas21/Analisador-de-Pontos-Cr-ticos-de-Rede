import networkx as nx
import matplotlib.pyplot as plt


def ler_arquivo(arquivo):
    with open(arquivo, "r", encoding="UTF-8") as arq:
        linhas = [linha.strip() for linha in arq if linha.strip()] 

        tipo = linhas[0] 
        arestas = [tuple(linha.split(" ")) for linha in linhas [1:]] 

        return tipo, arestas



def construir_grafo(arestas, evitar_duplicatas=True): 
    if evitar_duplicatas: 
        grafo = {}
        for u, v in arestas: 
            grafo.setdefault(u, set()).add(v)
            grafo.setdefault(v, set()).add(u)
        return {k: sorted(list(v)) for k, v in grafo.items()} 
    else:
        grafo = {} 
        for u, v in arestas: 
            grafo.setdefault(u, list()).append(v)
            grafo.setdefault(v, list()).append(u)
        return grafo
    


def imprimir_listadj(grafo):
    print("Lista de Adjacência")
    separador = ", "
    for x, y in grafo.items():
        print(x, "->", separador.join(y))


 
def identificar_criticos(grafo):
    tempo = 0  
    visitado = {v: False for v in grafo}
    disc = {v: float('inf') for v in grafo}
    pai = {v: None for v in grafo}
    low = {v: float('inf') for v in grafo}
    articulacoes = set()

    def dfs(u):
        nonlocal tempo
        visitado[u] = True
        disc[u] = low[u] = tempo
        tempo += 1
        filhos = 0

        for v in grafo[u]:
            if not visitado[v]:
                pai[v] = u
                filhos += 1
                dfs(v) 

                low[u] = min(low[u], low[v])

                if pai[u] is None and filhos > 1:
                    articulacoes.add(u)

                if pai[u] is not None and low[v] >= disc[u]:
                    articulacoes.add(u)

            elif v != pai[u]:
                low[u] = min(low[u], disc[v])

    for vertice in grafo:
        if not visitado[vertice]:
            dfs(vertice)

    return sorted(list(articulacoes))


def remover_criticos(grafo, vertice):
    if vertice in grafo:
        copia = grafo.copy() 
        copia.pop(vertice)
        for x, vizinhos in copia.items():
            for y in vizinhos:
                if y == vertice:
                    vizinhos.remove(y)
        
        return copia
    else:
        return False



def plotar_grafo(grafo): 
    G = nx.Graph() 

    for u, adjacentes in grafo.items():
        for v in adjacentes: 
            G.add_edges_from([(u, v)])
    
    nx.draw(
        G,                         
        with_labels = True,
        font_size = 10,             
        node_color = "lightblue",   
        edge_color = "gray",        
        node_size = 600         
    )

    print("Gerando Grafo...")

    plt.show()

def plotar_grafo_criticos(grafo, criticos):
    G = nx.Graph() 
    for u, adjacentes in grafo.items():
        for v in adjacentes: 
            G.add_edges_from([(u, v)])

    cores = []
    for n in G.nodes():
        if criticos and n in criticos:
            cores.append("red")
        else:
            cores.append("lightblue")
    
    nx.draw(
        G,                          
        with_labels = True,
        font_size = 10,             
        node_color = cores ,        
        edge_color = "gray",        
        node_size = 600    
    )
    
    print("Gerando Grafo...")
    plt.show()

def listar_arestas(arestas):
    print("Arestas: ")
    for u, v in arestas:
        print(f"({u}, {v})")

def calcular_grau(grafo, vertice):
    if vertice in grafo.keys():
        print(f"{vertice} tem grau {len(grafo.get(vertice))}")
    else:
        print("Informe um vértice que exista no grafo.")

def listar_vizinhos(grafo, vertice):
    if vertice in grafo.keys():
        print(f"Vizinhos de {vertice}: {grafo.get(vertice)}")
    else:
        print("Informe um vértice que exista no grafo.")

def ver_adj(grafo, vertice1, vertice2):
     if vertice1 in grafo.get(vertice2):
        return True
     if vertice2 in grafo.get(vertice1):
         return True
     else:
         return False
