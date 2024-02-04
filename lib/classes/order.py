
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self.average_price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and 1 <= new_price <= 10:
            self._price = new_price
        else:
            raise Exception("Price must be a number between 1 and 10")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        from customer import Customer
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception("customer must be an instance of Customer class")
        
    @property
    def coffee(self):
        return self._coffee 
    
    @coffee.setter
    def coffee(self, new_coffee):
        from coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception("coffee must be and instance of Coffee class")
        
        
    