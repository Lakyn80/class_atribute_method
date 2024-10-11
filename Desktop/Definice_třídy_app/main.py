import tkinter as tk

# Definice třídy MyApp
class MyApp:
    def __init__(self, root):
        self.root = root  # Ukládáme si referenci na hlavní okno
        self.root.title("Jednoduchá aplikace")

        # Vytvoření tlačítka
        self.button = tk.Button(self.root, text="Klikni na mě!", command=self.say_hello)
        self.button.pack(pady=20)  # Zobrazení tlačítka na obrazovce

    # Definujeme metodu, která se zavolá po kliknutí na tlačítko
    def say_hello(self):
        print("Ahoj světe!")

# Vytvoření hlavního okna (objekt)
root = tk.Tk()

# Vytvoření instance třídy MyApp
app = MyApp(root)

# Spuštění aplikace
root.mainloop()
