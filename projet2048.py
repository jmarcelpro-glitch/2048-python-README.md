import tkinter as tk
from tkinter import messagebox, filedialog
import random

# la grille du jeu (4x4)
grille = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

score = 0
en_jeu = False

# couleurs pour chaque valeur de tuile . Les couleurs sont prit sur internet
couleurs = {
    0:    "#e99ae0",
    2:    "#f7c4f2",
    4:    "#f2a8eb",
    8:    "#d4a8e8",
    16:   "#b8a8e8",
    32:   "#9ab8e8",
    64:   "#7ab8e8",
    128:  "#5aaad4",
    256:  "#4a9ac4",
    512:  "#3a8ab4",
    1024: "#2a7aa4",
    2048: "#1a6a94",
}


# ---- fonctions de logique ----  

def cases_vides():
    vides = []
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                vides.append((i, j))
    return vides


def ajouter_tuile ():
    case_vide =[]
    for i in range (4) :
        for j in range (4):
             if grille[i][j]==0:
                case_vide.append((i,j))
    i, j = random.choice(case_vide) #choisir au hasard une case vide
    if random.random() < 0.9:
        valeur = 2
    else:
        valeur = 4
    grille[i][j] = valeur  #placer la tuile dans la grille
    return grille


def deplacer_gauche():
    global score
    modifie = False
    for i in range(4):
        # on enleve les zeros
        ligne = []
        for v in grille[i]:
            if v != 0:
                ligne.append(v)

        # on fusionne
        j = 0
        while j < len(ligne) - 1:
            if ligne[j] == ligne[j + 1]:
                ligne[j] = ligne[j] * 2
                score += ligne[j]
                ligne.pop(j + 1)
            j += 1

        # on remet les zeros
        while len(ligne) < 4:
            ligne.append(0)

        if ligne != grille[i]:
            modifie = True
        grille[i] = ligne
    return modifie


def deplacer_droite():
    global score
    modifie = False
    for i in range(4):
        ligne = []
        for v in grille[i]:
            if v != 0:
                ligne.append(v)
        ligne.reverse()

        j = 0
        while j < len(ligne) - 1:
            if ligne[j] == ligne[j + 1]:
                ligne[j] = ligne[j] * 2
                score += ligne[j]
                ligne.pop(j + 1)
            j += 1

        while len(ligne) < 4:
            ligne.append(0)
        ligne.reverse()

        if ligne != grille[i]:
            modifie = True
        grille[i] = ligne
    return modifie


def deplacer_haut():
    global score
    modifie = False
    for j in range(4):
        colonne = []
        for i in range(4):
            if grille[i][j] != 0:
                colonne.append(grille[i][j])

        k = 0
        while k < len(colonne) - 1:
            if colonne[k] == colonne[k + 1]:
                colonne[k] = colonne[k] * 2
                score += colonne[k]
                colonne.pop(k + 1)
            k += 1

        while len(colonne) < 4:
            colonne.append(0)

        for i in range(4):
            if grille[i][j] != colonne[i]:
                modifie = True
            grille[i][j] = colonne[i]
    return modifie


def deplacer_bas():
    global score
    modifie = False
    for j in range(4):
        colonne = []
        for i in range(4):
            if grille[i][j] != 0:
                colonne.append(grille[i][j])
        colonne.reverse()

        k = 0
        while k < len(colonne) - 1:
            if colonne[k] == colonne[k + 1]:
                colonne[k] = colonne[k] * 2
                score += colonne[k]
                colonne.pop(k + 1)
            k += 1

        while len(colonne) < 4:
            colonne.append(0)
        colonne.reverse()

        for i in range(4):
            if grille[i][j] != colonne[i]:
                modifie = True
            grille[i][j] = colonne[i]
    return modifie


def partie_terminee():
    # s'il reste des cases vides c'est pas fini
    if len(cases_vides()) > 0:
        return False
    # on verifie si une fusion est encore possible
    for i in range(4):
        for j in range(4):
            if j + 1 < 4 and grille[i][j] == grille[i][j + 1]:
                return False
            if i + 1 < 4 and grille[i][j] == grille[i + 1][j]:
                return False
    return True


# ---- fonctions de l'interface ----

def afficher_grille():
    for i in range(4):
        for j in range(4):
            val = grille[i][j]
            if val == 0:
                texte = ""
                bg = couleurs[0]
            else:
                texte = str(val)
                if val in couleurs:
                    bg = couleurs[val]
                else:
                    bg = "#3c3239"

            # taille de police selon la valeur
            if val < 100:
                taille = 28
            elif val < 1000:
                taille = 22
            else:
                taille = 16

            labels[i][j].config(text=texte, bg=bg,
                                 font=("Arial", taille, "bold"))

    label_score.config(text="Score : " + str(score))


def bouton_play():
    global score, en_jeu
    # on remet tout a zero
    for i in range(4):
        for j in range(4):
            grille[i][j] = 0
    score = 0
    en_jeu = True
    ajouter_tuile()
    ajouter_tuile()
    afficher_grille()


def jouer(direction):
    global en_jeu
    if not en_jeu:
        messagebox.showinfo("2048", "Cliquez sur Play pour commencer !")         # showinfo : internet
        return
    modifie = direction()
    if modifie:
        ajouter_tuile()
        afficher_grille()
        if partie_terminee():
            en_jeu = False
            messagebox.showinfo("2048", "Partie terminee ! Score : " + str(score))


def bouton_save():
    if not en_jeu:
        messagebox.showwarning("2048", "Aucune partie en cours.")
        return
    chemin = filedialog.asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Fichier texte", "*.txt")])
    if chemin:
        fichier = open(chemin, "w")
        fichier.write("score:" + str(score) + "\n")
        for i in range(4):
            ligne_txt = ""
            for j in range(4):
                ligne_txt += str(grille[i][j])
                if j < 3:
                    ligne_txt += " "
            fichier.write(ligne_txt + "\n")
        fichier.close()
        messagebox.showinfo("2048", "Partie sauvegardee !")


def bouton_load():
    global score, en_jeu
    chemin = filedialog.askopenfilename(filetypes=[("Fichier texte", "*.txt")])
    if chemin:
        fichier = open(chemin, "r")
        lignes = fichier.readlines()
        fichier.close()
        score = int(lignes[0].strip().replace("score:", ""))
        for i in range(4):
            valeurs = lignes[i + 1].strip().split(" ")
            for j in range(4):
                grille[i][j] = int(valeurs[j])
        en_jeu = True
        afficher_grille()
        messagebox.showinfo("2048", "Partie chargee !")


def bouton_exit():
    total = 0
    for i in range(4):
        for j in range(4):
            total += grille[i][j]
    messagebox.showinfo("2048", "Score final (somme des tuiles) : " + str(total))
    # on remet la grille a zero
    for i in range(4):
        for j in range(4):
            grille[i][j] = 0
    afficher_grille()


# ---- creation de la fenetre ---- > marcel

fenetre = tk.Tk()
fenetre.title("2048")
fenetre.configure(bg="#e993e5")           # #e993e5: internet 
fenetre.resizable(False, False)           #  e993e5 : internet  

tk.Label(fenetre, text="2048", font=("Arial", 40, "bold"),         # bold : internet 
         bg="#e993e5", fg="#070105").pack(pady=10)                 # 070105  et .pack(pady=10): internet 
 
label_score = tk.Label(fenetre, text="Score : 0", font=("Arial", 16),
                       bg="#e993e5", fg="#070105")
label_score.pack()  

# cadre de la grille
cadre_grille = tk.Frame(fenetre, bg="#A83EA8", padx=8, pady=8)
cadre_grille.pack(padx=20, pady=10)

# creation des labels (cases)
labels = []
for i in range(4): #Boucle sur les lignes
    ligne_labels = []  # Liste temporaire pour une ligne
    for j in range(4):
        l = tk.Label(cadre_grille, text="", width=4, height=2,
                     bg=couleurs[0], font=("Arial", 28, "bold")
                     relief="flat")                     #relief ,supprime les bordures (style plat) : internet 
        l.grid(row=i, column=j, padx=6, pady=6)         # grid : position dans la grille  sert à organiser le tableau : verifier sur internet 
        ligne_labels.append(l)                          # Ajoute la case dans la ligne
    labels.append(ligne_labels)                         #Ajoute la ligne dans la grille

# boutons de direction , inspirer d'un article sur internet 
cadre_dir = tk.Frame(fenetre, bg="#e993e5")  
cadre_dir.pack()   

tk.Button(cadre_dir, text="↑", width=4, font=("Arial", 14, "bold"),
          bg="#7d0b5b", fg="white",
          command=lambda: jouer(deplacer_haut)).grid(row=0, column=1, padx=4, pady=4)
tk.Button(cadre_dir, text="←", width=4, font=("Arial", 14, "bold"),
          bg="#7d0b5b", fg="white",
          command=lambda: jouer(deplacer_gauche)).grid(row=1, column=0, padx=4, pady=4)
tk.Button(cadre_dir, text="↓", width=4, font=("Arial", 14, "bold"),
          bg="#7d0b5b", fg="white",
          command=lambda: jouer(deplacer_bas)).grid(row=1, column=1, padx=4, pady=4)
tk.Button(cadre_dir, text="→", width=4, font=("Arial", 14, "bold"),
          bg="#7d0b5b", fg="white",
          command=lambda: jouer(deplacer_droite)).grid(row=1, column=2, padx=4, pady=4)

# boutons de controle
cadre_ctrl = tk.Frame(fenetre, bg="#e993e5")              # frame : internet
cadre_ctrl.pack(pady=12)

tk.Button(cadre_ctrl, text="🌸Play", width=7, font=("Arial", 12, "bold"),
          bg="#f63ba8", fg="white", command=bouton_play).grid(row=0, column=0, padx=5)
tk.Button(cadre_ctrl, text="🐚Save", width=7, font=("Arial", 12, "bold"),
          bg="#f63ba8", fg="white", command=bouton_save).grid(row=0, column=1, padx=5)
tk.Button(cadre_ctrl, text="🌊Load", width=7, font=("Arial", 12, "bold"),
          bg="#f63ba8", fg="white", command=bouton_load).grid(row=0, column=2, padx=5)
tk.Button(cadre_ctrl, text="🐠Exit", width=7, font=("Arial", 12, "bold"),
          bg="#f63ba8", fg="white", command=bouton_exit).grid(row=0, column=3, padx=5)      

# touches du clavier
fenetre.bind("<Left>",  lambda e: jouer(deplacer_gauche))     
fenetre.bind("<Right>", lambda e: jouer(deplacer_droite))
fenetre.bind("<Up>",    lambda e: jouer(deplacer_haut))
fenetre.bind("<Down>",  lambda e: jouer(deplacer_bas))

fenetre.mainloop()                                        #  mainloop : internet
