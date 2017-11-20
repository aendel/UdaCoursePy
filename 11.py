def remove_duplicates(lista):
    nuova = [] 
    for item in lista:
        if item not in nuova:
            nuova.append(item)
    return nuova

#Per conservare collezioni di dati unici usiamo i SETS.

squares = set()

n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1

print(squares) #tutti i numeri quadrati da 0 a 2000

#Dictionaries per coppie di elementi (keys - values) chiavi - valori

elements = {'hydrogen': 1 ,'helium': 2 ,'carbon' : 6}
print(elements['carbon']) #ritorna 6

#Aggiungiamo elementi anche singolarmente così -->
elements['lithium'] = 3
print(elements['lithium']) #stampa 3

if 'mithril' in elements:
    print("That's a real element!")
else:
    print("There's no such element!")

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

def most_prolific(dictis):
    """
    """
    count={}
    max = 0
    myear = 0
    for item in dictis:
        if dictis[item] in count:
            count[dictis[item]] +=1
        else:
            count[dictis[item]] = 1
    print(count)
    for year in count:
        if count[year] > max:
            max = count[year]
            myear = year
    return myear

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
    
print(most_prolific(Beatles_Discography))
