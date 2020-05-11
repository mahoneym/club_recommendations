####### RECOMMENDER.PY #######
####### This file contains the Recommender class. A Recommender object runs #######
####### the whole recommender system (except the GUI) #######

from Recommender_Classes import Club
from Recommender_Classes import User
from Recommender_Classes import Event
from Recommender_Classes import Interest

# import to read the Excel file data
import pandas as pd
import xlrd

class Recommender:
    """The hub of activity for the project"""

    # all variables are pointers
    # instance variables
    __users = []                   # array of students
    __clubs = []                   # array of clubs
    __interests = []               # array of possible interests

    # the constructor for the recommender class
    # adds the clubs from the excel file
    def __init__(self):
        self.addExcelClubs()

    # create a user and add to the __user dictionary
    # param: student's ID
    # returns: the new user
    def addUser(self, id):
        newUser = User(id)                          # call __init__ of the user class
        self.__users.append(newUser)                     # add the user to the dict
        return newUser

    # add a new club to the list
    # param: the name of the club, its category, and its ID
    # returns: the new club
    def addClub(self, clubName, clubCategory, clubID, description):
        newClub = Club(clubName, clubCategory, clubID, description, self)
        self.__clubs.append(newClub)
        return newClub

    # adds an interest to the list of possibilities (__userInterests)
    # param: the interest id, the interest name, and its category id
    # returns: a None object
    def addInterestToList(self, interestId, interestName, interestCategoryId):
        newInterest = Interest(interestName)
        self.__interests.append(newInterest)
        return None

    # gets the club based on the club name
    # returns the id of the club if it is found; o.w. returns -1
    def getClub(self, clubName):
        for club in self.__clubs:
            if(clubName.lower() == club.getClubName().lower()):
                return club                         # return the pointer to the club
        return -1                                   # something went wrong if I'm here..

    # gets the recommendation from the user based on their clubs and returns it
    # param: student's ID
    # returns the recommendation
    def createClubRecommendation(self, id):
        # set recommendation to None (NULL) so it has the scope of the method
        recommendation = None
        for user in self.__users:
            if(user.id == id):
                # call findClub() in the user to get recommendation
                recommendation = user.findClub()
                return recommendation
        return -1

    # returns the user that is being referenced
    # param: the object itself and the student's id
    # returns: the user object if it is found
    def getUser(self, id):
        for user in self.__users:
            if(user.id == id):
                return user
        return None

    # looks at the user's interests and recommends a club based on them
    # param: the id of the student for which to get the recommendation and the object itself
    # returns: the interest object to the caller
    def createInterestRecommendation(self, id):
        user = self.getUser(id)
        if(not user == None):
            recommendation = user.getInterestRecommendation()
            return recommendation

    # gets the next club event
    # param: the club object to look at
    # returns: the event
    def getNextClubEvent(self, club):
        event = club.getNextEvent()
        return event

    # adds the clubs from the excel file and creates the categories
    # NOTE: categories are acting as the interests at this point
    # param: none to be passed but it takes the self
    # returns: None
    def addExcelClubs(self):
        excel_file = 'data/Clubs.xlsx'

        excelClubs = pd.read_excel(excel_file)

        for index, rows in excelClubs.iterrows():
            # look for the category in the interests
            category = rows['Category']
            foundInInterests = False
            # add the club
            self.addClub(rows['Name'], rows['Category'], rows['ID'], rows['Description'])
            newClub = self.__clubs[len(self.__clubs)-1]
            for interest in self.__interests:
                if (category == interest.getInterestName()):
                    # connect the club to it's interest that we just found
                    interest.addRelatedClub(newClub)
                    foundInInterests = True
            if(foundInInterests == False):         # if the interest was not found
                # add the interest cause it doesn't already exist
                self.addInterestToList(0, category, 0)
                # connect the two
                self.__interests[len(self.__interests)-1].addRelatedClub(newClub)
        return None

    # will find the interest object based on the name
    # param: the string name of the interest
    # return: the interest if it's found; o.w. nothing
    def __findInterest(self, interestName):
        for interest in self.__interests:
            if(interest.getInterestName() == interestName):
                return interest

    # adds an interest to the user
    # param: the student's id and the string name of the interest
    # returns: None
    def addUserInterest(self, id, interestName):
        user = self.getUser(id)
        if(user != None):
            interest = self.__findInterest(interestName)
            user.addInterest(interest)
        return None

    # adds an event to a club
    # param: the club name (string), the event name (string), date (datetime object), location (string), and description (string)
    # returns: 0
    def addEventToClub(self, clubName, name, date, location, description):
        club = self.getClub(clubName)
        event = Event(name, date, club, location, description)
        club.addEvent(event)
        return 0

    # returns a list of the next upcoming event for each of the user's clubs
    # param: the user's id numbers
    # returns: a list(/array) of events
    def getUserUpcomingEvents(self, idNumber):
        user = self.getUser(idNumber)
        eventList = user.getNextEvents()
        return eventList

    # get the names of all the clubs
    # param: none
    # returns: a list of club names (strings)
    def getClubNames(self):
        clubNames = []
        for club in self.__clubs:
            clubNames.append(club.getClubName())
        return clubNames
