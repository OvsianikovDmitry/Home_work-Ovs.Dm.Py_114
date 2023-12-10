suit = ['Пик','Червей','Треф','Бубей']
meaning = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

card_deck = [m +' '+ s for s in suit for m in meaning]

card_iter = (i for i in card_deck)

while True:
    try:
        print(card_iter.__next__())
    except StopIteration:
        print(StopIteration)
        break
