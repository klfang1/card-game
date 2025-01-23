def main():
  class Card(object):
    def __init__(self, suit, value):
      self.suit = suit
      self.value = value

    def __repr__(self):
      suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
      values = ["Two", "Three","Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
      suit_name = suits[self.suit]
      value_name = values[self.value]
      return value_name + " of " + suit_name

  class StandardDeck(list):
    def __init__(self):
      super().__init__()
      suits = list(range(4))
      values = list(range(13))
      [[self.append(Card(i, j)) for i in suits] for j in values]

  deck = StandardDeck()
  for card in deck:
    print(card)
  print(len(deck))
  
if __name__ == "__main__":
  main()
