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
('Kentucky Avenue', 220),
('Chance', None),
('Indiana Avenue', 220),
('Illinois Avenue', 240),
('B.&.O Railroad', 200),
('Atlantic Avenue', 260),
('Ventor Avenue', 260),
('Waterworks', 150),
('Marvin Gardens', 280),
('Go To Jail', None),
('Pacific Avenue', 300),
('North Carolina', 300),
('Community Chest', None),
('Pennsylvania Avenue', 320),
('Short Line', 200),
('Chance', None),
('Park Place', 350),
('Luxury Tax', 100),
('Boardwalk', 400)

]

class Board:
   def __init__(self) -> None:
      self.start = Property(info[0][0], info[0][1])

      node = self.start
      for i in range(1, 40):
         node.next = Property(info[i][0], info[i][1], i)
         node = node.next
         if i == 39:
            node.next = self.start


   def display(self):
      curr = self.start
      count = 0

      while curr and count < 41:
         print(f"{curr.name}")
         curr = curr.next
         count += 1


