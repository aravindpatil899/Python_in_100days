import random
cards =['1','2','3','4','5','6','7','8','9','10']

contine_gaming ='y'
while contine_gaming=='y':
    your_cards =[]
    computers_cards = []
    for i in range(2):
        num =(random.choice(cards))
        your_cards.append(num)
        your_total= sum([ eval(i) for i in your_cards])
    print(f'your_cards : {your_cards} and the sum is {your_total}')
    for i in range(2):
        num =(random.choice(cards))
        computers_cards.append(num)
    print(f'computers first_card : {computers_cards[1]}')
    another_card = input("type 'y' to get another card , type 'n' to pass : ").lower()
    while another_card=='y':    
        num =(random.choice(cards))
        your_cards.append(num)
        your_total= sum([ eval(i) for i in your_cards])
        print(f'your_cards are : {your_cards} and the sum is {your_total}')
        another_card = input("type 'y' to get another card , type 'n' to pass : ").lower()
    computers_total=sum([eval(i) for i in computers_cards])
    while computers_total<17:
        computers_total=sum([eval(i) for i in computers_cards])
        num =(random.choice(cards))
        computers_cards.append(num)
        
    print(f'computer_cards are : {computers_cards} and the sum is { sum([ eval(i) for i in computers_cards])}')
    if your_total<=21 and your_total>computers_total and (computers_total<=21 or  computers_total>21) :
        print('You win')
    elif your_total>21 and computers_total<=21 :
        print('you loose')
    elif your_total>21 and computers_total>21:
        print('both loose')
    else :
        print('computer wins')
    contine_gaming=input("do you want to continue to play 'y' or 'n' : ")




