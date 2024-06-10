from tkinter import *
from tkinter import messagebox
from backend import backend as bk

'''
Author: Hunter, 2022001566
Pledge of Honour: I pledge by honour that this program is solely my work
Purpose: Program that reads MS Access content and queries data for statistics
'''

class App(Tk):
    def __init__(self):
        super().__init__()

        # Window details
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
        self.date_range = Button(self, text="Filter by range", command=self.ByRangeWindow)

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
        self.mLabel = Label(query_win, text="Month").grid(row=0,column=1,padx=40,pady=15)
        self.yLabel = Label(query_win, text="Year").grid(row=0,column=2,padx=30,pady=15)

        # Get values
        self.q1 = IntVar(query_win)
        self.q2 = IntVar(query_win)
        self.q3 = IntVar(query_win)

        # Entry Boxes
        self.d = Entry(query_win, width=9, textvariable=self.q1).grid(row=1,column=0)
        self.m = Entry(query_win, width=9, textvariable=self.q2).grid(row=1,column=1)
        self.y = Entry(query_win, width=9, textvariable=self.q3).grid(row=1,column=2)

        # Buttons
        self.confirm = Button(query_win, text="Enter", command=self.get1).grid(row=2,column=1,padx=30,pady=15)

    def get1(self):
        '''Gets values for query_record_by_date'''
        try:
            # Get values
            bk().query_record_by_date(self.q1.get(),self.q2.get(),self.q3.get())
        except Exception as QueryError:
            messagebox.showerror("Error","Invalid date")


    def ByRangeWindow(self):
        byrange_win = Toplevel(self)
        byrange_win.title("Enter date by range")
        byrange_win.geometry("400x200")

        # Labels
        self.field1 = Label(byrange_win, text="1").grid(row=1,column=0,padx=30,pady=15)
        self.field2 = Label(byrange_win, text="2").grid(row=2,column=0,padx=30,pady=15)

        self.dLabel = Label(byrange_win, text="Date").grid(row=0,column=1,padx=30,pady=15)
        self.mLabel = Label(byrange_win, text="Month").grid(row=0,column=2,padx=40,pady=15)
        self.yLabel = Label(byrange_win, text="Year").grid(row=0,column=3,padx=30,pady=15)
        
        # Get Values
        self.d1q1 = IntVar(byrange_win)
        self.d1q2 = IntVar(byrange_win)
        self.d1q3 = IntVar(byrange_win)
        
        self.d2q1 = IntVar(byrange_win)
        self.d2q2 = IntVar(byrange_win)
        self.d2q3 = IntVar(byrange_win)
        

        # Entry Boxes
        self.d1 = Entry(byrange_win, width=9, textvariable=self.d1q1).grid(row=1,column=1,pady=15)
        self.m1 = Entry(byrange_win, width=9, textvariable=self.d1q2).grid(row=1,column=2,pady=15)
        self.y1 = Entry(byrange_win, width=9, textvariable=self.d1q3).grid(row=1,column=3,pady=15)

        self.d2 = Entry(byrange_win, width=9, textvariable=self.d2q1).grid(row=2,column=1)
        self.m2 = Entry(byrange_win, width=9, textvariable=self.d2q2).grid(row=2,column=2)
        self.y2 = Entry(byrange_win, width=9, textvariable=self.d2q3).grid(row=2,column=3) 
        

        # Buttons
        self.confirm = Button(byrange_win, text="Enter", command=self.get2).grid(row=3,column=2,padx=30,pady=15)

    def get2(self):
        '''Gets two dates and searches for companies in between those dates'''
        bk().count_companies_between_dates(self.d1q1.get(),self.d1q2.get(),self.d1q3.get(),self.d2q1.get(),self.d2q2.get(),self.d2q3.get())


def main():
    '''Runs all the main functions for the program to function'''
    app = App()
    app.mainloop()
    # b.count_companies_between_dates()

main()


