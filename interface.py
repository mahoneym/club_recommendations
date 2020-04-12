from tkinter import *
import tkinter.messagebox
from datetime import datetime

import recommender
import admin_section
import next_event
import user_events
from constants import topRightCorner, wholeRow, errorBoxTop, id_errorMessage, dateFormat, backgroundColor, foregroundColor, secondWindowBackground, secondWindowForeground, singleLineLeftJustify

interface = Tk()        # create the interface

directions = "Welcome to the club recommender! Please enter your Student ID in the box below."

nextEventTitle = ""
nextEventLocation = ""
nextEventDescription = ""
nextEventDate = None

# called when the user hits the "Club based" Button
# uses the recommender object to get a club recommendation for the user
# knows the user by the student id entered in the text box
def getClubRecommendations():
    # get whatever is in the label
    idNumber = idEntry.get()           # get the user's input
    flag = checkEntryEdgeCases(idNumber)
    if(flag == True):
        graphEdge = recommend.createClubRecommendation(int(idNumber))
        setEventInfo(graphEdge.getDestination())
        # get the recommendations from the recommender object
        if(not (graphEdge == None or type(graphEdge) == type(0))):
            showTheResults(graphEdge.getDestination())
        else:
            clearRecommendationArea()
            tkinter.messagebox.showerror(errorBoxTop, id_errorMessage)
    return None

# called when the user hits the "Interest Based" button
# uses the recommender object to get a interest recommendation for the user
# knows the user by the student id in the box
def getInterestRecommendations():
    idNumber = idEntry.get()        # get the user's input
    flag = checkEntryEdgeCases(idNumber)        # check the idNumber is valid
    club = None
    if(flag == True):               # if the user id is acceptable
        club = recommend.createInterestRecommendation(int(idNumber))    # get the recommendation
        if(club == None):
            clearRecommendationArea()
            tkinter.messagebox.showerror(errorBoxTop, id_errorMessage)
        else:
            setEventInfo(club)  # get the next event info while the club is handy
            showTheResults(club)
    return club

def getUserUpcomingEvents():
    idNumber = idEntry.get()
    if(idNumber == "" or (not checkEntryEdgeCases(idNumber))):
        tkinter.messagebox.showerror(errorBoxTop, id_errorMessage)
        clearRecommendationArea()
    else:
        upcomingEventsList = recommend.getUserUpcomingEvents(int(idNumber))
        user_events.UserEvents(upcomingEventsList)

#eventName, dateInput, locationEntry, descriptionEntry

def adminSection():
    id = idEntry.get()
    if(id == 'Admin'):
        # create instiantiation of admin_section class and let it deal with everything
        admin = admin_section.AdminSection(recommend)
    else:
        clearRecommendationArea()


# sets up event info for when/if the user wants to see the next event
# param: the club object that is being used
def setEventInfo(club):
    global nextEventTitle, nextEventLocation, nextEventDescription, nextEventDate
    nextEvent = recommend.getNextClubEvent(club)
    if(not nextEvent == None):
        clubEventButton["state"] = "normal"
        nextEventTitle = nextEvent.getName()
        nextEventLocation = nextEvent.getLocation()
        nextEventDescription = nextEvent.getDescription()
        nextEventDate = nextEvent.getDate().strftime(dateFormat)        # gets the date and puts in "Sat May 25 2019 7:00 PM" format
    else:
        clubEventButton["state"] = "disabled"

# show the results of the recommendation
def showTheResults(club):
    if(club == -1):
        clearRecommendationArea()
        tkinter.messagebox.showerror(errorBoxTop, id_errorMessage)
    else:
        clubNameInterface.configure(text = club.getClubName())
        clubDescriptionInterface.configure(text = club.getDescription())
        clubCategoryInterface.configure(text = club.getCategory())

# set up and start the next event pop up window
def getNextEvent():
    next_event.NextEvent(nextEventTitle, nextEventDate, nextEventLocation, nextEventDescription)

# make sure the user's entry is all digits
# if it's not, tell them to go back and check their ALLCARD
def checkEntryEdgeCases(idNumber):
    flag = True
    if(not idNumber.isdigit()):
        clearRecommendationArea()
        tkinter.messagebox.showerror(errorBoxTop, id_errorMessage)
        flag = False
    return flag

# clears the recommendation and event info area
def clearRecommendationArea():
    global nextEventTitle, nextEventLocation, nextEventDescription, nextEventDate

    # delete the recommended club's info
    clubNameInterface.configure(text="")
    clubDescriptionInterface.configure(text="")
    clubCategoryInterface.configure(text = "")

    # clean the event pop up
    nextEventTitle = ""
    nextEventLocation = ""
    nextEventDescription = ""
    nextEventDate = None

    idEntry.delete(0,'end')     # clears the user's input in the entry box


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
    date_2 = datetime(year= 2020, month = 5, day = 25, hour = 19, minute = 0)

    # add events to some clubs
    recommend.addEventToClub("Computer Science Club", "Event_1", date_1, "Alter Hall Rm 101", "This is a longer description to play with text wrapping. The first event that is added to the clubs. It should be showing up for CS club.")
    recommend.addEventToClub("Computer Science Club", "Event_1_2", date_1_2, "Alter Hall Rm 101", "This is a longer description to play with text wrapping. The first event that is added to the clubs. It should be showing up for CS club.")
    recommend.addEventToClub("4 Paws for Ability at XU", "Event_2", date_2, "Alter Hall Rm 102", "Event 2")

    recommend.addEventToClub("Don't Tell Anna", "Spring Show", date_2, "Kennedy Auditorium", "Spring Show")
    recommend.addEventToClub("MuskieTHON", "Dance Marathon", date_2, "GSC", "The 24 Hour Dance Marathon")
    return None

######## THE AREA TO GET USER'S ID ##########
recommend = recommender.Recommender()                                                            # starts the recommender object
addData()                                                                                        # adds the data to the recommender

interface.title("Club Recommendation System")
interface.geometry("550x550")                                                                    # sets minimal size of the window when it first opens
interface.configure(background=backgroundColor)                                                  # sets background color to midnight blue

directionsLabel = Label(interface, text=directions, fg=foregroundColor, background= backgroundColor, wraplength = 550, justify = LEFT)
directionsLabel.grid(row=0, column=0, columnspan=4)

takeUpSpace = Label(interface, background=backgroundColor)
takeUpSpace.grid(row=1)

# set up the label for the Student ID
idLabel = Label(interface, text="Student ID:", fg = foregroundColor, background = backgroundColor)
idLabel.grid(row = 2, column = 0, sticky = singleLineLeftJustify)

# set up the text box for the user to put their student ID
idEntry = Entry(interface)
idEntry.grid(row = 2 , column = 1)

# set up the submit button, which will trigger the looking for recommendations
clubButton = Button(interface, text = "Club Based", command = getClubRecommendations)
clubButton.grid(row = 2, column = 2, padx = 6, sticky = wholeRow)

interestButton = Button(interface, text="Interest Based", command = getInterestRecommendations)
interestButton.grid(row = 2, column = 3, padx = 2, sticky = wholeRow)

######## THE AREA TO SHOW THE RECOMMENDATION ########

# the justify attribute only works on wrapped text
# sticky = "W" is the justify left for non-wrapped text in labels

# have the row here just so there's some space between the input and the club recommendations
rowOneLayer = Label(interface, background = backgroundColor)
rowOneLayer.grid(row = 3)

# create labels that will show what information is being displayed
clubNameLabel = Label(interface, text = "Club name: ", background = backgroundColor, fg = foregroundColor)
clubNameLabel.grid(row = 4, column = 0, sticky = singleLineLeftJustify)

clubCategoryLabel = Label(interface, text = "Club Category: ", background = backgroundColor, fg = foregroundColor)
clubCategoryLabel.grid(row = 5, column = 0, sticky=topRightCorner)

clubDescriptionLabel = Label(interface, text = "Description: ", background = backgroundColor, fg = foregroundColor)
clubDescriptionLabel.grid(row = 6, column = 0, sticky = topRightCorner)

# create the labels that will display a specific club recommendation
clubNameInterface = Label(interface, text= "", background = backgroundColor, fg = foregroundColor)
clubNameInterface.grid(row = 4, column = 1, columnspan = 3, sticky = singleLineLeftJustify)

clubCategoryInterface = Label(interface, text="", background = backgroundColor, fg = foregroundColor)
clubCategoryInterface.grid(row=5, column = 1, columnspan = 3, sticky=singleLineLeftJustify)

clubDescriptionInterface = Label(interface, text="", background= backgroundColor, fg = foregroundColor, wraplength = 400, justify = LEFT)
clubDescriptionInterface.grid(row=6, column= 1, columnspan = 3, sticky = singleLineLeftJustify)

takeUpSpace = Label(interface, background=backgroundColor)
takeUpSpace.grid(row=7)

clubEventButton = Button(interface, text = "Get Next Event", state = "disabled", command = getNextEvent)
clubEventButton.grid(row = 8, columnspan = 5, padx = 6, sticky = wholeRow)

rowOneLayer = Label(interface, background = backgroundColor)
rowOneLayer.grid(row = 9)

upcomingEventsButton = Button(interface, text= "Get Upcoming Events for my Clubs", command = getUserUpcomingEvents)
upcomingEventsButton.grid(row = 10, columnspan = 4 , padx = 6, sticky = wholeRow)

space = Label(interface, background = backgroundColor, fg = foregroundColor)
space.grid(row = 11)

space_2 = Label(interface, background = backgroundColor, fg = foregroundColor)
space.grid(row = 12)

admin = Button(interface, text = "Admin", command = adminSection)
admin.grid(row=13, columnspan = 4, sticky = wholeRow)

######## START THE PROGRAM ########
interface.mainloop()
