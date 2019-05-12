import json
    
class MatrizAdjGrafo:

        def lerGrafoJSON(self, nomeArquivo):
                with open(nomeArquivo) as json_file:
                        grafoJSON = json.load(json_file)
                        self.v = len(grafoJSON['vertices'])
                        self.e = len(grafoJSON['arestas'])
                        print (grafoJSON['nome'])
                        print (self.v)
                        print (self.e)
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


#FIM DA MATRIZ DE ADJACENCIAS

grafoMatriz = MatrizAdjGrafo()
grafoMatriz.lerGrafoJSON('grafo.txt')
grafoMatriz.imprimirGrafo(grafoMatriz.m)
