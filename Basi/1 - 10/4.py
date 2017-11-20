def which_prize(points):
    """
    Ritorna il premio vinto in base ai punti.
    """
    prize = ""
    if points>=0 and points<=50:
        prize = "wooden rabbit"
    elif points>=51 and points<=150:
        prize = False
    elif points>=151 and points<=180:
        prize = "wafer-thin mint"
    elif 181 <= points <= 200:
        prize = "penguin"
    else:
        prize = "EVERYTHING"
        
    if prize:
        return "Congratulations! You have won a {}!".format(prize)
    else:
        return "Oh dear, no prize this time."

print(which_prize(182))
