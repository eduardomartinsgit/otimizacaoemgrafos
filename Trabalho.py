import json
    
class MatrizAdjGrafo:

        def lerGrafoJSON(self, nomeArquivo):
                with open(nomeArquivo) as json_file:
                        grafoJSON = json.load(json_file)
                        self.v = len(grafoJSON['vertices'])
                        self.e = len(grafoJSON['arestas'])

                        for i in range(self.v): #Criação da matriz e inicializando com 0
                                self.m.append(self.v * [0])                        
                        return grafoJSON
        def __init__(self):
                self.v = 0
                self.e = 0
                self.m = []


        def imprimirGrafo(self,grafo):
                for i in range(self.v):
                        for j in range(self.v):
                                print(grafo[i][j], end=' ') # end=' ' para o print aparecer no console como uma matriz
                        print('')


        def inserirAresta(self, grafoJSON):
                arestas = grafoJSON['arestas']
                for i in range(0, len(arestas)):
                        print (arestas[i][0])
                        print (arestas[i][1])
                        self.m[int(arestas[i][0]) - 1][int(arestas[i][1]) - 1] = int(1)
                        self.m[int(arestas[i][1]) - 1][int(arestas[i][0]) - 1] = int(1)

        def removerAresta(self, linha, coluna):
                self.m[linha][coluna]=0
                self.m[coluna][linha]=0
                self.e= self.e - 1

#FIM DA MATRIZ DE ADJACENCIAS


class ListaAdjGrafo:
        def __init__(self):
                self.L = []
                self.v = None
                self.e = None

        def lerGrafoJSON(self, nomeArquivo):
                with open(nomeArquivo) as json_file:
                        grafoJSON = json.load(json_file)
                        self.v = len(grafoJSON['vertices'])
                        self.e = len(grafoJSON['arestas'])




# FIM DA LISTA DE ADJACENCIAS

grafo = MatrizAdjGrafo()
grafoJSON = grafo.lerGrafoJSON('grafo.txt')
grafo.inserirAresta(grafoJSON)
grafo.imprimirGrafo(grafo.m)
print ()
print ()
grafo.removerAresta(1,2)
grafo.imprimirGrafo(grafo.m)
