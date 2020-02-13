from clubs.py import addRelated
from recommender.py import getClubPointer
import graph_edge.py
import random

class User:
    """Represents a student in the recommendation system"""
    clubs           # put graph edge objects for the student's interests
    id              # a unique id for the user

    def __init__(self, studentId, studentName):
        self.clubs = []
        self.id = studentId

    def addClub(clubName):
        # check that the club isn't already being pointed to
        for club in clubs:                                  # loop through each of the clubs
            if (club.destination == clubName):              # check the graph_edge destinations to be the same as the parameter
                return -1                                   # Get out of here cause the club is already here..
        getClubPointer(clubName)                            # get a pointer to the club from recommender class
        newClub = graph_edge(a)                             # create a graph_edge object
        clubs.append(newClub)                               # append the graph_edge object to the clubs dictionary

        # make connections between clubs to the club I just added to this user (A)
        # go through each club in the user's array
        # for each club:
            # make a pointer in club A to it
            # make a pointer from the club to club A
        return 0

    def findClub():
        # find club with highest weight
        index = 0
        # set index and weight to a negative number
        # so we will know if something messed up
        maxIndex = -1
        maxWeight = -1
        while(index < len(clubs)):
            if club.weight > maxWeight:
                maxIndex = index
                maxWeight = club.Weight
            index++
        # follow the club index to the club's actual object
        # look for the club's heaviest edge
        # follow one of the pointers and get it back
        return 0

    def addUserData():
        # add a pointer to the new interests
        return 0
