class item:
    def __init__(self, n, q, u, up, lista):
        self.name = n
        self.quantity = float(q)
        self.unit = u
        self.unit_price = float(up)
        lista.append(self)

items = []
item1 = item("Ancient Fruit", 2, "szt.", "550", items)
print(item1.name)
print(items)