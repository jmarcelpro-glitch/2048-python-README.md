import random  # Permet d'utiliser des fonctions aléatoires

TAILLE = 4  # Taille de la grille (4x4)


# -------------------------
# CRÉER LA GRILLE
# -------------------------
def creer_grille():
    grille = []  # Liste vide qui va contenir la grille

    for i in range(TAILLE):  # Pour chaque ligne
        ligne = []  # Crée une nouvelle ligne

        for j in range(TAILLE):  # Pour chaque colonne
            ligne.append(0)  # Ajoute un 0 dans la ligne

        grille.append(ligne)  # Ajoute la ligne à la grille

    return grille  # Retourne la grille remplie de 0


# -------------------------
# AFFICHER LA GRILLE
# -------------------------
def afficher(grille):
    print("\n---------------------")  # Ligne de séparation

    for ligne in grille:  # Parcourt chaque ligne
        for valeur in ligne:  # Parcourt chaque case
            if valeur == 0:
                print(".", end=" ")  # Affiche un point si vide
            else:
                print(valeur, end=" ")  # Affiche le nombre
        print()  # Retour à la ligne

    print("---------------------")