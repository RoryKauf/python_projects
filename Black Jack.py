import random
import time

suites = ["hearts", "diamonds", 'spades', 'clubs']
ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King', "Ace"]
d = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

class Card():
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suite}"

class Deck():
    def __init__(self):
        self.deck = []
        for s in suites:
            for n in ranks:
                card = Card(s, n)
                self.deck.append(card)

    def __str__(self):
        s = ""
        for card in self.deck:
            s += card.__str__() + "\n"
        return s

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck[-1]
        self.deck = self.deck[:-1]
        return single_card

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        s = ""
        for card in self.cards:
            s += card.__str__() + "\n"
        return s

    def add_card(self, card):
        self.cards.append(card)
        self.value += d[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Bet():
    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def player_turn():
    while True:
        if player_hand.value <= 21:
            h_or_s = input("Would you like to hit (h) or stick (s)?\n")
            if  h_or_s.lower() =="h":
                new_card = d_1.deal()
                print(f"Your card is the {new_card}")
                player_hand.add_card(new_card)
                player_hand.adjust_for_ace()
                time.sleep(0.5)
                print(f"Your hand now scores {player_hand.value} and contains:\n{player_hand}")
            else:
                time.sleep(0.5)
                print(f"Your hand scores {player_hand.value}\n")
                break
        else:
            time.sleep(1.0)
            print(f"You are bust\n")
            break

def house_turn():
    while True:
        if house_hand.value < 17:
            time.sleep(1)
            new_card = d_1.deal()
            house_hand.add_card(new_card)
            house_hand.adjust_for_ace()
            print(f"The house's new card is the {new_card}.\nThe house's hand now scores {house_hand.value}")
        elif house_hand.value > 21:
            time.sleep(1.0)
            print(f"The house is bust\n")
            break
        else:
            time.sleep(1.5)
            print(f"The house has stuck\n")
            break

def bet():
    min_bet = 50
    while True:
        try:
            print(f"Your total is {player_pot.total}")
            player_pot.bet = int(input("How much would you like to bet?\n"))
            if player_pot.bet >= min_bet:
                break
            else:
                print("You must be at least 50")
        except:
            print("Please only enter a number")

def results():
    print(f"Your score is {player_hand.value} and the house's score is {house_hand.value}")
    if house_hand.value < 22:
        if player_hand.value > house_hand.value:
            player_pot.win_bet()
            print(f"You won!!\n")
            time.sleep(0.8)
            print(f"You've had {player_pot.bet} add to you pot.\nYour new total is {player_pot.total}")
        elif player_hand.value < house_hand.value:
            player_pot.lose_bet()
            print(f"You lost\n")
            time.sleep(0.8)
            print(f"You've had {player_pot.bet} taken from your pot.\nYour new total is {player_pot.total}")
        else:
            print(f"It's a draw")
            time.sleep(0.8)
            print(f" your pot is the same. It's {player_pot.total}")
    else:
        player_pot.win_bet()
        print(f"The house went bust, you win!!\nYou've had {player_pot.bet} add to you pot.\nYour new total is {player_pot.total}")

def first_cards():
    p1 = d_1.deal()
    player_hand.add_card(p1)
    print(f"Your first cards is a {p1}")
    time.sleep(1.0)
    p2 = d_1.deal()
    player_hand.add_card(p2)
    print(f"Your second cards is a {p2}")
    time.sleep(1.0)
    h1 = d_1.deal()
    house_hand.add_card(h1)
    print(f"The house's first cards is a {h1}")
    time.sleep(1.0)
    h2 = d_1.deal()
    house_hand.add_card(h2)
    print("The house's second card is dealt and hidden")
    return h2

def another_game():
    while True:
        p_a = input("Would you like to play again? Y/N")
        if p_a.lower() == "y":
            play_again = True
            break
        elif p_a.lower() == "n":
            play_again = False
            break
        else:
            print("Please only enter Y or N")
    return play_again

def game():
    bet()
    h2 = first_cards()
    player_turn()
    if player_hand.value < 22:
        time.sleep(1.0)
        print(f"The house' hidden card was {h2}, their hand now scores {house_hand.value}\n")
        house_turn()
        results()
    else:
        player_pot.lose_bet()
        print(f"You went bust. You've had {player_pot.bet} taken from your pot.\nYour new total is {player_pot.total}")

play_again = True
player_pot = Bet()
while play_again:
    d_1 = Deck()
    d_1.shuffle()
    player_hand = Hand()
    house_hand = Hand()
    game()
    time.sleep(1)
    play_again = another_game()

