import random

suits = ('Червы','Бубны ','Пики','Трефы')
ranks = ('Два','Три','Торт','Пять','Шесть','Семь','Восемь','Девять','Десять','Валет','Дама','Король',' Туз')
values = {'Два':2,'Три':3,'Торт':4,'Пять':5,'Шесть':6,'Семь':7,'Восемь':8,'Девять':9,'Десять':10,' Валет':10,'Дама':10,'Король':10,'Туз':11}
playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank =  rank

    def __str__(self):
        return self.rank + ' ' + self.suit

class Desk:
    def __init__(self):
        self.desk = []
        for suit in suits:
            for rank in ranks:
                self.desk.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.desk:
            deck_comp += '\n' + card.__str__()
        return 'There are cards in the deck' + deck_comp

    def shuffle(self):
        random.shuffle(self.desk)

    def deal(self):
        single_card = self.desk.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Tuz':
            self.aces += 1


    def adjust_for_ace(self):
        while self.value > 21 and self.aces >0:
            self.value -= 10
            self.aces -= 1

num_zero = 0
num_one = 1

"""if 0:
    print('True')

test_deck = Desk()
test_deck.shuffle()

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)

test_player.add_card(pulled_card)
print(test_player.value)


test_player.add_card(test_deck.deal())
test_player.value"""

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.beat = 0

    def win_bet(self):
        self.total += self.beat

    def lose_bet(self):
        self.total -= self.beat
        

"""def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips do you want bet? : '))

        except:
            print("Sorry, please insert the value")

        else:
            if chips.bet >chips.total:
                print(f'Sorry,not enough chips.The number of available chips : {chips.total}')
            else:
                break
"""
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('\nTake an additional card (Hit) or stay with the current cards (Stand). Enter h or s : ')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("The player remains with the current cards. Dealer's move ")
            playing = False

        else:
            print('Sorry, the answer is not understandable. Please enter h or s:')
            continue
        break

def show_some(player,dealer):
    print("\n                  Dealer's card : \n")
    print('',dealer.cards[0])
    print('',dealer.cards[1])
    print("\n                  Player card:\n",*player.cards,sep='\n')



def show_all(player,dealer):
    print("\t\tDealer card : ",*dealer.cards,sep='\n ')
    print("Dealer card =",dealer.value)
    print("\n\t\tPlayer card:",*player.cards,sep='\n ')
    print("Player card = ",player.value )
    print("\n\n")


def player_busts(player,dealer,chips):
    print('Player lost the game')
    chips.lose_bet()

def player_win(player,dealer,chips):
    print('Player won')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Player won the game!')
    chips.lose_bet()

def dealer_win(player,dealer,chips):
    print('Dealer won')
    chips.win_bet()

def push(player,dealer):
    print('Draw!')

    
while True:
    print("\n<<<<<<<<<Welcome to game Blackjack>>>>>>>>>>>")

    deck = Desk()
    deck.shuffle()

   

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    #print((player_hand.add_card(deck.deal())+player_hand.add_card(deck.deal())).values())
    player_chips = Chips()

    #take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <=21:

        while dealer_hand.value <17:

            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value >21:

            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:

            dealer_win(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:

            player_win(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    #print('\n The amount of player chips: {}'.format(player_chips.total))


    new_game = input('Do you want play again? : ')
    print('\n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks')
        break



