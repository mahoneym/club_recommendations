from tkinter import *
import tkinter.messagebox
import recommender

# I want to use a grid system so i don't have to play with pixels all the time

######## THE AREA TO GET USER'S ID ########

def getRecommendations():
    # get whatever is in the label
    # get the recommendations from the recommender object
    tkinter.messagebox.showerror("Oops", "Your student ID was not found. Please make sure it is correct and try again.")
    return None

def showRecommendations():
    return None

interface = Tk()
interface.title("Club Recommendation System")
interface.geometry("500x250")                                                           # sets minimal size of the window when it first opens
interface.configure(background="navy")                                                  # sets background color to navy

# set up the label for the Student ID
usernameLabel = Label(interface, text="Student ID:", fg="grey", background="navy")
usernameLabel.grid(row = 0, column = 0)

# set up the text box for the user to put their student ID
nameEntry = Entry(interface)
nameEntry.grid(row = 0 , column = 1)

# set up the submit button, which will trigger the looking for recommendations
submitButton = Button(interface, text = "Submit", command = getRecommendations)
submitButton.grid(row = 0, column =2, padx=2)

######## THE AREA TO SHOW THE RECOMMENDATION ########


######## START THE INTERFACE ########
interface.mainloop()
