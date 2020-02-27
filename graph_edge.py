class GraphEdge:
    """ Represents a edge in the graph of users and clubs- allows me to have a weight to the graph"""

    def __init__(self, newDestination):
        self.weight = 1     # initialize it to one
        self.destination = newDestination

    def addOneToWeight(self):
        self.weight = self.weight + 1
        return self.weight
