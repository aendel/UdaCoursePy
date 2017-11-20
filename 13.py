AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat)) #<class 'tuple'>
print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

dimensions = 52 , 40 , 100
length , width , height = dimensions

print("The dimension are {} x {} x {}".format(length,width,height))

longitudine , latitudine = 10,10

world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}

def first_and_last(sequence):
    """Ritorna primo e ultimo"""
    return sequence[0], sequence[-1]

first_and_last(["Spam", "egg", "sausage", "Spam"])

start, end = first_and_last(["Spam", "egg", "sausage", "Spam"])

print(start)
print(end)

def hours2days(input_hours):
    days = input_hours // 24
    hours = input_hours % 24
    return days, hours

print(hours2days(25))
print(hours2days(24))


def box(width, height, symbol='*'):
    """print a box made up of asterisks, or some other character.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    symbol: a single character string used to draw the box edges
    """
    print(symbol * width) # print top edge of box

    # print sides of box
    for _ in range(height-2):
        print(symbol + " " * (width-2) + symbol) 

    print(symbol * width) # print bottom edge of box

box(10,10)
box(4,6,'#')

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
