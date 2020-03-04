from tkinter import *
import tkinter.messagebox
import recommender

# I want to use a grid system so i don't have to play with pixels all the time

######## THE AREA TO GET USER'S ID ########

interface = Tk()

def getRecommendations():
    # get whatever is in the label
    idNumber = nameEntry.get()           # get the user's input
    print(str(idNumber))
    if(idNumber == ''):
        tkinter.messagebox.showerror("Oops", "Please enter your student ID.")
    else:
        club = recommend.createUserRecommendations(int(idNumber))
        # get the recommendations from the recommender object
        if(club == -1):
            clubNameInterface.configure(text="")
            clubDescriptionInterface.configure(text="")
            clubCategoryInterface.configure(text = "")

            tkinter.messagebox.showerror("Oops", "Your student ID was not found. Please make sure it is correct and try again.")
        else:
            print(club.getDestination().getClubName())

            clubNameInterface.configure(text = club.getDestination().getClubName())
            clubDescriptionInterface.configure(text = club.getDestination().getDescription())
            clubCategoryInterface.configure(text = club.getDestination().getCategory())

        return None

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

recommend = recommender.Recommender()               # starts the recommender object
addData()


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
clubButton = Button(interface, text = "Club Based", command = getRecommendations)
clubButton.grid(row = 0, column = 2, padx = 6)

#interestButton = Button(interface, text="Interest Based", command= getRecommendations)
#interestButton.grid(row = 1, column = 2, padx = 2)

######## THE AREA TO SHOW THE RECOMMENDATION ########

#have the row here just so there's some space between the input and the club recommendations
rowOneLayer = Label(interface, background="navy")
rowOneLayer.grid(row = 1)

# create labels that will show what information is being displayed
clubNameLabel = Label(interface, text="Club name: ", background='navy', fg='grey')
clubNameLabel.grid(row = 2, column = 0)

clubDescriptionLabel = Label(interface, text= "Description:", background='navy', fg = 'grey')
clubDescriptionLabel.grid(row = 3, column = 0)

clubCategoryLabel = Label(interface, text = "Club Category: ", background = 'navy', fg = 'grey')
clubCategoryLabel.grid(row = 4, column = 0)


# create the labels that will display a specific club recommendation
clubNameInterface = Label(interface, text= "", background='navy', fg='grey')
clubNameInterface.grid(row = 2, column = 1)

clubDescriptionInterface = Label(interface, text="", background= 'navy', fg = 'grey')
clubDescriptionInterface.grid(row=3, column= 1)

clubCategoryInterface = Label(interface, text="", background = 'navy', fg = 'grey')
clubCategoryInterface.grid(row=4, column = 1)

######## START THE INTERFACE ########
interface.mainloop()
