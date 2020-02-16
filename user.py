# ----------------------------- USER.PY ---------------------------------------
# This file contains a User class, which will represent each user of the system
# (or student). The User class tracks the user's ID number (as a way to identify
# each one) and keeps a list of the user's clubs. As a result, the class is
# able to addClubs and calls the methods to maintain the connections between clubs.


import clubs
import recommender
import graph_edge
import random

class User:
    """Represents a student in the recommendation system"""
    clubs           # put graph edge objects for the student's interests
    id              # a unique id for the user => given by the data

    def __init__(self, studentId):
        self.clubs = []
        self.id = studentId

    # adds a club to the user's clubs array
    # param: the name of the club to be added
    # returns: 0 when the method finish
    def addClub(clubName):
        index = 0
        # check that the club isn't already being pointed to
        while(index < len(clubs)):                                  # loop through each of the clubs
            if (club.destination.name == clubName):                      # check the graph_edge destinations to be the same as the parameter
                return -1                                           # Get out of here cause the club is already here..
            index = index + 1
        # a = getClubPointer(clubName)                              # get a pointer to the club from recommender class
        # clubs[index].destination will be the club
        newClub = graph_edge(clubs[index].destination)              # create a graph_edge object
        clubs.append(newClub)                                       # append the graph_edge object to the clubs dictionary

        # add connections between the new club and the rest of the user's clubs
        makeConnectionsBetweenClubs(len(clubs)-1)
        return 0

    # goes through the clubs array and connects the index added and the other indices
    # param: the index of the club that was added before this method
    # returns: 0
    def makeConnectionsBetweenClubs(indexAdded):
        index = 0
        while(index < len(clubs)):
            if (index != indexAdded):                                                       # make sure im not gonna connect the club with itself
                clubs[index].destination.addConnection(clubs[indexAdded].destination)       # point from the already present club to the new one
                clubs[indexAdded].destination.addConnection(clubs[index].destination)       # point from the new club to the already present club
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
        while(index < len(clubs)):
            if club.weight > maxWeight:
                maxIndex = index
                maxWeight = club.Weight
            index = index + 1
        # follow the club index to the club's actual object to get recommendation
        return clubs[index].destination
