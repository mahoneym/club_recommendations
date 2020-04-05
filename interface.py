from tkinter import *
import tkinter.messagebox
import recommender
from datetime import datetime

interface = Tk()        # create the interface

# create string variables for what is used throughout the interface
directions = "Welcome to the club recommender! Please enter your Student ID in the box below."
erroxBoxTop = "Oops"
errorMessage = "An error occured. Please check your ID Number on your AllCard and try again."
backgroundColor = "midnight blue"
foregroundColor = "gray64"

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
            tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
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
        setEventInfo(club)  # get the next event info while the club is handy
        if(club == None):
            clearRecommendationArea()
            tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
        else:
            showTheResults(club)
    return club

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
        nextEventDate = nextEvent.getDate().strftime("%a %b %d, %Y %I:%M %p")        # gets the date and puts in "Sat May 25 2019 7:00 PM" format
    else:
        clubEventButton["state"] = "disabled"

# show the results of the recommendation
def showTheResults(club):
    if(club == -1):
        clearRecommendationArea()
        tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
    else:
        clubNameInterface.configure(text = club.getClubName())
        clubDescriptionInterface.configure(text = club.getDescription())
        clubCategoryInterface.configure(text = club.getCategory())

# set up and start the next event pop up window
def getNextEvent():
    eventPopUp = Tk()   # start the pop up window

    # set up the pop up window 
    eventPopUp.wm_title("Next Event")
    eventPopUp.configure(background = foregroundColor)                                                  # sets background color to midnight blue
    eventPopUp.geometry("430x200")

    title = Label(eventPopUp, text = "Event Title: ", background = foregroundColor, fg = backgroundColor)
    title.grid(row = 0, column = 0, sticky= "W")

    date = Label(eventPopUp, text = "Event Date", background = foregroundColor, fg = backgroundColor)
    date.grid(row = 1, column = 0, sticky= "W")

    location = Label(eventPopUp, text = "Event Location: ", background = foregroundColor, fg = backgroundColor)
    location.grid(row = 2, column = 0, sticky= "W")

    description = Label(eventPopUp, text = "Event Description", background = foregroundColor, fg = backgroundColor)
    description.grid(row = 3, column = 0, sticky= "NW")

    eventTitle = Label(eventPopUp, text = nextEventTitle, background = foregroundColor, fg = backgroundColor)
    eventTitle.grid(row = 0, column = 1, sticky= "W")

    eventDate = Label(eventPopUp, text = nextEventDate, background = foregroundColor, fg = backgroundColor)
    eventDate.grid(row = 1, column = 1, sticky= "W")

    eventLocation = Label(eventPopUp, text = nextEventLocation, background = foregroundColor, fg = backgroundColor)
    eventLocation.grid(row = 2, column = 1, sticky= "W")

    eventDescription = Label(eventPopUp, text = nextEventDescription, background = foregroundColor, fg = backgroundColor, wraplength = 300, justify = LEFT)
    eventDescription.grid(row = 3, column = 1, sticky= "W")

    filler = Label(eventPopUp, background = foregroundColor, text = "")
    filler.grid(row = 4, sticky = "W")

    #emailMeButton = Button(eventPopUp, text = "Email Me this Event")
    #emailMeButton.grid(row = 5, columnspan = 2, sticky = "NSEW")

# make sure the user's entry is all digits
# if it's not, tell them to go back and check their ALLCARD
def checkEntryEdgeCases(idNumber):
    flag = True
    if(not idNumber.isdigit()):
        clearRecommendationArea()
        tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
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
    date_2 = datetime(year= 2020, month = 5, day = 25, hour = 19, minute = 0)

    # add events to some clubs
    recommend.addEventToClub("Computer Science Club", "Event_1", date_1, "Alter Hall Rm 101", "This is a longer description to play with text wrapping. The first event that is added to the clubs. It should be showing up for CS club.")
    recommend.addEventToClub("4 Paws for Ability at XU", "Event_2", date_2, "Alter Hall Rm 102", "Event 2")
    return None

######## THE AREA TO GET USER'S ID ##########
recommend = recommender.Recommender()                                                            # starts the recommender object
addData()                                                                                        # adds the data to the recommender

interface.title("Club Recommendation System")
interface.geometry("550x550")                                                                    # sets minimal size of the window when it first opens
interface.configure(background=backgroundColor)                                                  # sets background color to midnight blue


nextEventTitle = ""
nextEventLocation = ""
nextEventDescription = ""
nextEventDate = None

# The interest recommendations will pick one of your interests from the Road To Xavier form and choose a related club.

directionsLabel = Label(interface, text=directions, fg=foregroundColor, background= backgroundColor, wraplength = 550, justify = LEFT)
directionsLabel.grid(row=0, column=0, columnspan=4)

takeUpSpace = Label(interface, background=backgroundColor)
takeUpSpace.grid(row=1)

# set up the label for the Student ID
idLabel = Label(interface, text="Student ID:", fg=foregroundColor, background=backgroundColor)
idLabel.grid(row = 2, column = 0, sticky="W")

# set up the text box for the user to put their student ID
idEntry = Entry(interface)
idEntry.grid(row = 2 , column = 1)

# set up the submit button, which will trigger the looking for recommendations
clubButton = Button(interface, text = "Club Based", command = getClubRecommendations)
clubButton.grid(row = 2, column = 2, padx = 6, sticky="NSEW")

interestButton = Button(interface, text="Interest Based", command= getInterestRecommendations)
interestButton.grid(row = 2, column = 3, padx = 2, sticky = "NSEW")

######## THE AREA TO SHOW THE RECOMMENDATION ########

# the justify attribute only works on wrapped text
# sticky = "W" is the justify left for non-wrapped text in labels

# have the row here just so there's some space between the input and the club recommendations
rowOneLayer = Label(interface, background=backgroundColor)
rowOneLayer.grid(row = 3)

# create labels that will show what information is being displayed
clubNameLabel = Label(interface, text="Club name: ", background=backgroundColor, fg=foregroundColor)
clubNameLabel.grid(row = 4, column = 0, sticky="W")

clubCategoryLabel = Label(interface, text = "Club Category: ", background = backgroundColor, fg = foregroundColor)
clubCategoryLabel.grid(row = 5, column = 0, sticky="NW")

clubDescriptionLabel = Label(interface, text= "Description: ", background=backgroundColor, fg = foregroundColor)
clubDescriptionLabel.grid(row = 6, column = 0, sticky="NW")

# create the labels that will display a specific club recommendation
clubNameInterface = Label(interface, text= "", background=backgroundColor, fg=foregroundColor)
clubNameInterface.grid(row = 4, column = 1, columnspan = 3, sticky="W")

clubCategoryInterface = Label(interface, text="", background = backgroundColor, fg = foregroundColor)
clubCategoryInterface.grid(row=5, column = 1, columnspan = 3, sticky="W")

clubDescriptionInterface = Label(interface, text="", background= backgroundColor, fg = foregroundColor, wraplength = 400, justify = LEFT)
clubDescriptionInterface.grid(row=6, column= 1, columnspan = 3, sticky = "W")

takeUpSpace = Label(interface, background=backgroundColor)
takeUpSpace.grid(row=7)

clubEventButton = Button(interface, text = "Get Next Event", state="disabled", command=getNextEvent)
clubEventButton.grid(row = 8, columnspan = 5, padx = 6, sticky="NSEW")

######## START THE PROGRAM ########
interface.mainloop()
