import clubs
import user

class Recommender:
    """The hub of activity for the project"""

    # these need to be instance variables i think => initialize here not in __init__()
    # i think if they aren't then how will I deal with them in user
    __users = []                   # array of connections to students
    __clubs = []                   # array of connections to clubs

    # all variables are pointers in python

    # create a user and add to the __user dictionary
    # param: student's ID
    # returns: the new user
    def addUser(self, id):
        newUser = user.User(id)                          # call __init__ of the user class
        self.__users.append(newUser)               # add the user to the dict
        return newUser

    def print__users(self):
        for user in self.__users:
            print(user.id)
        return 0

    def print_clubs(self):
        for club in self.__clubs:
            print(club.name)
            print(club.category)
            print(club.id)
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
            if(clubName == club.name):
                return club                         # return the pointer to the club
        return -1                                   # something went wrong if I'm here..

    # gets the recommendation from the user and returns it
    # param: student's ID
    # returns the recommendation
    def createUserRecommendations(id):
        # set recommendation to None (NULL) so it has the scope of the method
        recommendation = None
        for user in __users:
            if(user.destination.id == id):
                # call findClub() in the user's object to get recommendations
                recommendation = user.findClub()
        return recommendation


    # the read data methods are taking it from excel spreadsheets
    def __readClubData():
        # open club information
        data = __readExcelData("")
        clubName = ""
        clubCategory = ""
        clubId = None
        newClub = club.Club(clubName, clubCategory, clubID)
        return 0

    def __readUserData():
        data = __readExcelData("")
        studentId = -1
        newUser = user.User(studentId)
        return 0

    def __readExcelData(filePath):
        data = None
        if(1 == 1):               # if the file has been completely read
            data = -1
        elif("" in filePath):     # the data is abput student interests
            # parse data from a line
            # deal with it
            data = 0
        else:                   # the data is about clubs
            # parse data from a line
            # deal with that
            data = 1
        return data
