import pyodbc
from datetime import datetime
from backend import backend as bk

'''
Author: Hunter, 2022001566
Pledge of Honour: I pledge by honour that this program is solely my work
Purpose: Program that reads MS Access content and queries data for statistics
'''

# Path 1: C:\Users\ender\OneDrive\Documents\WITT\4DCA\Assignments\Assessment_4\DCA_AS4\DCA_AS4\company.accdb
# Path 2: C:\Users\2022001566\source\repos\DCA_AS4\DCA_AS4\company.accdb

# All functions except main moved to backend


def main():
    '''Runs all the main functions for the program to function'''
    b = bk()
    b.print_all_records()
    # b.print_positive_growth()
    # b.query_record_by_date()
    # b.count_companies_between_dates()

main()
# print_all_records()
# print_positive_growth()
# query_record_by_date()
# count_companies_between_dates()
