names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']

for name in names:
    print(name.title())

def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for item in input_list:
        sum+=item
    return sum

#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count

for number in range(4):
    print(number)

names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
# create a new list of capitalized names without modifying the original list
capitalized_names = [] #create a new, empty list
for name in names:
    capitalized_names.append(name.title()) #add elements to the new list

# modify the names list in place
for index in range(len(names)): # iterate over the index numbers of the names list
    names[index] = names[index].title() # modify each element of names


#NON HA EFFETTO
"""
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']

for name in names:
    name = name.title()

print(names)
"""

#define the  html_list function
def html_list(lista):
    li = ""
    li+="<ul>\n"
    for item in lista:
        li+="<li>{}</li>\n".format(item)
    li+="</ul>\n"
    return li
    
print(html_list(['first string', 'second string']))
