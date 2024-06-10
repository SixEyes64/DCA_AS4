import pyodbc
from datetime import datetime

# Path 1: C:\Users\ender\OneDrive\Documents\WITT\4DCA\Assignments\Assessment_4\DCA_AS4\DCA_AS4\company.accdb
# Path 2: C:\Users\2022001566\source\repos\DCA_AS4\DCA_AS4\company.accdb

class backend():
    def __init__(self):
        self.HeaderFormat = '{0:<8}{1:<25}{2:<20}{3:<18}{4:<18}{5:20}{6:<20}{7:10}'

        # Connect py file to Access using pyodbc
        self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022001566\source\repos\DCA_AS4\DCA_AS4\company.accdb')
        self.cursor = self.conn.cursor()

    def print_all_records(self):
        '''Prints all records'''
        # Select ALL records
        self.cursor.execute('SELECT * FROM Company_Data')

        # Format the header with HeaderFormat
        # and print the underscores to separate heading from data
        print(self.HeaderFormat.format('ID','Company Name','Industry','Year Revenue','Revenue Growth','# of Employees','Headquarters','Company Found Date'))
        print(f'{"_":_<150}')

        for row in self.cursor.fetchall():
            date = datetime.strftime(row.company_found_date, '%d/%m/%Y')

            record = f'{row.ID:<8}{row.company_name:<25}{row.industry:<25}{row.year_revenue:<15}{row.revenue_growth:<16}{row.number_of_employees:<20}{row.headquarter:<20}{date:<10}'
            print(record)


    def print_positive_growth(self):
        '''Only prints data with positive growth'''
        # Only selects records with positive growth
        self.cursor.execute('SELECT * FROM Company_Data WHERE revenue_growth > 0')
        
        # Format the header with HeaderFormat
        # and print the underscores to separate heading from data
        print(self.HeaderFormat.format('ID','Company Name','Industry','Year Revenue','Revenue Growth','# of Employees','Headquarters','Company Found Date'))
        print(f'{"_":_<150}')
        
        # Print all positive growth records
        for row in self.cursor.fetchall():
            date = datetime.strftime(row.company_found_date, '%d/%m/%Y')

            record = f'{row.ID:<8}{row.company_name:<25}{row.industry:<25}{row.year_revenue:<15}{row.revenue_growth:<16}{row.number_of_employees:<20}{row.headquarter:<20}{date:<10}'
            print(record)



    def query_record_by_date(self, day, month, year):
        '''Displays a query sorting records by date'''
        # Enter the day, month and year
        self.day = day
        self.month = month
        self.year = year

        # Get date data and format it
        date = datetime(self.year, self.month, self.day)
        queryDate = date.strftime('%d/%m/%Y')

        # Use cursor to select from table   
        self.cursor.execute('SELECT * FROM Company_Data')

        # Look through DB
        for row in self.cursor.fetchall():

            rowDate = datetime.strftime(row.company_found_date, '%d/%m/%Y')

            if queryDate in rowDate:
                date_str = 'Company Name: {name}\nRevenue: {revenue}'.format(name=row.company_name,revenue=row.year_revenue)
                break
            else:
                date_str = "No date found"

        # Print result
        print(date_str)


    def count_companies_between_dates(self, day1, month1, year1, day2, month2, year2):
        '''Asks user for start and end date, and then lists companies 
        between those two dates'''
        date_list = [] # Date list gathers the two dates
        no_of_dates = []

        # Get date data and format it
        date1 = datetime(year1, month1, day1)
        queryDate1 = date1.strftime('%d/%m/%Y')
        
        date2 = datetime(year2, month2, day2)
        queryDate2 = date2.strftime('%d/%m/%Y')

        # Add to date_list
        date_list.append(queryDate1)
        date_list.append(queryDate2)

        # Select BETWEEN dates
        self.cursor.execute('SELECT * FROM Company_Data WHERE company_found_date BETWEEN ? AND ?',(date_list[0],date_list[1]))


        for row in self.cursor.fetchall():
            no_of_dates.append(row)

        # Print final amount of dates
        print("The number of companies between {y1} and {y2} found is {no}".format(y1=date1.year, y2=date2.year, no=len(no_of_dates)))