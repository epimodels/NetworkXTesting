import networkx as nx
import random
import matplotlib.pyplot as plt


# Stores two populations (each population stores an integer)
class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2


class PopGraph(nx.Graph):

    # overrides the __init__ method from nx.Graph
    # if a graph is passed for G, then the nodes and edges of G will be added to self
    def __init__(self, G=None):
        super().__init__()
        if G is not None:
            self.add_nodes_from(G.nodes())
            self.add_edges_from(G.edges())

    # simple method to cleanly add new population objects
    def add_pop(self, pop1, pop2):
        self.add_node(PopNode(pop1, pop2))

    # simple method to add a list of populations passed as an array of tuples
    def add_pops_from(self, popArray):
        for pop in popArray:
            self.add_pop(pop[0], pop[1])

    # simple method to find a popNode object that matches the given tuple population
    def find(self, popTuple):
        for node in self.nodes:
            if (popTuple[0] == node.pop1) and (popTuple[1] == node.pop2):
                return node
        return None

    # method that creates edges based on passed array
    # eg: [((44, 13), (36, 46), (68, 92), (88, 19)),
    #      ((36, 46), (44, 13), (65, 93)) (39, 25)),
    #      ((39, 25), (36, 46), (67, 25), (0, 34)),
    #      ((0, 34), (39, 25), (67, 25), (36, 46)),
    #      ((65, 93), (82, 68), (52, 77), (36, 46)),
    #      ((82, 68), (67, 25), (68, 92), (65, 93)),
    #      ((68, 92), (82, 68), (44, 13), (0, 34)),
    #      ((52, 77), (88, 19), (65, 93), (0, 34)),
    #      ((67, 25), (82, 68), (88, 19), (39, 25)),
    #      ((88, 19), (44, 13), (52, 77), (67, 25))
    #      ]
    def add_pop_edges_from(self, popEdgeArray):
        pass

    # Returns a graph from a graph of empty nodes, and a list of PopNodes
    # Uses relabel_nodes function:
    def populate(self, popList):
        nodeList = self.nodes  # gets a list of the nodes of the graph to be written over
        mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
        newGraph = nx.relabel_nodes(self, mapping, True)  # copies the population objects to the original graph
        return newGraph

    # Returns a graph from a graph of empty nodes
    def auto_populate(self):
        # generate list of popNodes
        popList = []
        for i in self:
            popNode = PopNode(random.randrange(0, 99), random.randrange(0, 99))
            popList.append(popNode)

        nodeList = self.nodes  # gets a list of the node of the graph to be written over
        mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
        newGraph = nx.relabel_nodes(self, mapping, True)  # copies the population objects to the original graph
        return newGraph

    # for each node, there is a chance of the population migrating
    def simulate(self, ticks, weight):
        for i in range(ticks):
            for node in self:
                for neighbor in iter(self[node]):
                    if random.random() <= weight:
                        neighbor.pop1 += 1
                        node.pop1 -= 1
                    if random.random() <= weight:
                        neighbor.pop2 += 1
                        node.pop2 -= 1
        return self

    def single_step(self):
        for node in self:
            for neighbor in iter(self[node]):
                print("(" + str(neighbor.pop1) + ", " + str(neighbor.pop2) + ")")
            print("node: " + "(" + str(node.pop1) + ", " + str(node.pop2) + ") \n neighbors: \n")

    # Displays a graph of PopNodes graphically, with each PopNode shown as a tuple
    def display(self):
        # make a list with a tuple for each node in g1
        tupleList = []
        for i in self.nodes():
            tupleList.append((i.pop1, i.pop2))

        # draw a graph with the PopNodes replaced with tuples
        mapping = dict(zip(self.nodes, tupleList))
        g2 = nx.relabel_nodes(self, mapping)
        nx.draw(g2, with_labels=True, font_weight='bold')
        plt.show()
