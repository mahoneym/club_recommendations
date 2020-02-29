import clubs
import user

class Recommender:
    """The hub of activity for the project"""

    # all variables are pointers
    # instance variables
    __users = []                   # array of students
    __clubs = []                   # array of clubs

    # create a user and add to the __user dictionary
    # param: student's ID
    # returns: the new user
    def addUser(self, id):
        newUser = user.User(id)                          # call __init__ of the user class
        self.__users.append(newUser)               # add the user to the dict
        return newUser

    def print_users(self):
        for user in self.__users:
            print(user.id)
            user.print_userClubs()
        return 0

    def print_clubs(self):
        for club in self.__clubs:
            print("Printing Related for:" + club.name)
            club.printRelated()
        return 0

    # add a new club to the list
    # param: the name of the club, its category, and its ID
    # returns: 0
    def addClub(self, clubName, clubCategory, clubID):
        newClub = clubs.Club(clubName, clubCategory, clubID, self)
        self.__clubs.append(newClub)
        return 0

    # return the id of the club if it is found; o.w. return -1
    def getClub(self, clubName):
        for club in self.__clubs:
            if(clubName == club.getClubName()):
                return club                         # return the pointer to the club
        return -1                                   # something went wrong if I'm here..

    # gets the recommendation from the user and returns it
    # param: student's ID
    # returns the recommendation
    def createUserRecommendations(self, id):
        # set recommendation to None (NULL) so it has the scope of the method
        recommendation = None
        for user in self.__users:
            if(user.id == id):
                # call findClub() in the user's object to get recommendations
                recommendation = user.findClub()
        return recommendation
