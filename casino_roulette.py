import random


argent_depart = int(input("Quel montant avez_vous en poche? "))
tours = int(input("Combien de tours voulez-vous tenter? "))
print (f"Vous commencez avec $ {argent_depart} et vous jouez pour {tours} tours.")


partie = 0
while partie < tours:
    croupier = random.randrange (0, 50)

    if croupier % 2 == 0 :
        couleur_c = "rouge"
    else :
        couleur_c = "noir"


    mise_argent = int(input("Combien misez vous? "))
    mise_nombre = int(input("Sur quel numéro? "))


    if mise_nombre % 2 == 0 :
        couleur_u = "rouge"
    else :
        couleur_u = "noir"

    if mise_nombre == croupier:
        argent_depart = argent_depart + (mise_argent * 3)
        print(f"Bravo, vous remportez 3 fois votre mise avec le {croupier}. Vous avez ${argent_depart}")
    elif mise_nombre != croupier and couleur_c == couleur_u:
        argent_depart = round(argent_depart + (mise_argent * 0.5))
        print(f"Presque, vous remportez 50% de votre mise car votre numero est {couleur_c} comme le {croupier}. Vous avez ${argent_depart}")
    else :
        argent_depart = argent_depart - mise_argent
        print(f"Vous avez perdu {mise_argent}, le nombre était {croupier}. Vous avez ${argent_depart}")


    partie += 1

print(f"Vous repartez avec ${argent_depart}.")



