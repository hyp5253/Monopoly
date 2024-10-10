class Property:
   def __init__ (
         
      self, 
      name="Placeholder", 
      price=0, 
      color=None,
      id=0, 
      is_owned=False, 
      next=None
      
      ):

      self.name = name
      self.price = price
      self.color = color
      self.id = id
      self.is_owned = is_owned
      self.next = next

      