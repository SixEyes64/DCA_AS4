from tkinter import *
from backend import backend as bk

'''
Author: Hunter, 2022001566
Pledge of Honour: I pledge by honour that this program is solely my work
Purpose: Program that reads MS Access content and queries data for statistics
'''

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Company Data")
        self.geometry("720x580")

        appFrame = AppFrame(self)
        appFrame.show_frame()

class AppFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def show_frame(self):   
        self.pack(pady=20)

        # Button Widgets
        self.print_all = Button(self, text="Print all", command=bk().print_all_records)
        self.pos_growth = Button(self, text="Positive Growth", command=bk().print_positive_growth)
        self.query_date = Button(self, text="Filter by date", command=self.QueryWindow)
        self.date_range = Button(self, text="Filter by range")

        # Place buttons
        self.print_all.grid(row=0,column=0, padx=10, pady=10)
        self.pos_growth.grid(row=0,column=1, padx=10, pady=10)
        self.query_date.grid(row=1,column=0, padx=10, pady=10)
        self.date_range.grid(row=1,column=1, padx=10, pady=10)

    def QueryWindow(self):
        # Setup
        query_win = Toplevel(self)
        query_win.title("Enter Date")
        query_win.geometry("300x150")
        
        # Labels
        self.dLabel = Label(query_win, text="Date").grid(row=0,column=0,padx=30,pady=15)
        self.mLabel = Label(query_win, text="Month").grid(row=0,column=1,padx=30,pady=15)
        self.yLabel = Label(query_win, text="Year").grid(row=0,column=2,padx=30,pady=15)

        # Entry Boxes
        self.d = Entry(query_win, width=9).grid(row=1,column=0)
        self.m = Entry(query_win, width=9).grid(row=1,column=1)
        self.y = Entry(query_win, width=9).grid(row=1,column=2)

        # Buttons
        self.confirm = Button(query_win, text="Enter").grid(row=2,column=1,padx=30,pady=15)



def main():
    '''Runs all the main functions for the program to function'''
    app = App()
    app.mainloop()
    # b.query_record_by_date()
    # b.count_companies_between_dates()

main()


