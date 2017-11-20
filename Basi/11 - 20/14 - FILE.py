#FILE
#1 Apertura
f = open('/Users/Francesco/Desktop/ProvaPy/File/1.txt','r') #'r' in lettura
#2 Lettura
file_data = f.read()
#3 Scrittura
"""
"""
#4 Chisura
f.close()

#Se il file non esiste con la w, verrà creato.
f = open('/Users/Francesco/Desktop/ProvaPy/File/2.txt','w') #'w' in scrittura
f.write("Hello World!")
f.close()

#'a' in aggiunta a contenuto esistente
f = open('/Users/Francesco/Desktop/ProvaPy/File/2.txt','a') 
f.write("\n Pt.2")
f.close

with open('./File/2.txt','r') as f:
    print(f.read(4))
    print(f.read(5))
    print(f.read())

with open('./File/3.txt','w') as f:
    f.write("Buongiorno all'alba ed al caffè \n")
    f.write("Buongiorno a chi non c'èèè")

with open('./File/3.txt','r') as f:
    print(f.read())

my_lines = []
with open('./File/3.txt','r') as f:
    for line in f:
        my_lines.append(line.strip())

print(my_lines)

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename,'r') as file:
        for line in file:
            temp = line.split(',')
            cast_list.append(temp[0])
    return cast_list
    
print(create_cast_list('./File/flying_circus_cast.txt'))
