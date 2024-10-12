from Property import Property
import random

class Player:
   """
   A class used to represent a player

   Attributes
   ----------
   name : str
      the name of the player
   money : int
      the amount of money a player has
   position : Property
      a node that indicates the position on the gameboard
   properties : 
      #FIXME
   is_turn : bool
      a flag to indicate if it is the player's turn

   Methods
   -------
   move(spaces)
      Moves the player x amount of spaces along the gameboard and updates position
   buy()
      Called inside move and allows player to buy property if available
   roll_dice()
      Returns a value representing a two dice roll
   """

   def __init__ (self, name='Player', money=1500, position=None,  properties=[], is_turn=False):
      """
      Parameters
      ----------
      name : str, optional
         The default name given is Player
      money : int, optional
         Money amount defaults to start amount of 1500
      position : Property, optional
         This value in None until the gameboard is intialized in gameloop
      properties : 
         #FIXME
      is_turn : bool, optional
         It is not the player's turn by default
      """

      self.name = name 
      self.money = money
      self.position = position
      self.properties = properties
      self.is_turn = is_turn

   
   def move(self, spaces: int) -> None:
      """
      Moves the player x amounn of spaces along the gameboard and updates position

      Parameters
      ----------
      spaces : int
         A value that is gotten from the roll_dice method
      """

      count = spaces

      while count > 0:
         self.position = self.position.next
         if self.position.id == 0:
            self.money += 200
            print("You passed Go, collect $200!")
         count -= 1
      Player.buy(self)
      print(' ')

   
   def buy(self) -> None:
      """
      Allows a player to buy a property if available
      """

      if self.position.is_owned == False and self.position.price != None:
         if self.position.group == 'Tax':
            self.money -= self.position.price
            print(f"{self.name} landed on {self.position.name}: - ${self.position.price}")
            return

         response = input(f"Would {self.name} like to buy {self.position.name} for ${self.position.price}? Y/N \n")

         if response == 'Y':
            if self.money > self.position.price:
               self.position.is_owned = True
               self.properties += [self.position.name]
               self.money -= self.position.price
               return
            print(f"{self.name}, you don't have enough money...")
      
      
   def roll_dice(self) -> int:
      """
      Simulates the rolling of a pair of dice and returns a bounded random int
      """

      self.is_turn = False
      return random.randint(2, 12)

if __name__ == '__main__':
   test = Player()
   print(test.__doc__)
   