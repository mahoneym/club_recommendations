import recommender
from datetime import datetime
from main_window import MainWindow

# add data to the interface's recommender object
def addData():
    global u1, u2, u3, u4, u5

    # create the users
    u1 = recommend.addUser(1)
    u2 = recommend.addUser(2)
    u3 = recommend.addUser(3)
    u4 = recommend.addUser(4)
    u5 = recommend.addUser(5)

    # add clubs to the users
    u1.addClub('MuskieTHON', recommend)
    u1.addClub('Computer Science Club', recommend)
    u1.addClub("Accounting Society", recommend)

    u2.addClub('MuskieTHON', recommend)
    u2.addClub('A Xavier Christmas', recommend)
    u2.addClub('Computer Science Club', recommend)

    u3.addClub('A Xavier Christmas', recommend)
    u3.addClub('4 Paws for Ability at XU', recommend)
    u3.addClub("Don't Tell Anna", recommend)

    u4.addClub('A Xavier Christmas', recommend)
    u4.addClub("Don't Tell Anna", recommend)
    u4.addClub('MuskieTHON', recommend)

    u5.addClub("Computer Science Club", recommend)
    u5.addClub("Don't Tell Anna", recommend)
    u5.addClub('A Xavier Christmas', recommend)

    # add interests to the users
    recommend.addUserInterest(1, "STEM")
    recommend.addUserInterest(1, "General Interests")
    recommend.addUserInterest(1, "Spirituality")

    recommend.addUserInterest(2, "Health Professions")
    recommend.addUserInterest(2, "Wellness")
    recommend.addUserInterest(2, "Service & Social Justice")

    recommend.addUserInterest(3, "STEM")
    recommend.addUserInterest(3, "General Interests")
    recommend.addUserInterest(3, "Wellness")

    recommend.addUserInterest(4, "Service & Social Justice")
    recommend.addUserInterest(4, "Spirituality")
    recommend.addUserInterest(4, "STEM")

    # create date objects for the events
    date_1 = datetime(year= 2019, month = 5, day = 25, hour = 19, minute = 0)
    date_1_2 = datetime(year=3020, month = 5, day = 25, hour = 19, minute = 0)
    date_2 = datetime(year= 3020, month = 5, day = 25, hour = 19, minute = 0)

    # add events to some clubs
    recommend.addEventToClub("Computer Science Club", "Event_1", date_1, "Alter Hall Rm 101", "This is a longer description to play with text wrapping. The first event that is added to the clubs. It should be showing up for CS club.")
    recommend.addEventToClub("Computer Science Club", "Event_1_2", date_1_2, "Alter Hall Rm 101", "This is a longer description to play with text wrapping. The first event that is added to the clubs. It should be showing up for CS club.")
    recommend.addEventToClub("4 Paws for Ability at XU", "Event_2", date_2, "Alter Hall Rm 102", "Event 2")

    recommend.addEventToClub("Don't Tell Anna", "Spring Show", date_2, "Kennedy Auditorium", "Spring Show")
    recommend.addEventToClub("MuskieTHON", "Dance Marathon", date_2, "GSC", "The 24 Hour Dance Marathon")
    return None


recommend = recommender.Recommender()                  # starts the recommender object
addData()                                              # adds the data to the recommender
MainWindow(recommend)                                  # starts the GUI and drives it
