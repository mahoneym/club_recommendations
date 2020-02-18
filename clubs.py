#import user
import graph_edge

class Club:
    """Represents clubs at Xavier University"""
    __clubs = []

    # the constructor for the Clubs class
    def __init__(self, clubName, clubCategory, clubID):
        self.name = clubName
        self.category = clubCategory
        self.related = []
        self.id = clubID
        __clubs.append(self)

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

    # call when tbe club needs to connect it to person's other clubs
    # param: the clubs array from the user and the index of the
        # club that called the method
    # return: TBD
    def addConnection(clubToConnectTo):
        if(clubToConnectTo in related):      # if the clubs already have a connection:
            oneToAddTo = related.index(clubToConnectTo)# find the club in the array
            related[oneToAddTo].addOneToWeight()   # add one to the weight
        else:
            newConnection = graph_edge(clubs[index]) # create a graph_edge to each of the other clubs
            related.update(newConnection)            # append to the club's related array

        return 0

    # looks at the club's most common related club
    # look for the club's heaviest edge
    # param: none
    # returns: club object to the user
    def returnMostCommonClub():
        # set the local variables
        # -1 so they are less than all objects
        mostCommonIndex = -1
        heaviestWeight = -1

        # go through the related and look for the most common link
        index = 0                   # 0 since we need to start at the beginning
        while(index < len(clubs)):
            if(heaviestWeight < related[index].weight):
                mostCommonIndex = index
                heaviestWeight = related[index].weight
            index = index + 1
        return related[index]       # return the club to the user


    def print_clubs(self):
        for club in self.__clubs:
            print(club.name)
            print(club.category)
            print(club.id)
        return 0

    # return the id of the club if it is found; o.w. return -1
    def getClub(clubName):
        for club in self.__clubs:
            if(clubName == club.name):
                return club                         # return the pointer to the club
        return -1                                   # something went wrong if I'm here..
