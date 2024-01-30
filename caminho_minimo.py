import heapq
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pyvis.network import Network
import webbrowser

# Representa o grafo usando listas de vértices e arestas
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'J2', 'K2', 'L2', 'M2', 'N2', 'O2', 'P2', 'Q2', 'R2', 'S2', 'T2', 'U2', 'V2', 'W2', 'X2', 'Y2', 'Z2',
            'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O', '0','S3','O3','P3','Q3','R3'] 

arestas = [('A', 'B', 6), ('A', 'C', 6), ('D', 'E', 2), ('C', 'E', 4), ('B', 'F', 6),('B','G', 4),('E','F',4),('F','H',4),('H','I',2),('I','G',4),
            ('I','J',2),('H','J',2),('J','K',4),('K','G',6),('K','L',6),('L','M',4),('M','V',10),('C','N',6),('N','O',2),('O','S3',2),('O','P',2),
            ('P','R',4),('P','F',8),('R','H',8),('R','S',6),('J','S',10),('S','T',2),('T','K',2),('T','U',4),('U','L',8),('U','V',2),('V','W',10),
            ('W','X',8),('V','Y',8),('U','Z',6),('T','A2',4),('S','B2',8),('R','C2',8),('R','D2',10),('O','F2',10),('N','G2',10),('G2','F2',2),('F2','E2',2),
            ('E2','D2',6),('D2','C2',6),('C2','B2',4),('B2','A2',2),('A2','Z',10),('Z','Y',4),('Y','X',4),('X','T2',6),('T2','S2',2),('S2','Y',6),('S2','R2',8),
            ('R2','Z',2),('R2','P2',10),('P2','A2',8),('P2','O2',6),('O2','B2',6),('O2','N2',6),('N2','C2',6),('P2','X2',6),('X2','W2',6),('W2','V2',6),('V2','U2',6),
            ('V2','S2',8),('U2','T2',8),('O3','P3',6),('P3','Q3',6),('Q3','R3',6),('O3','M3',8),('P3','L3',8),('Q3','K3',8),('R3','J3',8),
            ('M3','L3',6),('L3','K3',6),('K3','J3',6),('J3','I3',6),('I3','H3',6),('M3','N3',6),('N3','W2',8),
            ('L3','Y2',8),('K3','Z2',8),('J3','A3',8),('I3','B3',8),('H3','C3',8),('H3','G3',10),('X2','Y2',6),('Y2','Z2',6),
            ('Z2','A3',6),('A3','B3',6),('B3','C3',6),('C3','D3',2),('C3','E3',2),('E3','D3',2),('E3','G3',6),
            ('Y2','O2',8),('Z2','N2',8),('A3','M2',8),('M2','N2',8),('M2','D2',6),('D2','K2',6),('M2','L2',4),
            ('L2','K2',2),('K2','J2',2),('J2','L2',2),('D3','J2',10),('J2','I2',6),('G3','F3',10),('F3','I2',10),
            ('F3','H2',10),('H2','I2',6),('H2','G2',10),('H2','F2',8),('I2','E2',10),('L2','B3',10)]

# Função que retorna os vértices vizinhos a um vértice
def vizinhos(vertice):
    vizinhos = []
    for aresta in arestas:
        if aresta[0] == vertice:
            vizinhos.append(aresta[1])
        elif aresta[1] == vertice:
            vizinhos.append(aresta[0])
    return vizinhos

# Recupera o caminho a partir da lista de antecessores
def recupera_caminho(antecessores, V1, V2):
    caminho = [V2]
    atual = V2
    while atual != V1:
        atual = antecessores[vertices.index(atual)]
        caminho.insert(0, atual)
    return caminho

# Encontra o custo (ou peso) de uma aresta ligando dois vértices
def custo(V1, V2):
    for aresta in arestas:
        if aresta[0] == V1 and aresta[1] == V2:
            return aresta[2]
        elif aresta[1] == V1 and aresta[0] == V2:
            return aresta[2]

# Verifica se o vértice está na fronteira
def esta_na_fronteira(fronteira, vertice):
    for v in fronteira:
        if v[1] == vertice:
            return True
    return False

# Altera custo acumulado na fronteira
def altera_custo(fronteira, vertice, novo_custo):
    for v in fronteira:
        if v[1] == vertice:
            v[0] = novo_custo
            return fronteira

# Encontra um caminho qualquer entre dois vértices V1 e V2
def caminho(V1, V2):
    fronteira = []
    # lista de antecessores com o mesmo tamanho da lista de vértices
    antecessores = [None] * len(vertices)
    custos = [100000] * len(vertices)
    custos[vertices.index(V1)] = 0

    # Insere todos os vértices com seus custos no heap
    for v in vertices:
        heapq.heappush(fronteira, [custos[vertices.index(v)], v])

    while fronteira != []:
        visitando = heapq.heappop(fronteira)[1]
        if visitando == V2:
            return recupera_caminho(antecessores, V1, V2)
        viz = vizinhos(visitando)
        for v in viz:
            if esta_na_fronteira(fronteira, v):
                novo_custo = custos[vertices.index(visitando)] + custo(visitando, v)
                if novo_custo < custos[vertices.index(v)]:
                    custos[vertices.index(v)] = novo_custo
                    antecessores[vertices.index(v)] = visitando
                    altera_custo(fronteira, v, novo_custo)
                    # Atualiza o heap
                    heapq.heapify(fronteira)

    caminho_vertices = recupera_caminho(antecessores, V1, V2)
    caminho_arestas = [(caminho_vertices[i], caminho_vertices[i+1]) for i in range(len(caminho_vertices)-1)]
    return caminho_arestas
# Função para imprimir o caminho mínimo
def imprimir_caminho_minimo(origem, destino, caminho):
    print(f'Caminho mínimo entre {origem} e {destino}: {caminho}')

# Função para imprimir a matriz de adjacência do grafo
def imprimir_matriz_adjacencia():
    matriz = [[0] * len(vertices) for _ in range(len(vertices))]
    for aresta in arestas:
        i, j, peso = vertices.index(aresta[0]), vertices.index(aresta[1]), aresta[2]
        matriz[i][j] = peso
        matriz[j][i] = peso
    print('Matriz de Adjacência:')
    for linha in matriz:
        print(linha)

# Função para verificar se o grafo é conexo
def eh_conexo():
    visitados = set()

    def dfs(vertice):
        visitados.add(vertice)
        for vizinho in vizinhos(vertice):
            if vizinho not in visitados:
                dfs(vizinho)

    dfs(vertices[0])
    return len(visitados) == len(vertices)

# Função para criar uma interface gráfica
# Função para criar uma interface gráfica
def criar_interface_grafica():
    def encontrar_caminho():
        origem = origem_var.get()
        destino = destino_var.get()
        if not origem or not destino:
            messagebox.showinfo("Aviso", "Por favor, preencha ambos os vértices de origem e destino.")
            return
        resultado = caminho(origem, destino)
        caminho_str.set(f'Caminho: {resultado}')

    def desenhar_grafo():
        origem = origem_var.get()
        destino = destino_var.get()

        # Crie um objeto Network do pyvis
        grafo = Network(notebook=True, width=800, height=600)

        # Adicione arestas e vértices ao grafo
        for v1, v2, peso in arestas:
            grafo.add_node(v1, label=v1)
            grafo.add_node(v2, label=v2)
            
            # Ajuste da largura com base no peso da aresta
            grafo.add_edge(v1, v2, title=str(peso), width=peso, color="red")

        # Exiba o grafo no notebook ou em uma nova janela, como preferir
        grafo.show("grafo.html")
        webbrowser.open("grafo.html", new=2)




    # Criação da janela principal
    janela = tk.Tk()
    janela.title('Encontrar Caminho Mínimo')

    # Componentes da interface
    origem_var = tk.StringVar()
    destino_var = tk.StringVar()
    caminho_str = tk.StringVar()

    ttk.Label(janela, text='Origem:').grid(row=0, column=0, padx=10, pady=10)
    ttk.Entry(janela, textvariable=origem_var).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(janela, text='Destino:').grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(janela, textvariable=destino_var).grid(row=1, column=1, padx=10, pady=10)

    ttk.Button(janela, text='Encontrar Caminho', command=encontrar_caminho).grid(row=2, column=0, columnspan=2, pady=10)

    ttk.Label(janela, textvariable=caminho_str).grid(row=3, column=0, columnspan=2, pady=10)

    # Adicione a visualização do grafo usando pyvis
    ttk.Button(janela, text='Mostrar Grafo', command=desenhar_grafo).grid(row=4, column=0, columnspan=2, pady=10)

    # Executa o loop principal da interface
    janela.mainloop()


# Imprime informações do grafo
print(f'O grafo é conexo: {eh_conexo()}')

# Imprime caminhos mínimos
criar_interface_grafica()