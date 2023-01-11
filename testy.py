class item:
    def __init__(self, n, q, u, up, lista):
        self.name = n
        self.quantity = float(q)
        self.unit = u
        self.unit_price = float(up)
        lista.append(self)

def show(lista):
    print("Dostępne towary")
    for a in lista:
        print(a.name)

items = []
item1 = item("Ancient Fruit", 2, "szt.", "550", items)
item2 = item("Pineapple", 15, "szt.", "300", items)
item3 = item("Coffee", 50, "szt.", "150", items)
show(items)