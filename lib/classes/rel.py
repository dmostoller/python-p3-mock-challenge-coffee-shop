from coffee import Coffee
from customer import Customer
from order import Order


latte = Coffee("latte")
black = Coffee("black")
mocha = Coffee("mocha")
espresso = Coffee("espresso")

david = Customer("david")
john = Customer("john")
kelly = Customer("kelly")
meg = Customer("meg")

order1 = Order(meg, latte, 6)
order2 = Order(david, black, 3)
order3 = Order(kelly, mocha, 5)
order4 = Order(john, espresso, 2)
order5 = Order(david, espresso, 2)
order6 = Order(meg, latte, 6)
order7 = Order(kelly, latte, 6)
order8 = Order(david, mocha, 5)

print(order3.customer.name)