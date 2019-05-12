import json
    
class MatrizAdjGrafo:

        def lerGrafoJSON(self, nomeArquivo):
                with open(nomeArquivo) as json_file:
                        grafoJSON = json.load(json_file) 
                        print (grafoJSON)
        def __init__(self):
                self.v = 0
                self.e = 0
                self.m = []

#FIM DA MATRIZ DE ADJACENCIAS

grafoMatriz = MatrizAdjGrafo()
grafoMatriz.lerGrafoJSON('grafo.txt')
