from tkinter import *
import tkinter.messagebox
import recommender

interface = Tk()

def getClubRecommendations():
    # get whatever is in the label
    idNumber = nameEntry.get()           # get the user's input
    flag = checkEntryEdgeCases(idNumber)
    if(flag == True):
        club = recommend.createUserRecommendations(int(idNumber))
        # get the recommendations from the recommender object
        showTheResults(club.getDestination())
    return None

def getInterestRecommendations():
    idNumber = nameEntry.get()
    flag = checkEntryEdgeCases(idNumber)
    club = None
    if(flag == True):
        club = recommend.createInterestRecommendation(int(idNumber))
        if(club == None):
            clearRecommendationArea()
            tkinter.messagebox.showerror("Oops", "You do not have any interests saved in the system. Please try again.")
        else:
            showTheResults(club)
    return club

def showTheResults(club):
    if(club == -1):
        clearRecommendationArea()
        tkinter.messagebox.showerror("Oops", "Your student ID was not found. Please make sure it is correct and try again.")
    else:
        clubNameInterface.configure(text = club.getClubName())
        clubDescriptionInterface.configure(text = club.getDescription())
        clubCategoryInterface.configure(text = club.getCategory())

def checkEntryEdgeCases(idNumber):
    flag = True
    if(not idNumber.isdigit()):
        clearRecommendationArea()
        tkinter.messagebox.showerror("Oops", "Your student ID is a number shown on your AllCard. Please try again.")
        flag = False
    return flag

def clearRecommendationArea():
    # delete the recommended club's info
    clubNameInterface.configure(text="")
    clubDescriptionInterface.configure(text="")
    clubCategoryInterface.configure(text = "")

    # clears the user's input in the entry box
    nameEntry.delete(0,'end')

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
interface.geometry("575x400")                                                           # sets minimal size of the window when it first opens
interface.configure(background="midnight blue")                                                  # sets background color to midnight blue


directions = """Welcome to the club recommender! Please enter your Student ID in the box below."""
# The interest recommendations will pick one of your interests from the Road To Xavier form and choose a related club.

directionsLabel = Label(interface, text=directions, fg="gray64", background="midnight blue", wraplength = 550, justify = LEFT)
directionsLabel.grid(row=0, column=0, columnspan=4)

takeUpSpace = Label(interface, background="midnight blue")
takeUpSpace.grid(row=1)

# set up the label for the Student ID
idLabel = Label(interface, text="Student ID:", fg="gray64", background="midnight blue")
idLabel.grid(row = 2, column = 0, sticky="W")

# set up the text box for the user to put their student ID
nameEntry = Entry(interface)
nameEntry.grid(row = 2 , column = 1)

# set up the submit button, which will trigger the looking for recommendations
clubButton = Button(interface, text = "Club Based", command = getClubRecommendations)
clubButton.grid(row = 2, column = 2, padx = 6)

interestButton = Button(interface, text="Interest Based", command= getInterestRecommendations)
interestButton.grid(row = 2, column = 3, padx = 2)

######## THE AREA TO SHOW THE RECOMMENDATION ########

# the justify attribute only works on wrapped text
# sticky = "W" is the justify left for non-wrapped text in labels

# have the row here just so there's some space between the input and the club recommendations
rowOneLayer = Label(interface, background="midnight blue")
rowOneLayer.grid(row = 3)

# create labels that will show what information is being displayed
clubNameLabel = Label(interface, text="Club name: ", background='midnight blue', fg='gray64')
clubNameLabel.grid(row = 4, column = 0, sticky="W")

clubCategoryLabel = Label(interface, text = "Club Category: ", background = 'midnight blue', fg = 'gray64')
clubCategoryLabel.grid(row = 5, column = 0, sticky="NW")

clubDescriptionLabel = Label(interface, text= "Description:", background='midnight blue', fg = 'gray64')
clubDescriptionLabel.grid(row = 6, column = 0, sticky="NW")

# create the labels that will display a specific club recommendation
clubNameInterface = Label(interface, text= "", background='midnight blue', fg='gray64')
clubNameInterface.grid(row = 4, column = 1, columnspan = 3, sticky="W")

clubCategoryInterface = Label(interface, text="", background = 'midnight blue', fg = 'gray64')
clubCategoryInterface.grid(row=5, column = 1, columnspan = 3, sticky="W")

clubDescriptionInterface = Label(interface, text="", background= 'midnight blue', fg = 'gray64', wraplength = 400, justify = LEFT)
clubDescriptionInterface.grid(row=6, column= 1, columnspan = 3, sticky = "W")

######## START THE PROGRAM ########
interface.mainloop()
