####### GRAPH_EDGE.PY #######
####### Has the GraphEdge class #######
####### The graph edge class will be the connections between clubs. #######
####### This class allows for a weighted connection between clubs. #######

class GraphEdge:
    """ Represents a edge in the graph of users and clubs- allows me to have a weight to the graph"""

    # the constructor for the GraphEdge class
    # param: a club object that will be the destination of the connection
    def __init__(self, newDestination):
        self.__weight = 1                   # initialize it to one
        self.__destination = newDestination     # initialize the destination to a club object

    # adds one to the weight of the connecton
    # param: nothing
    # returns: the weight
    def addOneToWeight(self):
        self.__weight = self.__weight + 1
        return self.__weight

    # returns: the destination of the edge
    # param: none
    def getDestination(self):
        return self.__destination

    # returns the weight of the connection
    # param: none
    def getWeight(self):
        return self.__weight
