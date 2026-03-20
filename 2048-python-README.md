import tkinter as tk   # Bibliothèque pour créer l'interface graphique
import random          # Pour générer des tuiles aléatoires

SIZE = 4  # Taille de la grille (4x4)


class Game2048:
    def __init__(self, root):
        self.root = root                     # Fenêtre principale
        self.root.title("2048")              # Titre de la fenêtre

        # Création de la grille 4x4 remplie de 0
        self.grid = [[0]*SIZE for _ in range(SIZE)]

        # Frame (conteneur) pour afficher la grille
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Création des cellules graphiques (labels)
        self.cells = []
        for i in range(SIZE):                # Parcourt les lignes
            row = []
            for j in range(SIZE):            # Parcourt les colonnes
                label = tk.Label(
                    self.frame,
                    text="",                 # Texte vide au départ
                    width=5,
                    height=2,
                    font=("Arial", 24),
                    borderwidth=2,
                    relief="solid"
                )
                label.grid(row=i, column=j)  # Placement dans la grille
                row.append(label)
            self.cells.append(row)


            import random
def partie():
pass
def creer_grille n = 4 ) :
# 4x4 remplie de zéros (cases vides
return [[0]*n for in range(n)] -
def ajout_tuile (grille):
tuile=random.randint(2 and 4)
pass
def deplacer_tuile(grille, orientation):
pass
def score(grille):
pass
def relancer_partie():
pass
