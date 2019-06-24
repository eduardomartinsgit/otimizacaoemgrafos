import json

class Grafo(object):
	def __init__(self, orientado = False):
		self.n, self.m, self.orientado = None, None, orientado
	
	def DefinirN(self, n):
		self.n, self.m = n, 0
		
	def V(self):
		for i in range(1, self.n+1):
			yield i

	def E(self, IterarSobreNo=False):
		for v in self.V():
			for w in self.N(n, Tipo = "+" if self.orientado else "*", IterarSobreNo=IterarSobreNo):
				enumerar = True
				if not self.orientado:
					wint = w if isinstance(w, int) else w.Viz
					enumerar = v < wint
				if enumerar:
					yield (v, w)
	
	
class GrafoMatrizAdj(Grafo):

	def lerGrafoJSON(self, nomeArquivo): #MÉTODO PARA LEITURA DO GRAFO NO FORMATO JSON
		with open(nomeArquivo) as json_file:
				grafoJSON = json.load(json_file)
				self.v = len(grafoJSON['vertices'])
				self.e = len(grafoJSON['arestas'])

				return grafoJSON

	def DefinirN(self, n):
		super(GrafoMatrizAdj, self).DefinirN(n)
		self.M = [None]*(self.n+1)
		for i in range(1, self.n+1):
			self.M[i] = [0] * (self.n+1)
	
	def RemoverArestas(self, u, v):
		self.M[u][v] = 0
		if not self.orientado:
			self.M[v][u] = 0
		self.m = self.m-1
		
	def AdicionarAresta(self, u, v):
		self.M[u][v] = 1
		if not self.orientado:
			self.M[v][u] = 1
		self.m = self.m+1
	
	def SaoAdj(self, u, v):
		return self.M[u][v] == 1
	
	def N(self, v, Tipo = "+", Fechada=False, IterarSobreNo=False):
		if Fechada:
			yield v
		w = 1
		t = "+" if Tipo == "*" and self.orientado else Tipo
		while w<= self.n:
			if t == "+":
				orig, dest, viz = v, w, w
			else:
				orig, dest, viz = w, v, w
				
			if self.SaoAdj(orig, dest):
				yield w
			w = w+1
			if w > self.n and t == "+" and Tipo == "*":
				t, w = "-", 1
				
				
class GrafoListaAdj(Grafo):
	class NoAresta(object):
		def __init__(self):
			self.Viz = None
			self.e = None
			self.Prox = None
	
	class Aresta(object):
		def __init__(self):
			self.v1, self.No1 = None, None
			self.v2, self.No2 = None, None
	
	def DefinirN(self, n, VizinhancaDuplamenteLigada=False):
		super(GrafoListaAdj, self).DefinirN(n)
		self.L = [None]*(self.n+1)
		for i in range(1,self.n+1):
			self.L[i] = GrafoListaAdj.NoAresta()
		self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada
		
	def AdicionarAresta(self, u, v):
		def AdicionarLista(u,v,e,Tipo):
			No = GrafoListaAdj.NoAresta()
			No.Viz, No.e, No.Prox, self.L[u].Prox = v, e, self.L[u].Prox, No
			if self.VizinhancaDuplamenteLigada:
				self.L[u].Prox.Ant = self.L[u]
				if self.L[u].Prox.Prox != None:
					self.L[u].Prox.Prox.Ant = self.L[u].Prox
			if self.orientado:
				No.Tipo = Tipo
			return No
		e = GrafoListaAdj.Aresta()
		e.v1, e.v2 = u, v
		e.No1 = AdicionarLista(u,v,e,"+")
		e.No2 = AdicionarLista(v,u,e,"-")
		self.m = self.m+1
		return e
	
	def RemoverArestas(self, uv):
		def RemoverLista(No):
			No.Ant.Prox = No.Prox
			if No.Prox != None:
				No.Prox.Ant = No.Ant
		RemoverLista(uv.No1)
		RemoverLista(uv.No2)
	
	def SaoAdj(self, u, v):
		Tipo = "+" if self.orientado else "*"
		for w in self.N(u, Tipo):
			if w == v:
				return True
		return False
		
	def N(self, v, Tipo = "*", Fechada=False, IterarSobreNo=False):
		if Fechada:
			No = GrafoListaAdj.NoAresta()
			No.Viz, No.e, No.Prox = v, None, None
			yield No if IterarSobreNo else No.Viz
		w = w.Prox
	
def FluxoMaximo(D):
	F = 0
	for (u, uv) in D.E():
		uv.e.f = 0
	Dlin = ObterRedeResidual(D)
	s, t = 1, D.n
	P = Busca(Dlin, s, t)
	while len(P) > 0:
		Flin = min([uv.e.r for uv in P])
		for j in range(len(P)):
			if P[j].e.direta:
				P[j].e.eD.f = P[j].e.eD.f + Flin
			else:
				P[j].e.eD.f = P[j].e.eD.f - Flin
		F = F + Flin
		Dlin = ObterRedeResidual(D)
		P = Busca(Dlin, s, t)
	return F
	
def ObterRedeResidual(D):
	Dlin = GrafoListaAdj(orientado=True)
	Dlin.Definir(D.n)
	for(v,uv) in D.E():
		uv = uv.e
		if uv.c-uv.f>0:
			e = Dlin.AdicionarAresta(uv.v1, uv.v2)
			e.r = uv.c-uv.f
			e.direta = True
			e.eD = uv
		if uv.f>0:
			e = Dlin.AdicionarAresta(uv.v2, uv.v1)
			e.r = uv.f
			e.direta = False
			e.eD = uv
	return Dlin


## INICIO PGM