from tkinter import *

# I want to use a grid system so i don't have tp play with pixels all the time

def getRecommendations():
    # get whatever is in the label
    # get the recommendations from the recommender object
    return None

def showRecommendations():
    return None

interface = Tk()
interface.title("Club Recommendation System")
interface.geometry("500x200")                   # sets minimal size of the window when it first opens
interface.configure(background="navy")          # sets background color to navy


userID = StringVar()
userID.set("Student ID:")

usernameLabel = Label(interface, text="Student ID:", fg="grey", background="navy")
usernameLabel.grid(row = 0, column = 0)

nameEntry = Entry(interface)
#nameEntry.place(x = 75, y = 75)
nameEntry.grid(row = 0 , column = 1)

button1 = Button(interface, text = "Submit", command = "getRecommendations()")
#button1.place(x = 270, y = 75)
button1.grid(row = 0, column =2, padx=2)

interface.mainloop()
