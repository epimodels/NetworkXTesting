import networkx as nx
import random
import matplotlib.pyplot as plt

import PopGraph


# Returns a graph from a graph of empty nodes, and a list of PopNodes
# Uses relabel_nodes function:
def populate(g, popList):
    nodeList = g.nodes  # gets a list of the node of the graph to be written over
    mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
    newGraph = nx.relabel_nodes(g, mapping, True)  # copies the population objects to the original graph
    return newGraph


# Returns a graph from a graph of empty nodes
def auto_populate(g):
    # generate list of popNodes
    popList = []
    for i in g:
        popNode = PopNode(random.randrange(0, 99), random.randrange(0, 99))
        popList.append(popNode)

    nodeList = g.nodes  # gets a list of the node of the graph to be written over
    mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
    newGraph = nx.relabel_nodes(g, mapping, True)  # copies the population objects to the original graph
    return newGraph


# for each node, there is a chance of the population migrating
def simulate(g1, ticks, weight):
    for i in range(ticks):
        for node in g1:
            for neighbor in iter(g1[node]):
                if random.random() <= weight:
                    neighbor.pop1 += 1
                    node.pop1 -= 1
                if random.random() <= weight:
                    neighbor.pop2 += 1
                    node.pop2 -= 1
    return g1


# Displays a graph of PopNodes graphically, with each PopNode shown as a tuple
def display(g1):
    # make a list with a tuple for each node in g1
    tupleList = []
    for i in g1.nodes():
        tupleList.append((i.pop1, i.pop2))

    # draw a graph with the PopNodes replaced with tuples
    mapping = dict(zip(g1.nodes, tupleList))
    g2 = nx.relabel_nodes(g1, mapping)
    nx.draw(g2, with_labels=True, font_weight='bold')
    plt.show()

# finds the greatest difference in population between graphs
def compare(g1, g2):
    lst1 = list(g1.nodes)
    lst2 = list(g2.nodes)

    popDif = 0

    for i in range(len(lst1)):
        temp1 = abs(lst1[i].pop1 - lst2[i].pop1)
        temp2 = abs(lst1[i].pop2 - lst2[i].pop2)
        if temp1 > popDif:
            popDif = temp1
        if temp2 > popDif:
            popDif = temp2

    return popDif


# Stores two populations (each population stores an integer)
class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2


if __name__ == '__main__':

    G = PopGraph.PopGraph()

    display(auto_populate(G))
