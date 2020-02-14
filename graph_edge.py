class GraphEdge:
    """ Represents a edge in the graph of users and clubs- allows me to have a weight to the graph"""
    weight = 1
    destination = None

    def __init__(self, newDestination):
        self.weight = 1
        destination = newDestination
        return 0

    def addOneToWeight(self):
        self.weight = self.weight + 1
        return self.weight
