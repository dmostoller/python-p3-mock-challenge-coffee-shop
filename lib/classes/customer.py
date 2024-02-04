class Customer:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, 'name') and isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception("Name cannot be changed")



        
    def orders(self, new_order=None):
        from classes.order import Order
        pass
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        pass