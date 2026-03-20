import tkinter as tk   # Import de la bibliothèque graphique Tkinter
import random          # Import pour générer du hasard (positions et valeurs)

TAILLE = 4  # Taille de la grille (4 lignes et 4 colonnes)


class Jeu2048:
    def __init__(self, fenetre):
        # On stocke la fenêtre principale
        self.fenetre = fenetre
        self.fenetre.title("2048")  # Titre de la fenêtre

        # Création de la grille logique (matrice 4x4 remplie de 0)
        self.grille = [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]

        # Création d'un conteneur pour afficher la grille
        self.cadre = tk.Frame(fenetre)
        self.cadre.pack()

        # Création des cases visuelles (labels)
        self.cellules = []
        for i in range(TAILLE):  # Pour chaque ligne
            ligne = []
            for j in range(TAILLE):  # Pour chaque colonne
                etiquette = tk.Label(
                    self.cadre,
                    text="",              # Texte vide au départ
                    width=5,
                    height=2,
                    font=("Arial", 24),
                    borderwidth=2,
                    relief="solid"
                )
                etiquette.grid(row=i, column=j)  # Placement dans la grille graphique
                ligne.append(etiquette)          # On ajoute la case dans la ligne
            self.cellules.append(ligne)          # On ajoute la ligne à la grille visuelle