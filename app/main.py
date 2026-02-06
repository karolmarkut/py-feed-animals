Stwórz klasę Animal, której metoda __init__ przyjmuje trzy argumenty:

name: imię zwierzęcia.

appetite: liczba całkowita określająca, ile punktów jedzenia zwierzę potrzebuje, aby się najeść.

is_hungry: wartość logiczna (boolean) określająca, czy zwierzę jest głodne (domyślnie True).

class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            points = self.appetite
            self.is_hungry = False
            return points
        else:
            return 0

class Cat(Animal):
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = 3
        self.is_hungry = is_hungry
    def catch_mouse(self):
        print(f"The hunt began!")
2. Klasa Cat (Kot)
Wszystkie koty jedzą jednorazowo 3 punkty jedzenia i potrafią łapać myszy. Stwórz klasę Cat,
która dziedziczy po klasie Animal. Jej metoda __init__ powinna przyjmować:
name: imię kota.

is_hungry: domyślnie True.

Uwaga: Musisz wywołać metodę __init__ klasy nadrzędnej, ustawiając appetite na sztywno na wartość 3.

Dodatkowa metoda:

catch_mouse: powinna wypisać tekst: The hunt began!.