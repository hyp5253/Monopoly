class Property:
   def __init__ (self, name="Placeholder", price=0, id=0, is_owned=False, next=None):
      self.name = name
      self.price = price
      self.id = id
      self.is_owned = is_owned
      self.next = next

      