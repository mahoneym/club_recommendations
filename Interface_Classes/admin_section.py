from tkinter import *
import tkinter.messagebox
from datetime import datetime, time
from tkinter import ttk
from tkcalendar import DateEntry
from constants import SINGLE_LINE_LEFT_JUSTIFY, WHOLE_ROW, SECOND_WINDOW_BACKGROUND, SECOND_WINDOW_FOREGROUND, ERROR_BOX_TOP

class AdminSection:
    """The Admin Section of the GUI"""

    # the constructor for the AdminSection
    # CREATES AND STARTS THE ADMIN SECTION
    # param: the recommender object
    # returns: nothing
    def __init__(self, recommendObject):
        global eventName, descriptionEntry, dateInput, minuteEntry, locationEntry, hourEntry, clubEntry, recommend, monthEntry, dayEntry, yearEntry, amOrPm

        recommend = recommendObject

        __clubNames = recommend.getClubNames()

        __admin = Tk()
        __admin.configure(background=SECOND_WINDOW_BACKGROUND)
        __admin.wm_title("Admin Section")

        __directions = Label(__admin, text = "Welcome, Admin! Below you can add an event for any of the clubs.", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __directions.grid(row = 0, columnspan = 6, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __admin_space_1 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_1.grid(row = 1, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __clubDescriptionLabel = Label(__admin, text = "Club: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __clubDescriptionLabel.grid(row = 2, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        clubEntry = ttk.Combobox(__admin, values = __clubNames)
        clubEntry.grid(row = 2, column = 1, sticky = WHOLE_ROW)

        __eventNameLabel = Label(__admin, text = "Name: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __eventNameLabel.grid(row = 2, column = 2, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        eventName = Entry(__admin)
        eventName.grid(row = 2, column = 3, sticky= WHOLE_ROW)

        __locationLabel = Label(__admin, text = "Location: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __locationLabel.grid(row = 2, column = 4, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        locationEntry = Entry(__admin)
        locationEntry.grid(row = 2, column = 5, sticky= WHOLE_ROW)

        __admin_space_2 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_2.grid(row = 3, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        # place to enter the date
        __monthLabel = Label(__admin, text = "Month:", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __monthLabel.grid(row=6, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        monthEntry = Entry(__admin)
        monthEntry.grid(row=6, column =1, sticky = WHOLE_ROW)

        __dayLabel = Label(__admin, text = "Day:", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __dayLabel.grid(row=6, column = 2, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        dayEntry = Entry(__admin)
        dayEntry.grid(row=6, column =3, sticky = WHOLE_ROW)

        __yearLabel = Label(__admin, text = "Year: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __yearLabel.grid(row=6, column =4, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        yearEntry = Entry(__admin)
        yearEntry.grid(row=6, column =5, sticky = WHOLE_ROW)

        __admin_space_3 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_3.grid(row = 7, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __hourLabel = Label(__admin, text = "Hour: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __hourLabel.grid(row = 8, column = 0, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        hourEntry = Entry(__admin)
        hourEntry.grid(row = 8, column = 1, sticky = WHOLE_ROW)

        __minuteLabel = Label(__admin, text = "Minute: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __minuteLabel.grid(row = 8, column = 2, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        minuteEntry = Entry(__admin)
        minuteEntry.grid(row = 8, column = 3, sticky = WHOLE_ROW)

        amOrPm = 1

        __morning = Radiobutton(__admin, text= "AM", variable = amOrPm, value = 0, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __morning.grid(row = 8, column = 4, padx = 10)

        __afternoon = Radiobutton(__admin, text = "PM", variable = amOrPm, value = 1, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __afternoon.grid(row = 8, column = 5, sticky = SINGLE_LINE_LEFT_JUSTIFY)

        __admin_space_4 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_4.grid(row = 9, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __descriptionLabel = Label(__admin, text = "Description: ", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __descriptionLabel.grid(row = 10, column = 0, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        descriptionEntry = Entry(__admin)
        descriptionEntry.grid(row = 10, column = 1, columnspan = 5, sticky= WHOLE_ROW)

        __admin_space_6 = Label(__admin, background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND)
        __admin_space_6.grid(row = 11, sticky= SINGLE_LINE_LEFT_JUSTIFY)

        __submitButton = Button(__admin, text = "Submit", background = SECOND_WINDOW_BACKGROUND, fg = SECOND_WINDOW_FOREGROUND, command = self.creatingAnEvent)
        __submitButton.grid(row = 12, columnspan = 6, sticky = WHOLE_ROW)

        __admin.mainloop()

    # creates an event based on user input
    # gets called when the user hits submit
    # param: none
    # returns: nothings
    def creatingAnEvent(self):
            name = eventName.get()
            club = clubEntry.get()
            eventDateTime = self.createDateTime()

            location = locationEntry.get()
            description = descriptionEntry.get()

            if(name == "" or club == "" or eventDateTime == None or location == "" or description == ""):
                tkinter.messagebox.showerror(ERROR_BOX_TOP, "You left one or more fields blank. Fill them all in then try again.")
            else:
                recommend.addEventToClub(club, name, eventDateTime, location, description)
                tkinter.messagebox.showinfo("Event Added", "Your event has been added")
                self.__clearTheScreen()

    def createDateTime(self):
        hour = hourEntry.get()
        minute = minuteEntry.get()

        month = monthEntry.get()
        day = dayEntry.get()
        year = yearEntry.get()

        filledIn = not (year == "" or day == "" or month == "" or minute == "" or hour == "")
        areDigits = (year.isdigit() and day.isdigit() and month.isdigit() and minute.isdigit() and hour.isdigit())

        if(filledIn == False and areDigits == False):
            return None

        if(amOrPm == 1):
            hour = int(hour) + 12
        else:
            hour = int(hour)

        eventDate = datetime(year = int(year), month= int(month), day = int(day), hour = hour, minute = int(minute))
        return eventDate


    # clears the Admin screen
    # param: none
    # returns: none
    def __clearTheScreen(self):
        eventName.delete(0,'end')     # clears the user's input in the entry box
        clubEntry.delete(0, 'end')
        monthEntry.delete(0, 'end')
        dayEntry.delete(0, 'end')
        yearEntry.delete(0, 'end')
        hourEntry.delete(0, 'end')
        minuteEntry.delete(0, 'end')
        locationEntry.delete(0, 'end')
        descriptionEntry.delete(0, 'end')
