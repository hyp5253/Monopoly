class Property:
   """
   Is used to represent a property area on the gameboard

   Attributes
   ----------
   name : str, optional
      The name of property is stored here, but defaults to Placeholder
   price : int, optional
      Price of the property
   group : str, optional
      Represents the group of properties to which this property belongs
   id : int, optional
      Additional way to represent the property besides name
   is_owned : bool, optional 
      Represents the state of property and if it is currently owned
   next : Property, optional
      This field is taken care of when the Gameboard is instantiated
   """

   def __init__ (self, name="Placeholder", price=0, group=None,id=0, is_owned=False, next=None):

      self.name = name
      self.price = price
      self.group = group
      self.id = id
      self.is_owned = is_owned
      self.next = next

if __name__ == '__main__':
   test = Property()
   print(test.__doc__) 