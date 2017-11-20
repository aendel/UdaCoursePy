python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]

print(python_versions[0]) #first element

print(python_versions[-1]) #last element

print(python_versions[-2]) #second to last

my_list = ['a','b','c','d','e']

print(my_list[4]) #e

#print(my_list[5]) #errore out of range

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number-1]
# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))
"""
"""
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
q3 = months[6:9]
print(q3)
"""
"""
print(months)
"""
"""
first_half = months[:6]
print (first_half)
second_half = months[6:]
print(second_half)
"""
"""
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

