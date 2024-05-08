import datetime

class Client:
    def __init__(self, id, name, surname, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email

class Item:
    def __init__(self, id, name, price, weight):
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight

class Transaction:
    def __init__(self, id, client_id, item_ids):
        self.id = id
        self.client_id = client_id
        self.item_ids = item_ids
        self.datetime = datetime.datetime.now()

client1 = Client('10001', 'Anna', 'Bērziņa', 'anna.b@someemail.com')
item1 = Item('90001', 'Monitors', 200, 6)
item2 = Item('90002', 'Ledusskapis', 400, 50)
item3 = Item('90003', 'T-krekls', 18, 0.2)
transaction1 = Transaction('50001', '10001', ['90001', '90003'])

