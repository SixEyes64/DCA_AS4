import pyodbc
from datetime import datetime

'''
Author: Hunter, 2022001566
Pledge of Honour: I pledge by honour that this program is solely my work
Purpose: Program that reads MS Access content and queries data for statistics
'''

# Path 1: C:\Users\ender\OneDrive\Documents\WITT\4DCA\Assignments\Assessment_4\DCA_AS4\DCA_AS4\company.accdb
# Path 2: C:\Users\2022001566\source\repos\DCA_AS4\DCA_AS4\company.accdb

HeaderFormat = '{0:<8}{1:<25}{2:<20}{3:<18}{4:<18}{5:20}{6:<20}{7:10}'

# Connect py file to Access using pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ender\OneDrive\Documents\WITT\4DCA\Assignments\Assessment_4\DCA_AS4\DCA_AS4\company.accdb')
cursor = conn.cursor()

def print_all_records():
    '''Prints all records'''
    # Select ALL records
    cursor.execute('SELECT * FROM Company_Data')

    # Format the header with HeaderFormat
    # and print the underscores to separate heading from data
    print(HeaderFormat.format('ID','Company Name','Industry','Year Revenue','Revenue Growth','# of Employees','Headquarters','Company Found Date'))
    print(f'{"_":_<150}')

    for row in cursor.fetchall():
        date = datetime.strftime(row.company_found_date, '%d/%m/%Y')

        record = f'{row.ID:<8}{row.company_name:<25}{row.industry:<25}{row.year_revenue:<15}{row.revenue_growth:<16}{row.number_of_employees:<20}{row.headquarter:<20}{date:<10}'
        print(record)


def print_positive_growth():
    '''Only prints data with positive growth'''
    # Only selects records with positive growth
    cursor.execute('SELECT * FROM Company_Data WHERE revenue_growth > 0')
    
    # Format the header with HeaderFormat
    # and print the underscores to separate heading from data
    print(HeaderFormat.format('ID','Company Name','Industry','Year Revenue','Revenue Growth','# of Employees','Headquarters','Company Found Date'))
    print(f'{"_":_<150}')
    
    # Print all positive growth records
    for row in cursor.fetchall():
        date = datetime.strftime(row.company_found_date, '%d/%m/%Y')

        record = f'{row.ID:<8}{row.company_name:<25}{row.industry:<25}{row.year_revenue:<15}{row.revenue_growth:<16}{row.number_of_employees:<20}{row.headquarter:<20}{date:<10}'
        print(record)



def query_record_by_date():
    '''Displays a query sorting records by date'''
    # Enter the day, month and year
    d = int(input("Enter day: "))
    m = int(input("Enter month: "))
    y = int(input("Enter year: "))

    # Get date data and format it
    date = datetime(y, m, d)
    queryDate = date.strftime('%d/%m/%Y')

    # Use cursor to select from table   
    cursor.execute('SELECT * FROM Company_Data')

    # Look through DB
    for row in cursor.fetchall():

        rowDate = datetime.strftime(row.company_found_date, '%d/%m/%Y')

        if queryDate in rowDate:
            date_str = 'Company Name: {name}\nRevenue: {revenue}'.format(name=row.company_name,revenue=row.year_revenue)
            break
        else:
            date_str = "No date found"

    # Print result
    print(date_str)




def count_companies_between_dates():
    '''Asks user for start and end date, and then lists companies 
       between those two dates'''
    date_list = []
    while len(date_list) <= 1:
        d = int(input("Enter day: "))
        m = int(input("Enter month: "))
        y = int(input("Enter year: "))

        # Get date data and format it
        date = datetime(y, m, d)
        queryDate = date.strftime('%d/%m/%Y')
        date_list.append(queryDate)
        print('\n',date_list)



def main():
    '''Runs all the main functions for the program to function'''
    pass


print_all_records()
# print_positive_growth()
# query_record_by_date()
count_companies_between_dates()
