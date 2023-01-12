import curses
from curses.textpad import Textbox

class item:
    def __init__(self, n, q, u, up, lista): # DONE
        self.name = n
        self.quantity = q
        self.unit = u
        self.unit_price = up
        lista.append(self)

def show(lista): # DONE
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    yellow = curses.color_pair(1)
    cyan = curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr("Aktualne stany magazynowe:")
    stdscr.addstr(1, 0, "Nazwa", cyan)
    stdscr.addstr(1, 25, "Ilość", cyan)
    stdscr.addstr(1, 50, "Jednostka", cyan)
    stdscr.addstr(1, 75, "Cena za jednostkę (PLN)", cyan)
    it = 0
    for a in lista:
        stdscr.addstr(it + 2, 0, str(a.name), yellow)
        stdscr.addstr(it + 2, 25, str(a.quantity), yellow)
        stdscr.addstr(it + 2, 50, str(a.unit), yellow)
        stdscr.addstr(it + 2, 75, str(a.unit_price), yellow) 
        it += 1
    stdscr.addstr("\nCo chciałbyś zrobić? (help - wyświetla liste dostępnych opcji): ")
    stdscr.refresh()

def add_item(lista):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    yellow = curses.color_pair(1)
    cyan = curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr("Aktualne stany magazynowe:")
    stdscr.addstr(1, 0, "Nazwa", cyan)
    stdscr.addstr(1, 25, "Ilość", cyan)
    stdscr.addstr(1, 50, "Jednostka", cyan)
    stdscr.addstr(1, 75, "Cena za jednostkę (PLN)", cyan)
    it = 0
    for a in lista:
        stdscr.addstr(it + 2, 0, f"({it + 1}) {str(a.name)}", yellow)
        stdscr.addstr(it + 2, 25, str(a.quantity), yellow)
        stdscr.addstr(it + 2, 50, str(a.unit), yellow)
        stdscr.addstr(it + 2, 75, str(a.unit_price), yellow) 
        it += 1
    stdscr.addstr("\nWpisz back w którymkolwiek momencie żeby powrócić\nWybierz indeks produktu lub podaj nazwę nowego: ")
    stdscr.refresh()
    a = stdscr.getyx()
    okno1 = curses.newwin(1, 30, a[0], a[1])
    box1 = Textbox(okno1)
    box1.edit()
    nazwa = box1.gather()
    nazwa = nazwa[:-1]
    if nazwa == "back":
        return lista

    numer = True
    try:
        int(nazwa)
    except:
        numer = False
    if numer == True:
        stdscr.refresh()
        stdscr.addstr("\nPodaj ilość: ")
        stdscr.refresh()
        a = stdscr.getyx()
        okno = curses.newwin(1, 30, a[0], a[1])
        box = Textbox(okno)
        box.edit()
        ilosc = box.gather()
        ilosc = ilosc[:-1]
        if ilosc == "back":
            return lista

        lista[int(nazwa) - 1].quantity += int(ilosc)
    else:
        stdscr.refresh()
        stdscr.addstr("\nPodaj ilość: ")
        stdscr.refresh()
        a = stdscr.getyx()
        okno = curses.newwin(1, 30, a[0], a[1])
        box = Textbox(okno)
        box.edit()
        ilosc = box.gather()
        ilosc = ilosc[:-1]
        if ilosc == "back":
            return lista

        stdscr.refresh()
        stdscr.addstr("\nPodaj jednostkę: ")
        stdscr.refresh()
        a = stdscr.getyx()
        okno = curses.newwin(1, 30, a[0], a[1])
        box = Textbox(okno)
        box.edit()
        jednostka = box.gather()
        jednostka = jednostka[:-1]
        if jednostka == "back":
            return lista

        stdscr.refresh()
        stdscr.addstr("\nPodaj cenę za jednostkę: ")
        stdscr.refresh()
        a = stdscr.getyx()
        okno = curses.newwin(1, 30, a[0], a[1])
        box = Textbox(okno)
        box.edit()
        cena = box.gather()
        cena = cena[:-1]
        if nazwa == "back":
            return lista

        item(nazwa, int(ilosc), jednostka, cena, lista)

    return lista

def sell_item():
    pass

def ask(): # DONE
    a = stdscr.getyx()
    okno = curses.newwin(1, 20, a[0], a[1])
    box = Textbox(okno)
    box.edit()
    wybor = box.gather()
    return wybor

def help(): # DONE
    stdscr.clear()
    stdscr.addstr(0, 0, "show - wyświetla stan magazynowy")
    stdscr.addstr(1, 0, "add - dodanie produktu do magazynu")
    stdscr.addstr(2, 0, "sell - sprzedaż produktu z magazynu")
    stdscr.addstr(3, 0, "sum - łączna wartość produktów w magazynie")
    stdscr.addstr(4, 0, "income - łączna wartość sprzedanych produktów")
    stdscr.addstr(5, 0, "revenue - uzyskany zysk")
    stdscr.addstr(7, 0, "Naciśnij przycisk na klawiaturze by powrócić")
    stdscr.refresh()
    stdscr.getkey()

def get_costs(): # wartość rzeczy w magazynie
    pass

def get_income(): # wartość sprzedanych rzeczy
    pass

def show_revenue(): # zysk
    pass

def main(stdscr):
    item1 = item("Ancient Fruit", 2, "szt.", "550", items)
    item2 = item("Pineapple", 15, "szt.", "300", items)
    item3 = item("Coffee", 50, "szt.", "150", items)
    stdscr.clear()
    show(items)
    while True:
        show(items)
        move = ask()
        if move == "help ":
            help()

        elif move == "show ":
            continue

        elif move == "add ":
            add_item(items)


stdscr = curses.initscr()
curses.start_color()
items = []
curses.wrapper(main)