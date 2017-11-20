#modules
#math contiene ad esempio il factorial
import math
print(math.factorial(3))
print(math.exp(3)) #esponenziale di e^3

import datetime #module for dates
print(datetime.time())
print(datetime.date.today())

import os #methods for changing the current working directory
import csv #methods for handle with .csv (comma separeted values) file ( useful for data mining)

import zipfile #methods for extract all of the files from a file zip ect...

import time#gestire timer, durate di esecuzioni ect...

#Possiamo importare singole classi o funzioni da un modulo.
#from module_name import object_name
#Es.
from collections import defaultdict
#se chiamiamo le componenti più generali darà errore

#collections #Errore
#collections.defaultdict() #Errore

defaultdict() #FUNZIONAAA

#possiamo fare anche importazioni multiple
from collections import defaultdict, namedtuple

#possiamo importare e usare nel nostro programma con un nome differente
#import module_name as different_name
#Es.
import multiprocessing as mp #modulo per processori

print(mp.cpu_count())

#Questo discorso vale anche per l'importazione della singola componente.
#Es.
#from module_name import object_name as different_name
from csv import reader as csvreader

#PUOI FARE UNA MINCHIATA E IMPORTARE TUTTOOOO
#NON LO FAREEE
#from module_name import *

import os.path
print(os.path.isdir('my_path')) #Return false in questo caso

