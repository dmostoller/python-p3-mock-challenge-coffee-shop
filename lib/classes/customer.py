class Customer:

    all = []

    def __init__(self, name):
        self.name = name

        self._coffees = []
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, 'name') and isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception("Name cannot be changed")


    def orders(self):
        return self._orders 
        
    def add_order(self, new_order=None):
        from order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        else:
            raise Exception("Order must be an instance of the Order class")
    
    orders = property(orders, add_order)

    def coffees(self):
        return list(set(self._coffees))

    def add_coffee(self, new_coffee=None):
        from coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffees.append(new_coffee)
        else:
            raise Exception("Coffee must be an instance of the Coffee class")
        
    coffees = property(coffees, add_coffee)


    def create_order(self, coffee_order, price):
        from coffee import Coffee
        if isinstance(coffee_order, Coffee) and isinstance(price, int):
            from order import Order
            Order(self, coffee_order, price)
        else:
            raise Exception("coffee must be an instance of the coffee class and price must be an integer")


    def __repr__(self):
        return f"Customer: {self.name}"