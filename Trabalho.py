import json
import time
import timeit
    
	
#INICIO DA IMPLEMENTAÇÃO DE UMA FILA COMO ESTRUTURA AUXILIAR
class Fila():
    def __init__(self):
        self.dados = []

    def insere(self, elemento):
        self.dados.append(elemento)

    def remove(self):
        return self.dados.pop(0) 
    
    def length(self):
        return len(self.dados)	
	
#FIM DA IMPLEMENTAÇÃO DE UMA FILA COMO ESTRUTURA AUXILIAR	
	
#INICIO DA IMPLEMENTAÇÃO DE UMA PILHA COMO ESTRUTURA AUXILIAR
class Pilha():
    def __init__(self):
        self.dados = [0]

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        return self.dados.pop()
    
    def length(self):
        return len(self.dados)	
#FIM DA IMPLEMENTAÇÃO DE UMA PILHA COMO ESTRUTURA AUXILIAR		

#INICIO DA MATRIZ DE ADJACENCIAS	
class MatrizAdjGrafo:

        def lerGrafoJSON(self, nomeArquivo): #MÉTODO PARA LEITURA DO GRAFO NO FORMATO JSON
                with open(nomeArquivo) as json_file:
                        grafoJSON = json.load(json_file)
                        self.v = len(grafoJSON['vertices'])
                        self.e = len(grafoJSON['arestas'])

                        for i in range(self.v): #Criação da matriz e inicializando com 0
                                self.m.append(self.v * [0])
                                self.visitado.append(False)
                                self.descoberta.append(self.v * [False])
                                self.explorado.append(self.v * [False])
                                self.distancia.append(0)
                        return grafoJSON
        def __init__(self):
                self.v = 0
                self.e = 0
                self.m = []
                self.explorado = []
                self.descoberta = []
                self.visitado = []
                self.distancia = []


        def imprimirGrafo(self,grafo): #MÉTODO PARA IMPRIMIR A ESTRUTURA DO GRAFO 
                for i in range(self.v):
                        for j in range(self.v):
                                print(grafo[i][j], end=' ') # Imprimir no console em forma de matriz
                        print('')


        def inserirAresta(self, grafoJSON): #MÉTODO PARA INSERIR UMA NOVA ARESTA
                arestas = grafoJSON['arestas']
                for i in range(0, len(arestas)):
                        self.m[int(arestas[i][0]) - 1][int(arestas[i][1]) - 1] = int(1)
                        self.m[int(arestas[i][1]) - 1][int(arestas[i][0]) - 1] = int(1)

        def removerAresta(self, linha, coluna): #MÉTODO PARA REMOÇÃO DE UMA ARESTA
                self.m[linha][coluna] = 0
                self.m[coluna][linha] = 0
                self.e= self.e - 1

        def Busca(self,r):#MÉTODO DE BUSCA DE UM DETERMINADO ELEMENTO NO GRAFO, SLIDE 5
            self.visitado[r] = True
            for x in range(self.v):
                for y in range(self.v):
                    if(self.visitado[x] and (not self.explorado[x][y])):
                        self.explorado[x][y] = True
                        if(not self.visitado[y]):
                            self.visitado[y] = True
                            self.descoberta[x][y] = True
                            
        def BuscaR(self): #MÉTODO DE BUSCA DE UM DETERMINADO ELEMENTO NO GRAFO, SLIDE 5
            self.rotular()
            self.Busca(1)

        def rotular(self): #MÉTODO ROTULAR, SLIDE 5
            self.visitado= [False]*self.v
            for i in range(self.v):
                self.explorado.append([False]*self.v)
                self.descoberta.append([False]*self.v)
                
        def BuscaCompleta(self): #MÉTODO DE BUSCA COMPLETA EM UM DETERMINADO GRAFO, SLIDE 6
            for i in range(self.v):
                if( not self.visitado[i]):
                    self.Busca(i)

        def EhConexo(self): #MÉTODO QUE VERIFICA SE UM DETERMINADO GRAFO É CONEXO, SLIDE 9
            self.BuscaR()
            for i in range(self.v):
                if(not self.visitado[i]):
                    return False
            return True


        def TemCiclo(self): #MÉTODO QUE VERIFICA SE TEM CICLO NO GRAFO, SLIDE 10
            self.BuscaCompleta()
            for x in range(self.v):
                for y in range(self.v):
                    if(self.m[x][y]==1):
                        if(not self.descoberta[x][y]):
                            return True
                return False

        
        def EhFloresta(self): #DECISÃO DE O GRAFO É FLORESTA, SLIDE 11
            return not self.TemCiclo()

        def EhArvore(self): #DECISÃO DE O GRAFO É UMA ARVORE, SLIDE 12
            self.BuscaR()
            for i in range(self.v):
                if(not self.visitado[i]):
                    return False
            for i in range(self.v):
                for j in range(self.v):
                    if(self.m[i][j]==1):
                        if(not self.descoberta[i][j]):
                            return False
            return True


        def EhArvoreConexoCiclo(self): #DECISÃO DE O GRAFO É UMA ARVORE, SLIDE 13
            return self.EhConexo() and not self.TemCiclo()

        def ObterFlorestaGeradora(self):#MÉTODO PARA OBTER A FLORESTA GERADORA, SLIDE 17
            t = MatrizAdjGrafo()
            t.v = self.v
            t.e = []
            for i in range(t.v):
                t.m.append([0]*t.v)
                self.BuscaCompleta()
            for i in range(self.v):
                for j in range(self.v):
                    if(self.descoberta[i][j]):
                        t.m[i][j] = 1
            return t

        def BuscaProfundidade(self,v): #MÉTODO DE BUSCA EM PROFUNDIDADE, SLIDE 26
            self.rotular()
            p = Pilha()
            self.visitado[v] = True
            p.empilha(v)
            p.empilha(self.PrimeiroViz(v))
            while(p.length() > 0):
                v = p.desempilha()
                if(p.length() > 1):
                    w = p.desempilha()
                    if(w > 0):
                        p.empilha(v)
                        p.empilha(self.ProximoViz(v,w))
                        if(self.visitado[w]):
                            if (not self.explorado[v][w]):
                                self.explorado[v][w] = True
                            else:
                                self.explorado[v][w] = True
                                self.descoberta[v][w] = True
                                self.visitado[w] = True
                                p.empilha(w)
                                p.empilha(self.PrimeiroViz(w))

        def PrimeiroViz(self,v):
            for i in range(self.v):
                if(self.m[v][i]==1):
                    return i
            return 0

        def ProximoViz(self,v, u):
            for i in range(u ,self.v):
                if(self.m[v][i]==1):
                    return i
            return 0

        def BuscaProfundidadeRecursiva(self, v): #MÉTODO DE BUSCA EM PROFUNDIDADE RECURSIVA, SLIDE 27
            self.visitado[v] = True
            for i in range(self.v):
                if(self.m[v][i] == 1):
                    if(self.visitado[i]):
                        if(not self.explorado[v][i]):
                            self.explorado[v][i] = True
                    else:
                        self.explorado[v][i] = True
                        self.descoberta[v][i] = True
                        self.BuscaProfundidadeRecursiva(i)

        def BuscaLargura(self, v): #MÉTODO DE BUSCA EM LARGURA, SLIDE 57
            f = Fila()
            self.visitado[v] = True
            f.insere(v)
            while(f.length() > 0):
                v = f.remove()
                for i in range(self.v):
                    if(self.m[v][i] == 1):
                        if(self.visitado[i]):
                            if(not self.explorado[v][i]):
                                self.explorado[v][i] = True
                        else:
                            self.explorado[v][i] = True
                            self.descoberta[v][i] = True
                            self.visitado[i] = True

        def DeterminarDistancias(self, v): #MÉTODO DE DETERMINAR DISTANCIAS, SLIDE 62
            f = Fila()
            self.rotular()
            self.visitado[v] = True
            self.distancia[v] = 0
            f.insere(v)
            while(f.length() > 0):
                p = f.remove()
                for i in range(self.v):
                    if(self.visitado[i] == 1):
                        if(not self.explorado[v][i]):
                            self.explorado[v][i] = True
                    else:
                        self.explorado[v][i] = True
                        self.descoberta[v][i] = True
                        self.visitado[i] = True
                        self.distancia[i] = p
                        f.insere(v+1)
                        
                    

#FIM DA MATRIZ DE ADJACENCIAS

# INICIO DA LISTA DE ADJACENCIAS
class ListaAdjGrafo:
        def __init__(self):
                self.L = []
                self.v = None
                self.e = None
                self.distancia = []
                
        def lerGrafoJSON(self, nomeArquivo):
                with open(nomeArquivo) as json_file:
                        grafoJSON = json.load(json_file)
                        self.v = len(grafoJSON['vertices'])
                        self.e = len(grafoJSON['arestas'])
                        self.L = [None]*(self.v+1)
                        self.distancia = [None]*(self.v+1)
                        for i in range(self.v+1): #Criação da lista e inicializando com None
                                self.L[i] = ListaAdjGrafo.NoAresta()
                return grafoJSON
                                
        class NoAresta(object): #CONFORME O SLIDE 
                def __init__(self):
                        self.viz = None
                        self.e = None
                        self.prox = None
                        self.vizitado = False
                        self.descoberta = False
                        self.explorado = False


        class Aresta(object): #CONFORME O SLIDE 
                def __init__(self):
                    self.explorado = False

                    
        def inserir(self, lista, vizinho, novaAresta): #METODO AUXILIAR PARA INSERÇÃO DE UMA NOVA ARESTA 
                novoNo = ListaAdjGrafo.NoAresta()
                novoNo.descoberta = True
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
                        self.L[u] = self.inserir(self.L[u], v, novaAresta)
                        self.L[v] = self.inserir(self.L[v], u, novaAresta)

        def imprimirVizinhos(self):
            for i in range(self.e):
                print(self.L[i].viz)


        def Busca(self, r):#MÉTODO DE BUSCA DE UM DETERMINADO ELEMENTO NO GRAFO, SLIDE 5
            self.L[r].explorado = True
            self.L[r].vizitado = True
            return self.L[r]
        
        def BuscaCompleta(self): #MÉTODO DE BUSCA COMPLETA EM UM DETERMINADO GRAFO, SLIDE 6
            for i in range(0, len(self.L)):
                self.Busca(i)

                
        def EhConexo(self): #MÉTODO QUE VERIFICA SE UM DETERMINADO GRAFO É CONEXO, SLIDE 9
            for i in range(self.v):
                if(not self.L[i].vizitado):
                    return False
            return True

        def TemCiclo(self): #MÉTODO QUE VERIFICA SE TEM CICLO NO GRAFO, SLIDE 10
            self.BuscaCompleta()
            for x in range(self.v):
                if(not self.L[x].descoberta):
                    return True
            return False

        def EhFloresta(self): #DECISÃO DE O GRAFO É FLORESTA, SLIDE 11
            return not self.TemCiclo()

        def EhArvore(self): #DECISÃO DE O GRAFO É UMA ARVORE, SLIDE 12
            self.BuscaCompleta()
            for i in range(self.v):
                if(not self.L[i].vizitado):
                    return False
            for i in range(self.v):
                for j in range(self.v):
                    if(not self.L[i].descoberta):
                        return False
            return True
        
        def EhArvoreConexoCiclo(self): #DECISÃO DE O GRAFO É UMA ARVORE, SLIDE 13
            return self.EhConexo() and not self.TemCiclo()


        def ObterFlorestaGeradora(self):#MÉTODO PARA OBTER A FLORESTA GERADORA, SLIDE 17
            t = ListaAdjGrafo()
            t.v = self.v
            t.e = None
            for i in range(t.v):
                t.L.append([0]*t.v)
                self.BuscaCompleta()
            for i in range(self.v):
                if(self.L[i].descoberta):
                    t.e = 1
            return t

        def PrimeiroViz(self,v):
            for i in range(self.v):
                if(self.L[v].e == 1):
                    return i
            return 0

        def ProximoViz(self,v, u):
            for i in range(u ,self.v):
                if(self.L[v].e == 1):
                    return i
            return 0

        def BuscaProfundidade(self,v): #MÉTODO DE BUSCA EM PROFUNDIDADE, SLIDE 26
            p = Pilha()
            self.L[v].vizitado = True
            p.empilha(v)
            p.empilha(self.PrimeiroViz(v))
            while(p.length() > 0):
                v = p.desempilha()
                if(p.length() > 1):
                    w = p.desempilha()
                    if(w > 0):
                        p.empilha(v)
                        p.empilha(self.ProximoViz(v,w))
                        if(self.L[w].vizitado):
                            if (not self.L[v].explorado):
                                self.L[v].explorado = True
                            else:
                                self.L[v].explorado = True
                                self.L[v].descoberta = True
                                self.L[v].visitado = True
                                p.empilha(w)
                                p.empilha(self.PrimeiroViz(w))

        def BuscaProfundidadeRecursiva(self, v): #MÉTODO DE BUSCA EM PROFUNDIDADE RECURSIVA, SLIDE 27
            self.L[v].visitado = True
            for i in range(self.v):
                if(self.L[i].e == v):
                    if(self.L[v].visitado):
                        if(not self.L[v].explorado):
                            self.L[v].explorado = True
                    else:
                        self.L[v].explorado = True
                        self.L[v].descoberta = True
                        self.BuscaProfundidadeRecursiva(i)

        def BuscaLargura(self, v): #MÉTODO DE BUSCA EM LARGURA, SLIDE 57
            f = Fila()
            self.L[v].visitado = True
            f.insere(v)
            while(f.length() > 0):
                v = f.remove()
                for i in range(self.v):
                    if(self.L[v].e == v):
                        if(self.L[i].visitado):
                            if(not self.L[v].explorado):
                                self.L[v].explorado = True
                        else:
                            self.L[v].explorado = True
                            self.L[v].descoberta = True
                            self.L[v].vizitado = True

        def DeterminarDistancias(self, v): #MÉTODO DE DETERMINAR DISTANCIAS, SLIDE 62
            f = Fila()
            self.L[v].visitado = True
            self.distancia[v] = 0
            f.insere(v)
            while(f.length() > 0):
                p = f.remove()
                for i in range(self.v):
                    if(self.L[v].vizitado):
                        if(not self.L[v].explorado):
                            self.L[v].explorado = True
                    else:
                        self.L[v].explorado = True
                        self.L[v].descoberto = True
                        self.L[v].vizitado = True
                        self.distancia[v] = p
                        f.insere(v+1)
                            
        
# FIM DA LISTA DE ADJACENCIAS


'''
grafo = MatrizAdjGrafo()
grafoJSON = grafo.lerGrafoJSON('grafo.txt')
grafo.inserirAresta(grafoJSON)
print (grafo.distancia)
'''

graph = ListaAdjGrafo()
grafoJSON = graph.lerGrafoJSON('grafo.txt')
graph.inserirAresta(grafoJSON)

grafo = MatrizAdjGrafo()
grafoJSON = grafo.lerGrafoJSON('grafo.txt')
grafo.inserirAresta(grafoJSON)

inicio = timeit.default_timer()
graph.DeterminarDistancias(28)
fim = timeit.default_timer()
print ('LISTA ADJACENCIAS duracao: %f' % (fim - inicio))

inicio = timeit.default_timer()
grafo.DeterminarDistancias(1)
fim = timeit.default_timer()
print ('MATRIZ ADJACENCIAS duracao: %f' % (fim - inicio))


#print (graph.EhConexo())

