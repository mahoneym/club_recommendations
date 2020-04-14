from constants import dateFormat, secondWindowBackground, secondWindowForeground, singleLineLeftJustify, secondWindowWrap
from tkinter import *

class UserEvents:
    """The Class for the User's Upcoming Events GUI"""

    # constructor for the User Events window
    # this will start the user event's window
    # param: a list of upcoming events (events objects) for a given user
    # returns: nothing
    def __init__(self, upcomingEventsList):
        __eventsList = Tk()
        __eventsList.configure(background=secondWindowBackground)
        __eventsList.wm_title("My Upcoming Events")

        index = 0
        rowsPerEvent = 6
        while(index < len(upcomingEventsList)):

            currentEvent = upcomingEventsList[index]
            name = Label(__eventsList, text= "Name: ", background=secondWindowBackground, fg = secondWindowForeground)
            name.grid(row= (rowsPerEvent*index) + 1, column = 0, sticky = singleLineLeftJustify)

            club = Label(__eventsList, text= "Club: ", background=secondWindowBackground, fg = secondWindowForeground)
            club.grid(row = (rowsPerEvent*index) +2, column = 0, sticky = singleLineLeftJustify)

            date = Label(__eventsList, text = "Date: ", background=secondWindowBackground, fg = secondWindowForeground)
            date.grid(row = (rowsPerEvent*index) + 3, column = 0, sticky = singleLineLeftJustify)

            location = Label(__eventsList, text = "Location: ", background=secondWindowBackground, fg = secondWindowForeground)
            location.grid(row = ((rowsPerEvent*index) +4), column = 0, sticky = singleLineLeftJustify)

            description = Label(__eventsList, text = "Description: ", background=secondWindowBackground, fg = secondWindowForeground)
            description.grid(row = ((rowsPerEvent*index) +5), column = 0, sticky = singleLineLeftJustify)

            newName = Label(__eventsList, text = currentEvent.getName(), background=secondWindowBackground, fg = secondWindowForeground)
            newName.grid(row = ((rowsPerEvent*index) + 1), column = 1, sticky = singleLineLeftJustify)

            newClub = Label(__eventsList, text = currentEvent.getClubHost().getClubName(), background=secondWindowBackground, fg = secondWindowForeground)
            newClub.grid(row = ((rowsPerEvent*index)+2), column = 1, sticky = singleLineLeftJustify)

            newDate = Label(__eventsList, text = currentEvent.getDate().strftime(dateFormat), background=secondWindowBackground, fg = secondWindowForeground)
            newDate.grid(row = ((rowsPerEvent*index)+3), column = 1, sticky = singleLineLeftJustify)

            newLocation = Label(__eventsList, text = currentEvent.getLocation(), background=secondWindowBackground, fg = secondWindowForeground)
            newLocation.grid(row = ((rowsPerEvent*index)+4), column = 1, sticky = singleLineLeftJustify)

            newDescription = Label(__eventsList, text = currentEvent.getDescription(), background=secondWindowBackground, fg = secondWindowForeground, wraplength = secondWindowWrap, justify = LEFT)
            newDescription.grid(row = ((rowsPerEvent*index)+5), column = 1, sticky = singleLineLeftJustify)

            filler = Label(__eventsList, background=secondWindowBackground, fg = secondWindowForeground)
            filler.grid(row=((rowsPerEvent*index)+rowsPerEvent), column = 1, sticky = singleLineLeftJustify)

            index = index + 1

        __eventsList.mainloop()
