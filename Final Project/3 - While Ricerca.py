# TODO: Implement the continue_crawl function described above
def continue_crawl(history,target,maxstep=25):
    if history[-1] == target:
        print("Obiettivo trovato! Concludere.")
        return False
    elif len(history) > maxstep:
        print("Ricerca troppo lunga. Concludere.")
        return False
        
        #history[-1] -> intendiamo l'ultimo articolo.
        #in -> intendiamo la presenza all'interno della lista.
        #history[:-1] -> intendiamo la lista escluso l'ultimo elemento.
        
    elif history[-1] in history[:-1]:
        print("Ultimo articolo presente nella lista degli articoli gia visionati. Ciclo. Concludere.")
        return False
    else:
        print("Continua...")
        return True

print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'))
