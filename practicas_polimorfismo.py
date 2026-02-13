"""palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for elemento in palabra, lista, tupla:
    print(len(elemento))"""


class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")

mago, arquero, samurai = Mago(), Arquero(), Samurai()

def personaje_defender(personaje):
    personaje.defender()

personajes = [mago, arquero, samurai]

for p in personajes:
    personaje_defender(p)