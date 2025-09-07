class Customer:

  def __init__(self , name , gender , address):
    self._name = name 
    self._pin = gender
    self._address = address
    
  def print_address(self):
    print (self._address._city , self._address._pin , self._address._state)

  def edit_profile(self , new_name ,new_city , new_pin , new_state):
    self._name = new_name
    self._address.edit_address(new_city,new_pin,new_state)


class Address:

  def __init__(self , city , pin , state ):
    self._city  = city 
    self._pin = pin 
    self._state = state

  def edit_address(self , new_city, new_pin, new_state):
    self._city = new_city
    self._pin = new_pin
    self._state = new_state

add1 = Address("ballia" , 277205 , "uttarpradesh")
obj1 = Customer("ishan" , "male" , add1)

obj1.print_address()

obj1.edit_profile("dhruv" , "pratapgarh" , 248298 , "assam")
obj1.print_address()