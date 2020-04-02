from tkinter import *
import tkinter.messagebox
import recommender

interface = Tk()

directions = "Welcome to the club recommender! Please enter your Student ID in the box below."
erroxBoxTop = "Oops"
errorMessage = "An error occured. Please check your ID Number on your AllCard and try again."
backgroundColor = "midnight blue"
foregroundColor = "gray64"

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

def getInterestRecommendations():
    idNumber = idEntry.get()
    flag = checkEntryEdgeCases(idNumber)
    club = None
    if(flag == True):
        club = recommend.createInterestRecommendation(int(idNumber))
        setEventInfo(club)
        if(club == None):
            clearRecommendationArea()
            tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
        else:
            showTheResults(club)
    return club

def setEventInfo(club):
    global nextEventTitle, nextEventLocation, nextEventDescription
    nextEvent = recommend.getNextClubEvent(club)
    if(not nextEvent == None):
        nextEventTitle = nextEvent.getName()
        nextEventLocation = nextEvent.getLocation()
        nextEventDescription = nextEvent.getDescription()

def showTheResults(club):
    if(club == -1):
        clearRecommendationArea()
        tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
    else:
        clubNameInterface.configure(text = club.getClubName())
        clubDescriptionInterface.configure(text = club.getDescription())
        clubCategoryInterface.configure(text = club.getCategory())

def getNextEvent():
    #tkinter.messagebox.showerror("YES", "THIS WILL BE ADDED AT A LATER DATE!")
    eventPopUp = Tk()
    #eventPopUp = Toplevel()
    eventPopUp.wm_title("Next Event")
    eventPopUp.configure(background = foregroundColor)                                                  # sets background color to midnight blue
    eventPopUp.geometry("400x300")

    title = Label(eventPopUp, text = "Event Title: ", background = foregroundColor, fg = backgroundColor)
    title.grid(row = 0, column = 0, sticky= "W")

    location = Label(eventPopUp, text = "Event Location: ", background = foregroundColor, fg = backgroundColor)
    location.grid(row = 1, column = 0, sticky= "W")

    description = Label(eventPopUp, text = "Event Description", background = foregroundColor, fg = backgroundColor)
    description.grid(row = 2, column = 0, sticky= "W")

    eventTitle = Label(eventPopUp, text = nextEventTitle, background = foregroundColor, fg = backgroundColor)
    eventTitle.grid(row = 0, column = 1, sticky= "W")

    eventLocation = Label(eventPopUp, text = nextEventLocation, background = foregroundColor, fg = backgroundColor)
    eventLocation.grid(row = 1, column = 1, sticky= "W")

    eventDescription = Label(eventPopUp, text = nextEventDescription, background = foregroundColor, fg = backgroundColor)
    eventDescription.grid(row = 2, column = 1, sticky= "W")

    filler = Label(eventPopUp, background = foregroundColor)
    filler.grid(row = 3, sticky = "W")

    emailMeButton = Button(eventPopUp, text = "Email Me this Event")
    emailMeButton.grid(row = 4, columnspan = 2, sticky = "NSEW")

def checkEntryEdgeCases(idNumber):
    flag = True
    if(not idNumber.isdigit()):
        clearRecommendationArea()
        tkinter.messagebox.showerror(erroxBoxTop, errorMessage)
        flag = False
    return flag

def clearRecommendationArea():
    # delete the recommended club's info
    clubNameInterface.configure(text="")
    clubDescriptionInterface.configure(text="")
    clubCategoryInterface.configure(text = "")

    nextEventTitle = ""
    nextEventLocation = ""
    nextEventDescription = ""
    # clears the user's input in the entry box
    idEntry.delete(0,'end')

def addData():
    global u1, u2, u3, u4, u5

    u1 = recommend.addUser(1)
    u2 = recommend.addUser(2)
    u3 = recommend.addUser(3)
    u4 = recommend.addUser(4)
    u5 = recommend.addUser(5)

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
    return None

######## THE AREA TO GET USER'S ID ##########
recommend = recommender.Recommender()               # starts the recommender object
addData()

interface.title("Club Recommendation System")
interface.geometry("575x375")                                                                    # sets minimal size of the window when it first opens
interface.configure(background=backgroundColor)                                                  # sets background color to midnight blue


nextEventTitle = ""
nextEventLocation = ""
nextEventDescription = ""

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

clubEventButton = Button(interface, text = "Get Next Event", command=getNextEvent)
clubEventButton.grid(row = 8, columnspan = 5, padx = 6, sticky="NSEW")


######## START THE PROGRAM ########
interface.mainloop()
