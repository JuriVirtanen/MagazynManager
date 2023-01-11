import curses

class item:
    def __init__(self, n, q, u, up, lista):
        self.name = n
        self.quantity = float(q)
        self.unit = u
        self.unit_price = float(up)
        lista.append(self)

def show(win, lista):
    win.addstr("Aktualne stany magazynowe :")
    win.addstr(1, 0, "Nazwa")
    win.addstr(1, 15, "Ilość")
    win.addstr(1, 30, "Jednostka")
    win.addstr(1, 45, "Cena za jednostkę")
    it = 0
    for a in lista:
        win.addstr(it + 2, 0, a.name)
        it += 1
    win.refresh()

def add_item():
    pass

def sell_item():
    pass

def main(stdscr):
    item1 = item("Ancient Fruit", 2, "szt.", "550", items)
    item2 = item("Pineapple", 15, "szt.", "300", items)
    item3 = item("Coffee", 50, "szt.", "150", items)
    stdscr.clear()
    stdscr.refresh()
    show(stdscr, items)
    stdscr.getkey()




stdscr = curses.initscr()
items = []
curses.wrapper(main)
