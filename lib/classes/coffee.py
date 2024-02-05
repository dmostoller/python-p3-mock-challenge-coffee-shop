class Coffee():

    all = []

    def __init__(self, name):
        self.name = name

        Coffee.all.append(self)

        self._customers = []
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) < 16:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 1-15 characters in length")    

    def orders(self):
        return self._orders
        
    def add_order(self, new_order=None):
        from order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        else:
            raise Exception("Order must be an instance of the Order class")
    
    orders = property(orders, add_order)

    def customers(self):
        return list(set(self._customers))

    def add_customer(self, new_customer=None):
        from customer import Customer
        if isinstance(new_customer, Customer):
            self.customers.append(new_customer)
        else:
            raise Exception("Coffee must be an instance of the Coffee class")
        
    customers = property(customers, add_customer)
    
    def num_orders(self):
        coffees_ordered = {}

        for coffee in Coffee.all:
            name = coffee.name
            if name not in coffees_ordered:
                coffees_ordered[name] = 1
            else:
                coffees_ordered[name] += 1
        
        return coffees_ordered[self.name]
    
    def average_price(self):
        pass

    def __repr__(self):
        return f"Coffee: {self.name}"


