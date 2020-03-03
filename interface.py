from tkinter import *
import tkinter.messagebox
import recommender

# I want to use a grid system so i don't have to play with pixels all the time

######## THE AREA TO GET USER'S ID ########

def getRecommendations():
    # get whatever is in the label
    idNumber = nameEntry.get()           # get the user's input
    club = recommend.createUserRecommendations(idNumber)
    # get the recommendations from the recommender object
    if(club == -1):
        tkinter.messagebox.showerror("Oops", "Your student ID was not found. Please make sure it is correct and try again.")
    else:
        print(club.getClubName())
    return None

def addData():
    global u1, u2, u3, u4

    u1 = recommend.addUser(1)
    u2 - recommend.addUser(2)
    u3 = recommend.addUser(3)
    u4 = recommend.addUser(4)
    u5 = recommend.addUser(5)

    recommendObject.addClub('Computer Science Club', 'Academic', 1)
    recommendObject.addClub('Pep Band', 'Music', 2)
    recommendObject.addClub('A Xavier Christmas', 'Service', 3)
    recommendObject.addClub('Accounting Club', 'Academic', 24)
    recommendObject.addClub("Don't Tell Anna", 'Service', 4)
    recommendObject.addClub('4 Paws for Ability', 'Animals', 5)

    u1.addClub('Pep Band', recommendObject)
    u1.addClub('Computer Science Club', recommendObject)
    u1.addClub("Accounting Club", recommendObject)

    u2.addClub('Pep Band', recommendObject)
    u2.addClub('A Xavier Christmas', recommendObject)
    u2.addClub('Computer Science Club', recommendObject)

    u3.addClub('A Xavier Christmas', recommendObject)
    u3.addClub('4 Paws for Ability', recommendObject)
    u3.addClub("Don't Tell Anna", recommendObject)

    u4.addClub('A Xavier Christmas', recommendObject)
    u4.addClub("Don't Tell Anna", recommendObject)
    u4.addClub('Pep Band', recommendObject)

    u5.addClub("Computer Science Club", recommendObject)
    u5.addClub("Don't Tell Anna", recommendObject)
    u5.addClub('A Xavier Christmas', recommendObject)

    return None

recommend = recommender.Recommender()               # starts the recommender object
addData()


interface = Tk()
interface.title("Club Recommendation System")
interface.geometry("500x250")                                                           # sets minimal size of the window when it first opens
interface.configure(background="navy")                                                  # sets background color to navy

# set up the label for the Student ID
idLabel = Label(interface, text="Student ID:", fg="grey", background="navy")
idLabel.grid(row = 0, column = 0)

# set up the text box for the user to put their student ID
nameEntry = Entry(interface)
nameEntry.grid(row = 0 , column = 1)

# set up the submit button, which will trigger the looking for recommendations
submitButton = Button(interface, text = "Submit", command = getRecommendations)
submitButton.grid(row = 0, column =2, padx=2)

######## THE AREA TO SHOW THE RECOMMENDATION ########
clubName = StringVar(interface)
clubDescription = StringVar(interface)

######## START THE INTERFACE ########
interface.mainloop()
