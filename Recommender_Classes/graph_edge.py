class GraphEdge:
    """ Represents a edge in the graph of users and clubs- allows me to have a weight to the graph"""

    def __init__(self, newDestination):
        self.__weight = 1     # initialize it to one
        self.__destination = newDestination

    def addOneToWeight(self):
        self.__weight = self.__weight + 1
        return self.__weight

    def getDestination(self):
        return self.__destination

    def getWeight(self):
        return self.__weight
