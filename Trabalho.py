import re
import time
    
class MatrizAdjGrafo:

        def lerGrafoJSON(self, nomeArquivo):
                f = open(nomeArquivo, 'r') #LEITURA DO ARQUIVO DE ENTRADA, NO MODO 'R' SOMENTE LEITURA
                json = f.readline()
                return json 
        
        def __init__(self):
                self.v = 0
                self.e = 0
                self.m = []

#FIM DA MATRIZ DE ADJACENCIAS

grafoMatriz = MatrizAdjGrafo()
