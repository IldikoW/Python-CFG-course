
import csv


def read_data():

    """
    This function  reads the data from the csv file
    :param: nothing
    :return: nothing
    """
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def total_sales():
    """
    This function collects all of the sales from each month into a single list and outputs the total sales across all months
    :param: nothing
    :return: total sales
    """


    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total_sales = sum(sales)
    return total_sales

total_sales()

def average_sales() :
    """
    This function outputs a summary of the results to a spreadsheet
    :param: nothing
    :return: average sales
    """
    average_sales = total_sales()/12
    print(average_sales)
    return average_sales


def summary_file ():
    """
    This function outputs a summary of the results to a spreadsheet
    :param: nothing
    :return: nothing
    """


    field_names = ['Total Sales', 'The average', 'Month with the highest sales']
    data = [{'Total Sales': total_sales(),'The average' : average_sales() ,'Month with the highest sales' : 'Jan'}]
    with open('Summary3.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)
    print( 'See Summary3 for results.')
    
summary_file()