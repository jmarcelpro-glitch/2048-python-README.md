Groupe BI04

Marcel , prithika, Anya et syrine


EXPLICATION DU PROGRAMME 2048 

1.  OBJECTIF Ce programme implémente le jeu 2048 avec une interface
    graphique Tkinter. Le but est de fusionner les nombres pour
    atteindre 2048.

2.  STRUCTURE GENERALE

Le programme est composé de trois parties principales :

A. LES DONNEES - grille : matrice 4x4 représentant le plateau - score :
nombre de points du joueur - en_jeu : indique si une partie est en cours

B. LA LOGIQUE DU JEU Fonctions principales : - cases_vides() : retourne
les cases libres - ajouter_tuile() : ajoute un 2 ou un 4 aléatoirement -
deplacer_gauche/droite/haut/bas() : gèrent les déplacements -
partie_terminee() : vérifie si le jeu est fini

Principe d’un déplacement : 1. supprimer les zéros 2. fusionner les
valeurs identiques 3. ajouter des zéros 4. mettre à jour le score

C. L’INTERFACE GRAPHIQUE Utilise Tkinter : - fenêtre principale - grille
visuelle (labels) - boutons (direction + contrôle) - affichage du score

3.  DEROULEMENT DU JEU

4.  L’utilisateur clique sur Play → la grille est réinitialisée → deux
    tuiles sont ajoutées

5.  L’utilisateur appuie sur une direction → fonction jouer(direction)

6.  Si le mouvement est valide : → mise à jour de la grille → ajout
    d’une tuile → mise à jour de l’affichage

7.  Vérification de fin de partie → message si terminé

8.  SAUVEGARDE / CHARGEMENT

-   Save : enregistre score + grille dans un fichier texte
-   Load : recharge une partie depuis un fichier

5.  INTERFACE UTILISATEUR

-   Frame : organise les éléments
-   Label : affiche texte et cases
-   Button : permet les actions
-   bind() : associe clavier aux actions



