from tkinter import *
import tkinter.messagebox
from datetime import datetime

from Interface_Classes import admin_section
from Interface_Classes import next_event
from Interface_Classes import user_events
from constants import TOP_RIGHT_CORNER, WHOLE_ROW, ERROR_BOX_TOP, ID_ERROR_MESSAGE, DATE_FORMAT, BACKGROUND_COLOR, FOREGROUND_COLOR, SECOND_WINDOW_BACKGROUND, SECOND_WINDOW_FOREGROUND, SINGLE_LINE_LEFT_JUSTIFY


class MainWindow:
    """The first window that the users sees and it controls everything else"""

    nextEventTitle = ""
    nextEventLocation = ""
    nextEventDescription = ""
    nextEventDate = None

    # the constructor for the main window of the application
    # THIS WILL START THE MAIN WINDOW
    # param: the recommender object
    # returns: None
    def __init__(self, recommender):
        global recommend, idEntry, clubEventButton, clubNameInterface,clubDescriptionInterface, clubCategoryInterface

        recommend = recommender

        directions = "Welcome to the club recommender! Please enter your Student ID in the box below."

        interface = Tk()        # create the interface

        interface.title("Club Recommendation System")
        interface.geometry("550x550")                                                                    # sets minimal size of the window when it first opens
        interface.configure(background = BACKGROUND_COLOR)                                                  # sets background color to midnight blue

        ######## THE AREA TO GET USER'S ID ##########
        directionsLabel = Label(interface, text = directions, fg=FOREGROUND_COLOR, background= BACKGROUND_COLOR, wraplength = 550, justify = LEFT)
        directionsLabel.grid(row=0, column=0, columnspan=4)

        takeUpSpace = Label(interface, background=BACKGROUND_COLOR)
        takeUpSpace.grid(row=1)

        # set up the label for the Student ID
        idLabel = Label(interface, text="Student ID:", fg = FOREGROUND_COLOR, background = BACKGROUND_COLOR)
        idLabel.grid(row = 2, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        # set up the text box for the user to put their student ID
        idEntry = Entry(interface)
        idEntry.grid(row = 2 , column = 1)

        # set up the recommendations button, which will trigger the looking for recommendations
        clubButton = Button(interface, text = "Club Based", command = self.getClubRecommendations)
        clubButton.grid(row = 2, column = 2, padx = 6, sticky = WHOLE_ROW)

        interestButton = Button(interface, text="Interest Based", command = self.getInterestRecommendations)
        interestButton.grid(row = 2, column = 3, padx = 2, sticky = WHOLE_ROW)

        ######## THE AREA TO SHOW THE RECOMMENDATION ########

        # the justify attribute only works on wrapped text
        # sticky = "W" is the justify left for non-wrapped text

        # have the row here just so there's some space between the input and the club recommendations
        rowOneLayer = Label(interface, background = BACKGROUND_COLOR)
        rowOneLayer.grid(row = 3)

        # create labels that will show what information is being displayed
        clubNameLabel = Label(interface, text = "Club name: ", background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        clubNameLabel.grid(row = 4, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        clubCategoryLabel = Label(interface, text = "Club Category: ", background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        clubCategoryLabel.grid(row = 5, column = 0, sticky=TOP_RIGHT_CORNER)

        clubDescriptionLabel = Label(interface, text = "Description: ", background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        clubDescriptionLabel.grid(row = 6, column = 0, sticky = TOP_RIGHT_CORNER)

        # create the labels that will display a specific club recommendation
        clubNameInterface = Label(interface, text= "", background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        clubNameInterface.grid(row = 4, column = 1, columnspan = 3, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        clubCategoryInterface = Label(interface, text="", background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        clubCategoryInterface.grid(row=5, column = 1, columnspan = 3, sticky=SINGLE_LINE_LEFT_JUSTIFY)

        clubDescriptionInterface = Label(interface, text="", background= BACKGROUND_COLOR, fg = FOREGROUND_COLOR, wraplength = 400, justify = LEFT)
        clubDescriptionInterface.grid(row=6, column= 1, columnspan = 3, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        takeUpSpace = Label(interface, background=BACKGROUND_COLOR)
        takeUpSpace.grid(row=7)

        clubEventButton = Button(interface, text = "Get Next Event", state = "disabled", command = self.getNextEvent)
        clubEventButton.grid(row = 8, columnspan = 5, padx = 6, sticky = WHOLE_ROW)

        rowOneLayer = Label(interface, background = BACKGROUND_COLOR)
        rowOneLayer.grid(row = 9)

        upcomingEventsButton = Button(interface, text= "Get Upcoming Events for my Clubs", command = self.getUserUpcomingEvents)
        upcomingEventsButton.grid(row = 10, columnspan = 4 , padx = 6, sticky = WHOLE_ROW)

        space = Label(interface, background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        space.grid(row = 11)

        space_2 = Label(interface, background = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        space.grid(row = 12)

        admin = Button(interface, text = "Admin", command = self.adminSection)
        admin.grid(row=13, columnspan = 4, sticky = WHOLE_ROW)

        ######## START THE PROGRAM ########
        interface.mainloop()

        return None

    # called when the user hits the "Club based" Button
    # uses the recommender object to get a club recommendation for the user
    # knows the user by the student id entered in the text box
    def getClubRecommendations(self):
        # get whatever is in the label
        idNumber = idEntry.get()           # get the user's input
        flag = self.checkEntryEdgeCases(idNumber)
        if(flag == True):
            graphEdge = recommend.createClubRecommendation(int(idNumber))
            self.setEventInfo(graphEdge.getDestination())
            # get the recommendations from the recommender object
            if(not (graphEdge == None or type(graphEdge) == type(0))):
                self.showTheResults(graphEdge.getDestination())
            else:
                self.clearRecommendationArea()
                tkinter.messagebox.showerror(ERROR_BOX_TOP, ID_ERROR_MESSAGE)
        return None

    # called when the user hits the "Interest Based" button
    # uses the recommender object to get a interest recommendation for the user
    # knows the user by the student id in the box
    # param: none
    # returns: the club
    def getInterestRecommendations(self):
        idNumber = idEntry.get()        # get the user's input
        flag = self.checkEntryEdgeCases(idNumber)        # check the idNumber is valid
        club = None
        if(flag == True):               # if the user id is acceptable
            club = recommend.createInterestRecommendation(int(idNumber))    # get the recommendation
            if(club == None):
                self.clearRecommendationArea()
                tkinter.messagebox.showerror(ERROR_BOX_TOP, ID_ERROR_MESSAGE)
            else:
                self.setEventInfo(club)  # get the next event info while the club is handy
                self.showTheResults(club)
        return club

    # gets the user's upcoming events
    # gets called when the user hits the "Get Upcoming Events for my Clubs" button
    # param: none
    # returns: nothing
    def getUserUpcomingEvents(self):
        idNumber = idEntry.get()
        if(idNumber == "" or (not self.checkEntryEdgeCases(idNumber))):
            self.clearRecommendationArea()
        else:
            upcomingEventsList = recommend.getUserUpcomingEvents(int(idNumber))
            user_events.UserEvents(upcomingEventsList)      # start user upcoming events GUI

    # starts the admin section
    # param: none
    # returns: nothing
    def adminSection(self):
        id = idEntry.get()
        if(id == 'Admin'):
            # create instiantiation of admin_section class and let it deal with everything
            admin = admin_section.AdminSection(recommend)
        else:
            self.clearRecommendationArea()

    # sets up event info for when/if the user wants to see the next event
    # param: the club object that is being used
    # returns: nothing
    def setEventInfo(self, club):
        global nextEventTitle, nextEventLocation, nextEventDescription, nextEventDate
        nextEvent = recommend.getNextClubEvent(club)
        if(not nextEvent == None):
            clubEventButton["state"] = "normal"
            self.nextEventTitle = nextEvent.getName()
            self.nextEventLocation = nextEvent.getLocation()
            self.nextEventDescription = nextEvent.getDescription()
            self.nextEventDate = nextEvent.getDate().strftime(DATE_FORMAT)        # gets the date and puts in "Sat May 25 2019 7:00 PM" format
        else:
            clubEventButton["state"] = "disabled"

    # show the results of the recommendation
    # param: the club object
    # returns: nothing
    def showTheResults(self, club):
        if(club == -1):
            self.clearRecommendationArea()
            tkinter.messagebox.showerror(ERROR_BOX_TOP, ID_ERROR_MESSAGE)
        else:
            clubNameInterface.configure(text = club.getClubName())
            clubDescriptionInterface.configure(text = club.getDescription())
            clubCategoryInterface.configure(text = club.getCategory())

    # set up and start the next event pop up window
    # param: none
    # returns: nothing
    def getNextEvent(self):
        next_event.NextEvent(self.nextEventTitle, self.nextEventDate, self.nextEventLocation, self.nextEventDescription)

    # make sure the user's entry is all digits; if it's not, tell them to go back and check their ALLCARD
    # param: the student's idNumber (integer)
    # returns: True if the idNumber is valid; o.w. returns False
    def checkEntryEdgeCases(self, idNumber):
        flag = True
        if(not idNumber.isdigit()):
            self.clearRecommendationArea()
            tkinter.messagebox.showerror(ERROR_BOX_TOP, ID_ERROR_MESSAGE)
            flag = False
        return flag

    # clears the recommendation and event info area
    # param: none
    # returns: nothing
    def clearRecommendationArea(self):
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
