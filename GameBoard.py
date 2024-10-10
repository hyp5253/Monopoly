from Property import Property

#(name, price, color)
info = [

('GO', None, None),   
('Mediterranean Avenue', 60, 'Brown'),
('Community Chest', None, None),
('Baltic Avenue', 60, 'Brown'),
('Income Tax', -200, None),
('Reading Railroad', 200, 'Railroad'),
('Oriental Avenue', 100, 'Lightblue'),
('Chance', None, None),
('Vermont Avenue', 100, 'Lightblue'),
('Connecticut Avenue', 120, 'Lightblue'),
('Just Visiting', None, None),
('St. Charles Place', 140, 'Pink'),
('Electric Company', 150, 'Utility'),
('States Avenue', 140, 'Pink'),
('Virginia Avenue', 160, 'Pink'),
('Pennsylvania RailRoad', 200, 'Railroad'),
('St. James Place', 180, 'Orange'),
('Community Chest', None, None),
('Tennessee Avenue', 180, 'Orange'),
('New York Avenue', 200, 'Orange'),
('Free Parking', None, None),
('Kentucky Avenue', 220, 'Red'),
('Chance', None, None),
('Indiana Avenue', 220, 'Red'),
('Illinois Avenue', 240, 'Red'),
('B.&.O Railroad', 200, 'Railroad'),
('Atlantic Avenue', 260, 'Yellow'),
('Ventor Avenue', 260, 'Yellow'),
('Waterworks', 150, 'Utility'),
('Marvin Gardens', 280, 'Yellow'),
('Go To Jail', None, None),
('Pacific Avenue', 300, 'Green'),
('North Carolina', 300, 'Green'),
('Community Chest', None, None),
('Pennsylvania Avenue', 320, 'Green'),
('Short Line', 200, 'Railroad'),
('Chance', None, None),
('Park Place', 350, 'Blue'),
('Luxury Tax', 100, None),
('Boardwalk', 400, 'Blue')

]

class Board:
   def __init__(self) -> None:
      self.start = Property(info[0][0], info[0][1], info[0][2])

      node = self.start
      for i in range(1, 40):
         node.next = Property(info[i][0], info[i][1], info[i][2], i)
         node = node.next
         if i == 39:
            node.next = self.start


   def display(self):
      curr = self.start
      count = 0

      while curr and count < 41:
         print(f"{curr.name} {curr.color}")
         curr = curr.next
         count += 1

if __name__ == '__main__':
   test = Board()
   test.display()
