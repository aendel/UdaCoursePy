def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
    
def convert_to_numeric(score):
    """
    Converte da stringa a numero il punteggio
    """
    return int(score)
    
def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Somma i 3 valori medi.
    """
    sum = score1+score2+score3+score4+score5
    sum = sum - min(score1,score2,score3,score4,score5) - max(score1,score2,score3,score4,score5)
    return sum

def score_to_rating_string(score):
    """
    Converte un valore in una stringa.
    """
    if 0<=score<1 : return "Terrible"
    elif 1<=score<2 : return "Bad"
    elif 2<=score<3 : return "OK"
    elif 3<=score<4 : return "Good"
    else : return "Excellent"
    
