sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']

sample_string[4] # N
sample_list[4] #Terry

sample_string[12:21] #Something
sample_list[2:4] #Terry,Eric

len(sample_string) #42
len(sample_list) #6

'thing' in sample_string #True
'Rowan' in sample_list #False

sample_list[3] = 'Eric'
print(sample_list)

#sample_string[8] = 'f' #TypeError

piatto = ["Ciao","ciao","ciaooo","no"]

nonpiatto = piatto
print("Print piatto" )
print(piatto)
print("Print non piatto")
print(nonpiatto)

print("Assegno a piatto[0] \"Hello\"")
piatto[0] = "Hello" #QUESTA MODIFICA AFFLIGGERA' ANCHE NONPIATTO

print("Print piatto" )
print(piatto)
print("Print non piatto")
print(nonpiatto)

vett = [320,15,2,10,12,1235]
print(max(vett)) #1235

vettParole = ["Come","Zacinto","Davvero","Eppure","Zeno"]
print(max(vettParole)) #Zeno

#print(max([vett,vettParole])) #Errore confronto int/str
#min speculare a max
print(sorted(vett))
print(sorted(vettParole))

nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)

names = ["García", "O'Kelly", "Davis"]
"-".join(names)
print(names)

arraymisto = ["parola",12]
#"and".join(arraymisto)#Errore TypeError, non puoi joinare una stringa ad un insieme misto

names.append("Francesco")
print(names)

def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
  
    return sorted(input_list,reverse=True)[:3]
    
print(top_three([2,3,5,6,8,4,2,1]))

def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    middle_index = int(len(numbers)/2)
    if len(numbers) %2 == 1 :
        return numbers[middle_index]
    else :
        return (numbers[middle_index-1]+numbers[middle_index])/2
        
test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))




