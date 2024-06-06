import pyodbc
from datetime import datetime

'''
Author: Hunter, 2022001566
Pledge of Honour: I pledge by honour that this program is solely my work
Purpose: Program that reads MS Access content and queries data for statistics
'''

HeaderFormat = '{0:<8}{1:<25}{2:<20}{3:<18}{4:<18}{5:20}{6:<20}{7:10}'
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022001566\source\repos\DCA_AS4\DCA_AS4\company.accdb')
cursor = conn.cursor()

def print_all_records():
    '''Prints all records'''
    cursor.execute('SELECT * FROM Company_Data')

    print(HeaderFormat.format('ID','Company Name','Industry','Year Revenue','Revenue Growth','# of Employees','Headquarters','Company Found Date'))
    print(f'{"_":_<150}')

    for row in cursor.fetchall():
        date = datetime.strftime(row.company_found_date, '%d/%m/%Y')

        record = f'{row.ID:<8}{row.company_name:<25}{row.industry:<25}{row.year_revenue:<15}{row.revenue_growth:<16}{row.number_of_employees:<20}{row.headquarter:<20}{date:<10}'
        print(record)


def print_positive_growth():
    '''Only prints data with positive growth'''
    cursor.execute('SELECT * FROM Company_Data WHERE revenue_growth > 0')
    
    print(HeaderFormat.format('ID','Company Name','Industry','Year Revenue','Revenue Growth','# of Employees','Headquarters','Company Found Date'))
    print(f'{"_":_<150}')
    
    for row in cursor.fetchall():
        date = datetime.strftime(row.company_found_date, '%d/%m/%Y')

        record = f'{row.ID:<8}{row.company_name:<25}{row.industry:<25}{row.year_revenue:<15}{row.revenue_growth:<16}{row.number_of_employees:<20}{row.headquarter:<20}{date:<10}'
        print(record)



def query_record_by_date():
    '''Displays a query sorting records by date'''
    d = int(input("Enter day"))
    m = int(input("Enter month"))
    y = int(input("Enter year"))
    
    # date = 
    
    cursor.execute('SELECT * FROM Company_Data')



def count_companies_between_dates():
    '''Asks user for start and end date, and then lists companies 
       between those two dates'''
    pass



def main():
    '''Runs all the main functions for the program to function'''
    pass


print_all_records()
print_positive_growth()

