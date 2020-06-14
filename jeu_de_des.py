"""Un jeu de hasard se déroule de la façon suivante: On paie 2 euros pour jouer puis on lance 2 dés non truqués tétraédriques.
Si le joueur obtient un double, il récupère sa mise et reçoit la somme des points marqués.
Sinon il ne reçoit rien et perd sa mise. Écrire un programme pour simuler ce jeu. Conseilleriez-vous ce jeu?"""

import random

p = 0
a = 10

go = input(f"Vous partez avec {a}€ en poche. Misez 2€ et tentez de faire un double avec les dés! o/n ")

while go == "o" :
    de01 = random.randint(1, 6)
    de02 = random.randint(1, 6)
    
    if de01 == de02 :
        print(f"Bravo! vous avez fait un double {de01}!")
        p = de01 + de02 
        a += 2
    elif de01 != de02 :
        print(f"Dommage! Vous avez fait un {de01} et un {de02}.")
        a-= 2

    print(f"Vous avez {a}€ et {p} points!")

    if a == 0 :
        print("DOMMAGE! Vous avez tout perdu.")
        break
    if p == 30 :
        print("FELICITATIONS! Vous avez gagné vos 30 points")
        break

    go = input("Misez 2€ et tentez de faire un double avec les dés! o/n ")
