# ----------------------------- USER.PY ---------------------------------------
# This file contains a User class, which will represent each user of the system
# (or student). The User class tracks the user's ID number (as a way to identify
# each one) and keeps a list of the user's clubs. As a result, the class is
# able to addClubs and calls the methods to maintain the connections between clubs.

import clubs
import graph_edge

class User:
    """Represents a student in the recommendation system"""
    __userClubs = []          # put graph edge objects for the student's interests
    id              # a unique id for the user => given by the data

    def __init__(self, studentId):
        self.id = studentId

    # adds a club to the user's clubs array
    # param: the name of the club to be added
    # returns: 0 when the method finish
    def addClub(self, clubName):
        index = 0
        # check that the club isn't already in the list
        while(index < len(self.__userClubs)):           # loop through each of the clubs
            if (checkForClub):                          # check the graph_edge destinations to be the same as the parameter
                return -1                               # Get out of here cause the club is already here..
            index = index + 1

        clubPointer = getClub(clubName)                 # get the club object that I need
        newClub = graph_edge(clubPointer)               # create a graph_edge object
        __clubs.append(newClub)                         # append the graph_edge object to the clubs dictionary

        # add connections between the new club and the rest of the user's clubs
        makeConnectionsBetweenClubs(len(__userClubs)-1)
        return 0

    def checkForClub(clubName):
        for club in self.__userClubs:
            if(club.destination == self.__userClubs):
                return True
        return False

    # goes through the clubs array and connects the index added and the other indices
    # param: the index of the club that was added before this method
    # returns: 0
    def makeConnectionsBetweenClubs(indexAdded):
        index = 0
        while(index < len(clubs)):
            if (index != indexAdded):                                                       # make sure im not gonna connect the club with itself
                __userClubs[index].destination.addConnection(__userClubs[indexAdded].destination)       # point from the already present club to the new one
                __userClubs[indexAdded].destination.addConnection(__userClubs[index].destination)       # point from the new club to the already present club
            index = index + 1
        return 0

    # find club with highest weight
    # param: None
    # returns: the club with the heaviest connection
    def findClub():
        index = 0
        # set maxIndex and weight to a negative number
        # so we will know if something messed up
        maxIndex = -1
        maxWeight = -1
        while(index < len(self.__userClubs)):
            if club.weight > maxWeight:
                maxIndex = index
                maxWeight = club.Weight
            index = index + 1
        # follow the club index to the club's actual object to get recommendation
        return self.__userClubs[index].destination
