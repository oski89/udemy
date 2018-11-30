'''
A BlackJack game
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def __str__(self):
        deck_string = 'The deck is:'
        for card in self.deck:
            deck_string += f'\n{card.__str__()}'
        return deck_string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = []  # start with an empty hand
        self.value = 0  # start with zero value
        self.aces = 0   # attribute to keep track of aces

    def __str__(self):
        hand_string = f'{self.name}\'s hand is:'
        for card in self.cards:
            hand_string += f'\n{card.__str__()}'
        return hand_string

    def add_card(self, card):
        # card passed in from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # start with a chip value of 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    chips.bet = 20
    '''
    while True:
        try:
            chips.bet = int(input('Place bet: '))
        except ValueError:
            print('Provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Insufficient funds. You have {chips.total} chips.')
            else:
                break
    '''


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or stand? (h or s) ')
        if x[:1].lower() == 'h':
            hit(deck, hand)
        elif x[:1].lower() == 's':
            print('Player stands. Dealers turn.')
            playing = False
        else:
            print('Not a valid input. Enter h or s.')
            continue
        break


def show_some(player, dealer):
    print("\nDealer's hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep='\n ')
    print("Player's hand value =", player.value)


def show_all(player, dealer):
    print("\nDealer's hand:", *dealer.cards, sep='\n ')
    print("Dealer's hand value =", dealer.value)
    print("\nPlayer's hand:", *player.cards, sep='\n ')
    print("Player's hand value =", player.value)


def player_busts(player, dealer, chips):
    print('Player busted!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Dealer busted!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.lose_bet()


def push(player, dealer):
    print("It's a draw!")


while True:

    # Print an opening statement
    print('Welcome to the Black Jack table!')

    # Create a deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Create a list of all hands
    hands = []
    player_hand = Hand('Player')
    hands.append(player_hand)
    dealer_hand = Hand('Dealer')
    hands.append(dealer_hand)

    # Deal two cards to all hands
    [hand.add_card(deck.deal()) for hand in hands for _ in range(0, len(hands))]

    # Create player chips
    player_chips = Chips()

    # Take bets
    take_bet(player_chips)

    # Display cards (one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:

        # If player gets blackjack = instant win
        player_insta_win = False
        if player_hand.value == 21:
            player_wins(player_hand, dealer_hand, player_chips)
            player_insta_win = True
            break

        # Prompt for hit or stand
        hit_or_stand(deck, player_hand)

        # Display cards (one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand > 21, call player_busts() and break
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If player hasn't busted, play dealers hand until it reaches at least 17
    if player_hand.value <= 21 and not player_insta_win:

        while dealer_hand.value < 17 and dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # If dealer's hand > 21, call dealer_busts() and break
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Print the remaining chips value
    print(f'\nPlayer total chips are at: {player_chips.total}')

    # Ask for a new round
    while True:
        new_game = input("Would you like to play again? (y or n) ")
        if new_game[:1].lower() not in 'yn':
            print('Not a valid input. Enter y or n.')
            continue
        else:
            break

    if new_game[:1].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break
