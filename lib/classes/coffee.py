class Coffee:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) < 16:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 1-15 characters in length")    

        
    
    def orders(self, new_order=None):
        from order import Order
        pass
    
    def customers(self, new_customer=None):
        from customer import Customer
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass



latte = Coffee("latte")

# print(latte.name)