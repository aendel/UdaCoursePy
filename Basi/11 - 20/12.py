
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

print(elements['helium'])
{'number': 2, 'symbol': 'He', 'weight': 4.002602}
print(elements.get('unobtainium', 'There\'s no such element!'))
There's no such element!

print(elements['helium']['weight'])
4.002602

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(yearly_record):
    sum = 0 
    for month in yearly_record:
        for date in range(len(yearly_record[month])):
            sum += yearly_record[month][date]
    return sum

print(total_takings(monthly_takings))

#FATTO MEGLIO
def total_takingsPy(yearly_record):
    #total is used to sum up the monthly takings
    total = 0
    for month in yearly_record.keys():
        #I use the Python function sum to sum up over 
        #all the elements in a list
        total = total + sum(yearly_record[month])
    return total

