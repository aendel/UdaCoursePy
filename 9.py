card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    print(hand)
    hand.append(card_deck.pop())

print("Stampa hand finale")
print(hand)

def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

