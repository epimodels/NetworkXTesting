import networkx as nx
import matplotlib.pyplot as plt


# Stores two object
class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2

    # removes first attribute and returns it
    def rem_attribute1(self):
        temp_pop = self.pop1
        self.pop1 = None
        return temp_pop

    # removes second attribute and returns it
    def rem_attribute2(self):
        temp_pop = self.pop2
        self.pop2 = None
        return temp_pop

    # adds attribute to PopNode if there is space
    def add_attribute(self, attribute):
        if self.pop1 is None:
            self.pop1 = attribute
        elif self.pop2 is None:
            self.pop2 = attribute


if __name__ == '__main__':
    popNode1 = PopNode("Werewolves", "Vampires")
    popNode2 = PopNode("Sharks", "Jets")

    G = nx.Graph()
    G.add_node(popNode1)
    G.add_node(popNode2)

    # the first attribute of popNode1 'migrates' to popNode2
    # it replaces the second attribute in popNode2, which is likely not desirable
    popNode2.pop2 = popNode1.rem_attribute1()

    G.add_edge(popNode1, popNode2)



    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
