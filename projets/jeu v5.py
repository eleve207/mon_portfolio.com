# Créé par julie, le 06/11/2024 en Python 3.7
import random
t=0

#choisir le niveau
niveau=int(input("Choisir un niveau de difficulté entre 1 et 3 : "))
if niveau==1:
#L'ordinateur choisit un nombre entier en 0 et 100
    nombre_choisi_par_ordinateur=random.randint(0,100)
    nombre_choisi_par_utilisateur=int(input("Deviner les nombre entre 0 et 100"))
elif niveau==2:
#L'ordinateur choisit un nombre entier en 0 et 200
    nombre_choisi_par_ordinateur=random.randint(0,200)
    nombre_choisi_par_utilisateur=int(input("Deviner les nombre entre 0 et 200"))
else:
#L'ordinateur choisit un nombre entier en 0 et 300
    nombre_choisi_par_ordinateur=random.randint(0,300)
    nombre_choisi_par_utilisateur=int(input("Deviner les nombre entre 0 et 300"))
#demander un nombre à l'utilisateur
nombre_choisi_par_utilisateur=int(input("Deviner le nombre "))
while nombre_choisi_par_utilisateur!=nombre_choisi_par_ordinateur and t!=10:
# on réduit le nombre de tentatives à 10
    t=t+1
    if nombre_choisi_par_utilisateur>nombre_choisi_par_ordinateur:

# on rajoute un message d'erreur pour les mauvaise réponses
        print(nombre_choisi_par_utilisateur, "est faux")
        print("C'est moins")
        nombre_choisi_par_utilisateur=int(input("Deviner le nombre "))
    else:
        print(nombre_choisi_par_utilisateur, "est faux")
        print("C'est plus")
        nombre_choisi_par_utilisateur=int(input("Deviner le nombre "))

#l'ordinateur dit quand c'est gagné ou quand c'est perdu
if nombre_choisi_par_utilisateur==nombre_choisi_par_ordinateur:
        print("gagné")
else:
        print("perdu")