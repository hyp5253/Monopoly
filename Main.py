import GameBoard as gb
from Player import Player

if __name__ == '__main__':
   test = gb.Board()
   player1 = Player(name='P1', position=test.start, is_turn=True)
   player2 = Player(name='P2', position=test.start)

# gameloop
   while True:
      if player1.is_turn:
         player1.move(player1.roll_dice())
         player2.is_turn = True
         if player1.position.id == 30:
            print(f"{player2.name} wins the game!")
            exit()   

      player2.move(player2.roll_dice())
      player1.is_turn = True
      if player2.position.id == 30:
         print(f"{player1.name} wins the game!")
         exit()


   
      
      


         

   