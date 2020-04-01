import recommender
from event import *
from datetime import datetime

recommend = recommender.Recommender()

# get some clubs to play with
csClub = recommend.getClub("Computer Science Club")

def theLoneEvent():
    print("The Lone Event")

    # create event_1 for the CS club
    date_1 = datetime(year= 2020, month = 5, day = 25, hour = 19, minute = 0)
    event_1 = Event("Event_1", date_1, csClub, "Alter hall", "It's the first event. :)")
    recommend.addEventToClub('Computer Science Club', "Event_1", date_1, "CS Lab", "It's the first event. :)")

    # try to get event 1 back from CS club list
    print("Trying to get the event back")
    event = recommend.getNextClubEvent(csClub)
    assert(not event == None)
    assert(event_1.getName() == event.getName())
    print("assertion for CS club event passed :) ")

def twoEventsInOneClub():
    print("Two Events in One Club Method")

    date_1 = datetime(year= 2019, month = 5, day = 25, hour = 19, minute = 0)
    date_2 = datetime(year= 2020, month = 5, day = 25, hour = 19, minute = 0)

    #event_1 = Event()
    #event_2 = Event()

    recommend.addEventToClub("Computer Science Club", "Event_1", date_1, "Alter Hall Rm 101", "Event 1")
    recommend.addEventToClub("Computer Science Club", "Event_2", date_2, "Alter Hall Rm 102", "Event 2")

    csClub.getClubEvents()

#theLoneEvent()
twoEventsInOneClub()
