import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.year = DAO.getYear()
        self.graph= nx.Graph()
        self.idMap ={}


    def buildGraph(self, year, giorni):
        self.graph.clear()
        nodi = DAO.getNodes()
        for n in nodi:
            self.graph.add_node(n)
            self.idMap[n.id] = n
        archi = DAO.getArchi(year, giorni)
        for a in archi:
            self.graph.add_edge(self.idMap[a[0]], self.idMap[a[1]], weight = a[2])


    def getPesi(self):
        ris = []
        for n in self.graph.nodes:
            peso = 0
            for v in self.graph.neighbors(n):
                peso+= self.graph[n][v]["weight"]
            ris.append((n, peso))
        return ris

    def graph_details(self):
        return len(self.graph.nodes), len(self.graph.edges)

