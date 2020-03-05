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
        if(club == -1):
            clearRecommendationArea()
            tkinter.messagebox.showerror("Oops", "Your student ID was not found. Please make sure it is correct and try again.")
        else:
            clubNameInterface.configure(text = club.getDestination().getClubName())
            clubDescriptionInterface.configure(text = club.getDestination().getDescription())
            clubCategoryInterface.configure(text = club.getDestination().getCategory())
    return None

def getInterestRecommendations():
    idNumber = nameEntry.get()
    flag = checkEntryEdgeCases(idNumber)
    if(flag == True):
        a = 1 + 1
    return None

def checkEntryEdgeCases(idNumber):
    flag = True
    if(not idNumber.isdigit()):
        clearRecommendationArea()
        tkinter.messagebox.showerror("Oops", "Your student ID is a number shown on your AllCard. Please try again.")
        flag = False
    elif(idNumber == ''):
        tkinter.messagebox.showerror("Oops", "Please enter your student ID.")
        flag = False
    else:
        flag = True
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

    recommend.addClub('Computer Science Club', 'Academic', 1)
    recommend.addClub('Pep Band', 'Music', 2)
    recommend.addClub('A Xavier Christmas', 'Service', 3)
    recommend.addClub('Accounting Club', 'Academic', 24)
    recommend.addClub("Don't Tell Anna", 'Service', 4)
    recommend.addClub('4 Paws for Ability', 'Animals', 5)

    u1.addClub('Pep Band', recommend)
    u1.addClub('Computer Science Club', recommend)
    u1.addClub("Accounting Club", recommend)

    u2.addClub('Pep Band', recommend)
    u2.addClub('A Xavier Christmas', recommend)
    u2.addClub('Computer Science Club', recommend)

    u3.addClub('A Xavier Christmas', recommend)
    u3.addClub('4 Paws for Ability', recommend)
    u3.addClub("Don't Tell Anna", recommend)

    u4.addClub('A Xavier Christmas', recommend)
    u4.addClub("Don't Tell Anna", recommend)
    u4.addClub('Pep Band', recommend)

    u5.addClub("Computer Science Club", recommend)
    u5.addClub("Don't Tell Anna", recommend)
    u5.addClub('A Xavier Christmas', recommend)

    return None

######## THE AREA TO GET USER'S ID ########
recommend = recommender.Recommender()               # starts the recommender object
addData()

interface.title("Club Recommendation System")
interface.geometry("525x425")                                                           # sets minimal size of the window when it first opens
interface.configure(background="midnight blue")                                                  # sets background color to midnight blue

# set up the label for the Student ID
idLabel = Label(interface, text="Student ID:", fg="gray64", background="midnight blue")
idLabel.grid(row = 0, column = 0)

# set up the text box for the user to put their student ID
nameEntry = Entry(interface)
nameEntry.grid(row = 0 , column = 1)

# set up the submit button, which will trigger the looking for recommendations
clubButton = Button(interface, text = "Club Based", command = getClubRecommendations)
clubButton.grid(row = 0, column = 2, padx = 6)

interestButton = Button(interface, text="Interest Based", command= getInterestRecommendations)
interestButton.grid(row = 0, column = 3, padx = 2)

######## THE AREA TO SHOW THE RECOMMENDATION ########

# have the row here just so there's some space between the input and the club recommendations
rowOneLayer = Label(interface, background="midnight blue")
rowOneLayer.grid(row = 1)

# create labels that will show what information is being displayed
clubNameLabel = Label(interface, text="Club name: ", background='midnight blue', fg='gray64')
clubNameLabel.grid(row = 2, column = 0)

clubDescriptionLabel = Label(interface, text= "Description:", background='midnight blue', fg = 'gray64')
clubDescriptionLabel.grid(row = 3, column = 0)

clubCategoryLabel = Label(interface, text = "Club Category: ", background = 'midnight blue', fg = 'gray64')
clubCategoryLabel.grid(row = 4, column = 0)

# create the labels that will display a specific club recommendation
clubNameInterface = Label(interface, text= "", background='midnight blue', fg='gray64')
clubNameInterface.grid(row = 2, column = 1)

clubDescriptionInterface = Label(interface, text="", background= 'midnight blue', fg = 'gray64', wraplength = 400, justify = LEFT)
clubDescriptionInterface.grid(row=3, column= 1, columnspan = 3)

clubCategoryInterface = Label(interface, text="", background = 'midnight blue', fg = 'gray64')
clubCategoryInterface.grid(row=4, column = 1)

######## START THE PROGRAM ########
interface.mainloop()
