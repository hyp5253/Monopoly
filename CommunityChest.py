class Card:
   def __init__ (self, msg=None, next=None):
      self.msg = msg
      self.next = next

#each of these cards will have some related function call most likely


community_chest = [

("Advance to GO (Collect $200)."),
("Bank error in your favor. Collect $200"),
("Income tax refund. Collect $20."),
("You inherit $100."),
("Life insurance matures. Collect $100."),
("Holiday fund matures. Recieve $100."),
("From sale of stock you get $50."),
("Recieve $25 consultancy fee."),
("You have won sexond prize in a beauty contest. Collect $10"),
("It's your birthday. Collect $10 from every player."),
("Pay hospital fees of $100."),
("Pay school fees of $50."),
("Doctor's fees. Pay $50."),
("You are assessed for street repairs: $40 per house, $115 per hotel."),
("Get out of jail free. This card may be kept until needed or traded."),
("Go to jail. Go directly to jail, do not pass GO, do not collect $200.")

]

class ChestDeque:
   def __init__ (self):
      self.top = Card(community_chest[0])
      self.bot = self.top

      curr = self.top
      for i in range(1, len(community_chest)):
         curr.next = Card(community_chest[i])
         curr = curr.next

   # most likely will have to add function calls within each card
   # this could be the second part of each tuple
   # each function gets called when the player lands on an appropriate square
   def get_top(self):
      card = self.top
      self.top = self.top.next
      self.bot.next = card
      self.bot = card
      print(card.msg)

   def shuffle(self):
      pass



