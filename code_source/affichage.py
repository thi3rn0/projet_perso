#construction de menus d'affichages simples
from data_access import *

def afficher_accueil(nom):
    print("bienvenue sur l'appli",nom)

def afficher_liste_classes():
    liste_des_classes = creer_liste_classes()
    affichage_liste_classes = {}
    num_choix_classes = 1
    for element in liste_des_classes:
        affichage_liste_classes[num_choix_classes] = element[1]
        num_choix_classes += 1
    # affichage permettant de choisir un numéro associé à une classe
    print("liste des classes: ")
    for affichage_classe in affichage_liste_classes.items():
        print('\t' + str(affichage_classe[0]) + ") " + affichage_classe[1])

def afficher_liste_matieres_cp():
    liste_des_matieres = creer_liste_matieres_cp()
    affichage_liste_matieres = {}
    num_choix_matieres = 1
    for element in liste_des_matieres:
        affichage_liste_matieres[num_choix_matieres] = element[1]
        num_choix_matieres +=1
    # affichage permettant de choisir un numéro associé à une matière
    for matiere in affichage_liste_matieres.items():
        print('\t' + str(matiere[0]) + ") " + matiere[1])


def afficher_modules_maths_cp():
    liste_modules_maths_cp = creer_liste_modules_maths_cp()
    affichage_modules_maths_cp = {}
    num_choix_modules_maths_cp = 1
    for element in liste_modules_maths_cp:
        affichage_modules_maths_cp[num_choix_modules_maths_cp] = element[1]
        num_choix_modules_maths_cp +=1
    # affichage permettant de choisir un numéro associé à une matière
    for module in affichage_modules_maths_cp.items():
        print('\t' + str(module[0]) + ") " + module[1])

def affichage_conseil_maths_cp():
    pass

def affichage_ressource_maths_cp():
    pass