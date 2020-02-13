import user
import graph_edge
import recommender

class Clubs:
    """Represents clubs at Xavier University"""
    category = ""
    related = []
    name = ""
    id = 0

    # the constructor for the Clubs class
    def __init__(self, clubName, clubCategory, clubID):
        self.name = clubName
        self.category = clubCategory
        self.related = []
        self.id = clubID

    # add a related club by pointing to it in the related array
    # returns 0 if the connection was added; o.w. returns -1
    def addRelated(clubName):
        ptr = getClubPointer(clubName)                   # get pointer to the club in the recommender object
        flag = -1                                        # assumes the connection will not be added
        if(ptr != -1):
            newConnection = graph_edge(ptr, clubName)    # create the graph_edge object
            related.append(newConnection);               # append the related array with the object
            flag = 0
        return flag

    def makeConnectionsBetweenClubs():
        # create a graph_edge
        # append to the related array
        return 0

    def returnMostCommonClub():
        return 0
