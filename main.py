import numpy as np
import tkinter as tk

# FUNÇÃO RESPONSÁVEL POR CARREGAR O GRAFO.TXT NO CÓDIGO E IMPRIMIR
        
def carregarMatriz():
    # ler todas as linhas e salva em uma lista
    arquivo = open('grafo.txt', 'r')

    # transforma cada linha do grafo.txt em uma lista
    lista = arquivo.readlines()

    # criamos um laço que percorre todo o txt e usamos a função "split()" para
    # dividir as strings de cada linha do txt e atribuímos a uma variável chamada "linha",
    # além disso, verificamos a quantidade de vértices do grafo.txt utilizando o valor do índice [0]
    # da primeira linha. Com o auxílio do NumPy, criamos uma matriz de adjacência quadrática
    # que terá como dimensões o valor de índice[0] com valores 0.

    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])
            matrizADJ = np.zeros((N, N), dtype=np.int64)
        # após isso, ele usa os índices [0] e [1] de cada linha da lista para atribuir
        # o número 1 na matriz de adjacência
        else:
            matrizADJ[int(linha[0])-1, int(linha[1])-1] = 1

    arquivo.close()
    return N, matrizADJ

def ordenar_vertices():
    [N, matrizADJ] = carregarMatriz()
    graus = np.sum(matrizADJ, axis=1)
    vertices_ordenados = np.argsort(graus)[::-1] + 1
    return vertices_ordenados.tolist()


def desenhar_grafo():
    [N, matrizADJ] = carregarMatriz()
    janela = tk.Tk()
    janela.title("Grafo")

    canvas = tk.Canvas(janela, width=400, height=400)
    canvas.pack()

    coordenadas = []
    raio = 150
    centro_x = 200
    centro_y = 200
    angulo = 2 * np.pi / N

    for i in range(N):
        x = centro_x + raio * np.cos(i * angulo)
        y = centro_y + raio * np.sin(i * angulo)
        coordenadas.append((x, y))
    for i in range(N):
        for j in range(N):
            if matrizADJ[i, j] == 1:
                x1, y1 = coordenadas[i]
                x2, y2 = coordenadas[j]
                canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, arrowshape=(30, 60, 10))

    raio_vertice = 20
    for i, (x, y) in enumerate(coordenadas):
        canvas.create_oval(x - raio_vertice, y - raio_vertice, x + raio_vertice, y + raio_vertice, fill='white')
        canvas.create_text(x, y, text=str(i + 1), fill='green', font=('Arial', 12, 'bold'))
    janela.mainloop()

[N, matrizADJ] = carregarMatriz()

v = ordenar_vertices()
cor = [""] * N
d = [0] * N
f = [0] * N
mark = 0

def DFS():
    global cor, d, f, mark
    for u in v:
        cor[u-1] = "branco"
    for u in v:
        if cor[u-1] == "branco":
            DFS_visit(u)

def DFS_visit(u):
    global cor, d, f, mark
    cor[u-1] = "cinza"
    mark += 1
    d[u-1] = mark
 
    for v in range(N):
        if matrizADJ[u-1, v] == 1 and cor[v] == "branco":
            print(u, "---->", v+1,"ARESTA DE ÁRVORE")
            DFS_visit(v+1)
        elif matrizADJ[u-1, v] == 1 and cor[v] == "cinza":
           
            print(u, "---->", v+1,"ARESTA DE RETORNO")
        elif matrizADJ[u-1, v] == 1 and cor[v] == "preto":
           
            print(u, "---->", v+1,"ARESTA DE AVANÇO OU CRUZAMENTO")
    cor[u-1] = "preto"
    mark += 1
    f[u-1] = mark
 



desenhar_grafo()