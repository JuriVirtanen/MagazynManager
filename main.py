import curses

class item:
    def __init__(self, n, q, u, up, lista):
        self.name = n
        self.quantity = q
        self.unit = u
        self.unit_price = up
        lista.append(self)

def show(win, lista):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    yellow = curses.color_pair(1)
    cyan = curses.color_pair(2)
    win.clear()
    win.addstr("Aktualne stany magazynowe :")
    win.addstr(1, 0, "Nazwa", cyan)
    win.addstr(1, 25, "Ilość", cyan)
    win.addstr(1, 50, "Jednostka", cyan)
    win.addstr(1, 75, "Cena za jednostkę (PLN)", cyan)
    it = 0
    for a in lista:
        win.addstr(it + 2, 0, str(a.name), yellow)
        win.addstr(it + 2, 25, str(a.quantity), yellow)
        win.addstr(it + 2, 50, str(a.unit), yellow)
        win.addstr(it + 2, 75, str(a.unit_price), yellow) 
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
curses.start_color()
items = []
curses.wrapper(main)