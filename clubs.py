import user
from graph_edge import *

class Club:
    """Represents clubs at Xavier University"""

    # the constructor for the Clubs class
    def __init__(self, clubName, clubCategory, clubID, recommender):
        self.name = clubName
        self.category = clubCategory
        self.related = []
        self.id = clubID
        self.recommender = recommender

    # add a related club by pointing to it in the related array
    # returns 0 if the connection was added; o.w. returns -1
    def addRelated(self, clubName):
        club = self.recommender.getClub(clubName)                   # get pointer to the club in the recommender object
        flag = -1
        #print("about to check club")                                      # assumes the connection will not be added
        if(club != -1):
            newConnection = GraphEdge(club)    # create the graph_edge object
            self.related.append(newConnection);               # append the related array with the object
            flag = 0
        return flag

    def printRelated(self):
        print(self.name)
        for club in self.related:
            print("Club:" + club.destination.name)
            print(club.weight)
        return None

    # call when tbe club needs to connect it to person's other clubs
    # param: the club to connect to
    # return: TBD
    #def addConnection(self, clubToConnectTo):
        #if(clubToConnectTo in self.related):              # if the clubs already have a connection:
        #    oneToAddTo = self.related.index(clubToConnectTo)   # find the club in the array
        #    self.related[oneToAddTo].addOneToWeight()     # add one to the weight
        #else:
        #    newConnection = GraphEdge(clubToConnectTo)               # create a graph_edge to each of the other clubs
        #    self.related.append(newConnection)            # append to the club's related array
        #return 0

    def addConnection(self, clubToConnectTo):
        for club in self.related:
            if(club.destination.name is clubToConnectTo.name):
                club.addOneToWeight()
                return 0                                    # get out of here cause we don't need to add it again

        # If I am here, I know the club was not already related
        newConnection = GraphEdge(clubToConnectTo)
        self.related.append(newConnection)
        return 1

    # looks at the club's most common related club
    # look for the club's heaviest edge
    # param: none
    # returns: club object to the user
    def returnMostCommonClub(self):
        # set the local variables so they are less than all objects
        mostCommonIndex = -1
        heaviestWeight = -1

        # go through the related and look for the most common link
        index = 0                   # 0 since we need to start at the beginning
        while(index < len(clubs)):
            if(heaviestWeight < self.related[index].weight):
                mostCommonIndex = index
                heaviestWeight = self.related[index].weight
            index = index + 1
        return self.related[index]       # return the club to the user
