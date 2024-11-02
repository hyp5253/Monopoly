class Card:
   def __init__ (self, msg=None, next=None):
      self.msg = msg
      self.next = next

chance = [

("Advance to GO (Collect $200)."),
("Advance to Boardwalk."),
("Go back three spaces."),
("Take a trip to Reading Railroad. If you pass GO collect $200."),
("Advance to the nearest railroad. Pay owner 2x rental if owned else you can buy it."),
("Advance to the nearest railroad. Pay owner 2x rental if owned else you can buy it."),
("Advance to Illinois Avenue. If you pass GO collect $200."),
("Advance to St. Charles Place. If you pass GO collect $200."),
("Advance to the nearest utility. Pay owner 10x roll amount if owned else you can buy it."),
("Bank pays you dividend of $50."),
("Your building loan matures. Collect $150."),
("Pay speeding fine $15."),
("You have been elected chairman of the board. Pay each player $50."),
("Make general repairs on all your property: $25 for each house, $100 for each hotel."),
("Get out of jail free. This card may be kept until needed or traded."),
("Go to jail. Go directly to jail, do not pass GO, do not collect $200.")

]

class ChanceDeque:
   def __init__ (self):
      self.top = Card(chance[0])
      self.bot = self.top

      curr = self.top
      for i in range(1, len(chance)):
         curr.next = Card(chance[i])
         curr = curr.next

   def get_top(self):
      card = self.top
      self.top = self.top.next
      self.bot.next = card
      self.bot = card
      print(card.msg)

   def shuffle(self):
      pass
