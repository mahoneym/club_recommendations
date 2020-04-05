import recommender
from event import *
from datetime import datetime

recommend = recommender.Recommender()

# get some clubs to play with
csClub = recommend.getClub("Computer Science Club")
accountingSociety = recommend.getClub("Accounting Society")

# adds one event to one club and tries to get it back successfully
def theLoneEvent():
    print("The Lone Event")

    # create event_1 for the Accounting Society
    date_1 = datetime(year= 2020, month = 5, day = 25, hour = 19, minute = 0)
    event_1 = Event("Event_1", date_1, csClub, "Alter hall", "It's the first event. :)")
    recommend.addEventToClub('Accounting Society', "Event_1", date_1, "Smith Somewhere", "It's the first event. :)")

    # try to get event 1 back from CS club list
    print("Trying to get the event back")
    event = recommend.getNextClubEvent(accountingSociety)
    assert(not event == None)
    assert(event_1.getName() == event.getName())
    print("The Lone Event passed :) ")

# puts two events in one club and make sure
def twoEventsInOneClub():
    print("\nTwo Events in One Club Method")

    date_1 = datetime(year= 2019, month = 5, day = 25, hour = 19, minute = 0)
    date_2 = datetime(year= 2020, month = 5, day = 25, hour = 19, minute = 0)

    event_1 = Event("Event_1", date_1, csClub, "Alter Hall Rm 101", "Event 1 :)")

    recommend.addEventToClub("Computer Science Club", "Event_1", date_1, "Alter Hall Rm 101", "Event 1")
    recommend.addEventToClub("Computer Science Club", "Event_2", date_2, "Alter Hall Rm 102", "Event 2")

    csClub.getClubEvents()

    # create the event that I expect to get back
    event = recommend.getNextClubEvent(csClub)
    assert(event_1.getDate() == event.getDate())    # create an assertion to make sure I am getting the right one

    print("Two Events In One Club passed :) ")

# put a third event in the CS club and see how that goes
def thirdEventInOneClub():
    """Putting a third event in the CS Club"""
    print ("\nThe third event in CS Club")

    date_3 = datetime(year = 2019, month = 8, day = 25, hour = 19, minute = 0)

    event_3 = Event("Event_3", date_3, csClub, "Alter Hall Rm 101", "Should be 2nd event in the list :)")

    recommend.addEventToClub("Computer Science Club", "Event_3", date_3, "Alter Hall Rm 103", "Event 3")

    csClub.getClubEvents()

    print("End of Third Event in One Club")

# puts a fourth event in the CS club with a duplicate date and time to make sure it wouldn't go crazy
def fourthEvent():
    """Putting a fourth event in the CS Club"""
    print ("\nThe fourth event in CS Club => has the same date as the 3rd event")

    date_3 = datetime(year = 2019, month = 8, day = 25, hour = 19, minute = 0)

    event_3 = Event("Event_4", date_3, csClub, "Alter Hall Rm 101", "Should be 3rd event in the list :)")

    recommend.addEventToClub("Computer Science Club", "Event_4", date_3, "Alter Hall Rm 103", "Event 4")

    csClub.getClubEvents()

    print("End of Fourth Event")

theLoneEvent()
twoEventsInOneClub()
thirdEventInOneClub()
fourthEvent()
