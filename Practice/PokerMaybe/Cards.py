import random
import time

## '♣' '♦' '♥' '♠'
global Deck

def ShuffleDeck():
    global Deck
    Deck = [(str(i), n, i) for i in range(2,11) for n in ('♣', '♦', '♥', '♠',)]  ## Form: List of tuples (Card Num, Suit, Value) Ex: (5, '♥', 5) or ('K', '♥', 10)
    for i in ('J', 'Q', 'K'):
        for n in ('♣', '♦', '♥', '♠',):
            Deck.append((i, n, 10))

    for n in ('♣', '♦', '♥', '♠',):
        Deck.append(('A', n, 11))
            
    random.shuffle(Deck)


def Deal(cards): ## Generator to pick random amount of cards to pass between players
    global Deck
    yield [Deck.pop() for _ in range(cards)]

def CardsValue(cards):
    value = 0
    for i in range(len(cards)):
        value += cards[i][2]
    return value

def BlackJack():
    global Deck
    cards = 2
    play = True
    

    while(play):
        flag = True
        print("\nDealer stays on 17, hits on 16")
        time.sleep(1)
        ShuffleDeck()

        player_cards = next(Deal(cards))
        dealer_cards = next(Deal(cards))
        BlackJackDisplay(player_cards, dealer_cards)

        print("\n1) Stay\n2) Hit")
        while flag:
            choice = input("1 or 2")

            if choice.strip() == '1':
                flag = False
            elif choice.strip() == '2':
                new_card = next(Deal(1))
                player_cards.append(new_card[0])
                BlackJackDisplay(player_cards, dealer_cards)

                if CardsValue(player_cards) > 21:
                    print("\nYou Busted, pay up")
                    flag = False
                    play = False
                else:
                    print("\n1) Stay\n2) Hit")
        ## Dealers turn
        while CardsValue(dealer_cards) < 17:
            new_card = next(Deal(1))
            dealer_cards.append(new_card[0])
            time.sleep(1)
            BlackJackDisplayEnd(player_cards, dealer_cards)

        if play:
            if CardsValue(player_cards) > CardsValue(dealer_cards):
                print("You win!\nDouble your chips!")

            elif CardsValue(player_cards) < CardsValue(dealer_cards):
                print("Dealer wins\nLose your chips")


                



def BlackJackDisplay(player, dealer):
    print("===================")
    print("\nDealer:        You:")
    print(f"{dealer[0][0]}{dealer[0][1]}            {player[0][0]}{player[0][1]}")
    print(f"FD              {player[1][0]}{player[1][1]}")
    if len(player) > 2:
        for i in range(len(player)-2):
            print(f"                {player[i+2][0]}{player[i+2][1]}")
    print("\nTotals:")
    print(f"    {dealer[0][2]}              {CardsValue(player)}")
    print("===================\n")
    
    
def BlackJackDisplayEnd(player, dealer):
    print("===================")
    print("\nDealer:        You:")
    for i in range(min(len(player), len(dealer))):
        print(f"    {dealer[i][0]}{dealer[i][1]}                {player[i][0]}{player[i][1]}")


    if len(player) > len(dealer):
        for i in range(len(player)-len(dealer)):
            print(f"                    {player[i+len(dealer)-1][0]}{player[i+len(dealer)-1][1]}")

    elif len(player) < len(dealer):
        for i in range(len(dealer)-len(player)):
                print(f"    {dealer[i+len(player)-1][0]}{dealer[i+len(player)-1][1]}")
    print("\nTotals:")
    print(f"    {CardsValue(dealer)}              {CardsValue(player)}")
    print("===================\n")




        
def Menu():
    print("\n---Welcome to the Casino---\n")
    print("\n---Pick a game to Play---")
