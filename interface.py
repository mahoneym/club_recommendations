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

#usernameLabel = Label(interface, text="Student ID", y = 75, x = 0)

button1 = Button(interface, text = "Submit", command = "getRecommendations()")
button1.place(x = 270, y = 75)

nameEntry = Entry(interface)
nameEntry.place(x = 75, y = 75)

interface.mainloop()
