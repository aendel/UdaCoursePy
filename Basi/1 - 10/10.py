manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    if cargo_weight >= 100:
        break;
    else:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]

print(cargo_weight)
print(cargo_hold)


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = []
    for i in range(len(my_answers)):
        if my_answers[i] == answers[i] :
            results.append(True)
        else : 
            results.append(False)
    
    return count_correct(results)
    
def count_correct(results):
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result :
            count_correct += 1
        else :
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
        
check_answers([1,2,3,4,5],[1,2,3,4,5])
check_answers([1,2,3,4,5],["badger","badger","badger","badger","badger"])
