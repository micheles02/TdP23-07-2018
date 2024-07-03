import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}
        for stato in DAO.getStati():
            self.idMap[stato.id] = stato

    def creaGrafo(self, anno, giorni):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.idMap.keys())
        self.grafo.add_edges_from(DAO.getVicini())
        print("pesi")
        for (u, v) in self.grafo.edges:
            peso = DAO.getPeso(u, v, anno, giorni)
            print(peso)
            self.grafo[u][v]["weight"] = peso

    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def pesiNodi(self):
        ris = []
        for u in self.grafo.nodes:
            peso = 0
            for v in self.grafo.neighbors(u):
                peso += self.grafo[u][v]["weight"]
            ris.append((u, peso))
        return ris
