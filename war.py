from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
cards = []


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return str(self.rank) + ' of ' + self.suit


class Player:
    def __init__(self, name, cards):
        """
        :param name:
        :param list cards:
        """
        self.name = name
        self.cards = cards
        self.table = []


class Deck:
    def __init__(self, cards):
        """
        :param Card[] cards:
        """
        self.cards = cards


def build_deck():
    for suit in suits:
        for rank in ranks:
            cards.append(Card(suit, rank))
    deck = Deck(cards)
    shuffle(deck.cards)
    return deck

def deal_cards(deck):
    while len(player1.cards) < (len(deck.cards) / 2):
        for card in deck.cards:
            player1.cards.append(card)
            deck.cards.pop(0)

    player2.cards = deck.cards

def clear_tables():
    player1.table = []
    player2.table = []

player1 = Player('Player 1', [])
player2 = Player('Player 2', [])

deck = build_deck()
deal_cards(deck)

while len(player1.cards) != 0 and len(player2.cards) != 0:

    player1.table.append(player1.cards.pop())
    player2.table.append(player2.cards.pop())

    print("Player 1 drew {}".format(player1.table[-1]))
    print("Player 2 drew {}".format(player2.table[-1]))

    if player1.table[-1].value > player2.table[-1].value:
        print("Player 1 wins the battle")
        player1.cards.extend(player1.table)
        player1.cards.extend(player2.table)
        clear_tables()
    elif player2.table[-1].value > player1.table[-1].value:
        print("Player 2 wins the battle")
        player2.cards.extend(player1.table)
        player2.cards.extend(player2.table)
        clear_tables()
    else:
        print("war")

        table_length = len(player1.table)
        if len(player1.cards) < table_length + 4:
            player2.cards.extend(player1.table)
            player2.cards.extend(player2.table)
            player2.cards.extend(player1.cards)

            player1.cards = []
            clear_tables()
            break
        if len(player2.cards) < table_length + 4:
            player1.cards.extend(player2.table)
            player1.cards.extend(player1.table)
            player1.cards.extend(player2.cards)
            player2.cards = []
            clear_tables()
            break
        while len(player1.table) <= table_length + 3:
            player1.table.append(player1.cards.pop())
        while len(player2.table) <= table_length + 3:
            player2.table.append(player2.cards.pop())



print("Player 1 has {} cards".format(len(player1.cards)))
print("Player 2 has {} cards".format(len(player2.cards)))


