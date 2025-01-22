def main():
  class Card(object):
    def __init__(self, suit, value):
      self.suit = suit
      self.value = value

  class StandardDeck(list):
    def __init(self):
      super().__init__()
      suits = list(range(4))
      values = list(range(13))
      [[self.append(Card(i, j)) for i in suits] for j in values]

  deck = StandardDeck()
  for i in range(len(deck)):
    print(i)
  for i in deck:
    print(i)
    print(i.suit)
    print(i.value)
  
if __name__ == "__main__":
  main()
