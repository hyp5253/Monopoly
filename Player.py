from Property import Property
import random

class Player:
   def __init__ (
      
      self, 
      name='Player', 
      money=1500, 
      position=0,  
      properties=[], 
      is_turn=False
      
      ):

      self.name = name 
      self.money = money
      self.position = position
      self.properties = properties
      self.is_turn = is_turn

   
   def move(self, spaces: int) -> None:
      count = spaces

      while count > 0:
         self.position = self.position.next
         count -= 1
      Player.buy(self)

   
   def buy(self) -> None:

      if self.position.is_owned == False:
         match self.position.id:
            case 2:
               print(f"{self.name} landed on {self.position.name}.")
               return 
            case 4:
               print(f"{self.name} landed on {self.position.name}.")
               self.money -= 200
               return
            case 7:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 10:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 17:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 20:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 22:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 30:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 33: 
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 36:
               print(f"{self.name} landed on {self.position.name}.")
               return
            case 38:
               print(f"{self.name} landed on {self.position.name}.")
               self.money -= 100
               return

         response = input(f"Would {self.name} like to buy {self.position.name} for ${self.position.price}? Y/N \n")

         if response == 'Y':
            if self.money > self.position.price:
               self.position.is_owned = True
               self.properties += [self.position.name]
               self.money -= self.position.price
               print(f"{self.name} now owns {self.position.name}.")
               return
            print(f"{self.name}, you don't have enough money...")
      
      
   def roll_dice(self) -> int:
      self.is_turn = False
      return random.randint(2, 12)

