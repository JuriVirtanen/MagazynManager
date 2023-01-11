from curses import wrapper

class item:
    def __init__(self, n, q, u, up, lista):
        self.name = n
        self.quantity = float(q)
        self.unit = u
        self.unit_price = float(up)
        lista.append(self)

def show(stdscr, lista):
    stdscr.addstr("Aktualne stany magazynowe :")
    stdscr.addstr(1, 0, "Nazwa")
    stdscr.addstr(1, 15, "Ilość")
    stdscr.addstr(1, 30, "Jednostka")
    stdscr.addstr(1, 45, "Cena za jednostkę")

    for a in lista:
        stdscr.addstr(2, 0, )


def add_item():
    pass

def sell_item():
    pass

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getkey()



if __name__ == "__main__":
    items = []
    wrapper(main)
