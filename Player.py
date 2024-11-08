from Property import Property
import random
import Chance

class Player:


   def __init__ (self, name='Player', money=1500, position=None, is_turn=False):

      self.name = name 
      self.money = money
      self.position = position
      self.properties = list([])
      self.is_turn = is_turn

   
   def move(self, spaces: int) -> None:

      count = spaces

      while count > 0:
         self.position = self.position.next
         if self.position.id == 0:
            self.money += 200
            print(f"{self.name} passed Go, collect $200!")
         count -= 1
      Player.display_stats(self)
      Player.buy(self)
      print(' ')

   
   def buy(self) -> None:

      if self.position.is_owned == False and self.position.price != None:
         if self.position.group == 'Tax':
            self.money += self.position.price
            print(f"{self.name} landed on {self.position.name}: {self.position.price}")
            return

         response = input(f"Would {self.name} like to buy {self.position.name} for ${self.position.price}? Y/N \n")

         if response == 'Y':
            if self.money > self.position.price:
               self.position.is_owned = True
               self.properties += [self.position.name]
               self.money -= self.position.price
               return
            print(f"{self.name}, you don't have enough money...")


   def display_stats(self) -> None:

      print(f"{self.name} ------------------")
      print(f"Current balance: ${self.money}")
      print(f"Owned properties: {self.properties}")   
      

   def roll_dice(self) -> int:

      self.is_turn = False
      return random.randint(2, 12)


   # we are writing out the functions in response to chance
   def toGO(self):
      spaces = 40 - self.position.id
      self.move(spaces)

   def toBW(self):
      spaces = abs(39 - self.position.id)
      self.move(spaces)

   def moveBackThree(self):
      pass

   def toRR(self):
      spaces = 40 - self.posiition.id + 5
      self.move(spaces)


if __name__ == '__main__':
   test = Player()
   