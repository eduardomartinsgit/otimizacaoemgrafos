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
                        self.L = [None]*(self.v+1)
                        for i in range(self.v+1): #Criação da lista e inicializando com None
                                self.L[i]=ListaAdjGrafo.NoAresta()
                return grafoJSON
                                
        class NoAresta(object): #CONFORME O SLIDE 
                def __init__(self):
                        self.viz = None
                        self.e = None
                        self.prox = None

        class Aresta(object): #CONFORME O SLIDE 
                def __init__(self):
                        self.explorado = None

        def inserir(self,lista,vizinho,novaAresta): #METODO AUXILIAR PARA INSERÇÃO DE UMA NOVA ARESTA 
                novoNo = ListaAdjGrafo.NoAresta()
                novoNo.viz = vizinho
                novoNo.prox = lista
                novoNo.e = novaAresta
                lista = novoNo
                return lista


        def inserirAresta(self, grafoJSON):
                arestas = grafoJSON['arestas']
                for i in range(0, len(arestas)):
                        novaAresta = ListaAdjGrafo.Aresta()
                        u = int(arestas[i][0])
                        v = int(arestas[i][1])
                        self.L[u]=self.inserir(self.L[u],v,novaAresta)
                        self.L[v]=self.inserir(self.L[v],u,novaAresta)


        def imprimirVizinhos(self):
                for i in range(self.e):
                        print(self.L[i].viz)

# FIM DA LISTA DE ADJACENCIAS

grafo = MatrizAdjGrafo()
grafoJSON = grafo.lerGrafoJSON('grafo.txt')
grafo.inserirAresta(grafoJSON)
#grafo.imprimirGrafo(grafo.m)
#print ()
#print ()
grafo.removerAresta(1,2)
#grafo.imprimirGrafo(grafo.m)



graph = ListaAdjGrafo()
grafoJSON = graph.lerGrafoJSON('grafo.txt')
graph.inserirAresta(grafoJSON)
graph.imprimirVizinhos()
