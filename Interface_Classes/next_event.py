from constants import topRightCorner, secondWindowBackground, secondWindowForeground, singleLineLeftJustify, secondWindowWrap
from tkinter import *

class NextEvent():
    """The GUI Class for a Club's Upcoming Event"""

    # the constructor for the NextEvent window
    # THIS WILL START THE NEXT EVENT WINODW
    # param: the event's: title (string), date (datetime), location (string), description (string)
    # returns: nothing 
    def __init__(self, nextEventTitle, nextEventDate, nextEventLocation, nextEventDescription):
        __eventPopUp = Tk()

        # set up the pop up window
        __eventPopUp.wm_title("Next Event")
        __eventPopUp.configure(background = secondWindowBackground)                                                  # sets background color to midnight blue

        __title = Label(__eventPopUp, text = "Event Title: ", background = secondWindowBackground, fg = secondWindowForeground)
        __title.grid(row = 0, column = 0, sticky= singleLineLeftJustify)

        __date = Label(__eventPopUp, text = "Event Date", background = secondWindowBackground, fg = secondWindowForeground)
        __date.grid(row = 1, column = 0, sticky= singleLineLeftJustify)

        __location = Label(__eventPopUp, text = "Event Location: ", background = secondWindowBackground, fg = secondWindowForeground)
        __location.grid(row = 2, column = 0, sticky= singleLineLeftJustify)

        __description = Label(__eventPopUp, text = "Event Description", background = secondWindowBackground, fg = secondWindowForeground)
        __description.grid(row = 3, column = 0, sticky= topRightCorner)

        __eventTitle = Label(__eventPopUp, text = nextEventTitle, background = secondWindowBackground, fg = secondWindowForeground)
        __eventTitle.grid(row = 0, column = 1, sticky= singleLineLeftJustify)

        __eventDate = Label(__eventPopUp, text = nextEventDate, background = secondWindowBackground, fg = secondWindowForeground)
        __eventDate.grid(row = 1, column = 1, sticky= singleLineLeftJustify)

        __eventLocation = Label(__eventPopUp, text = nextEventLocation, background = secondWindowBackground, fg = secondWindowForeground)
        __eventLocation.grid(row = 2, column = 1, sticky= singleLineLeftJustify)

        __eventDescription = Label(__eventPopUp, text = nextEventDescription, background = secondWindowBackground, fg = secondWindowForeground, wraplength = secondWindowWrap, justify = LEFT)
        __eventDescription.grid(row = 3, column = 1, sticky= singleLineLeftJustify)

        __filler = Label(__eventPopUp, background = secondWindowBackground, text = "")
        __filler.grid(row = 4, sticky = singleLineLeftJustify)
