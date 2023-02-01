# construction de menus d'affichages simples
from code_source.data.data_access import *


def afficher_accueil(nom):
    """
    description fonction
    :param
    :return
    """
    print("bienvenue sur l'appli", nom)


def afficher_liste_classes():
    """
    description fonction
    :param
    :return
    """
    liste_des_classes = get_classes()
    affichage_liste_classes = {}
    num_choix_classes = 1
    for element in liste_des_classes:
        affichage_liste_classes[num_choix_classes] = element[1]
        num_choix_classes += 1
    # affichage permettant de choisir un numéro associé à une classe
    print("liste des classes: ")
    for affichage_classe in affichage_liste_classes.items():
        print('\t' + str(affichage_classe[0]) + ") " + affichage_classe[1])


def afficher_liste_matieres(classe):
    """
    description fonction
    :param
    :return
    """
    liste_des_matieres = get_matieres(classe)
    affichage_liste_matieres = {}
    num_choix_matieres = 1
    for element in liste_des_matieres:
        affichage_liste_matieres[num_choix_matieres] = element[1]
        num_choix_matieres += 1
    # affichage permettant de choisir un numéro associé à une matière
    print("Liste des matières: ")
    for matiere in affichage_liste_matieres.items():
        print('\t' + str(matiere[0]) + ") " + matiere[1])


def afficher_modules(matiere):
    """
    description fonction
    :param
    :return
    """
    liste_modules = get_modules(matiere)
    affichage_modules = {}
    num_choix_modules = 1
    for element in liste_modules:
        affichage_modules[num_choix_modules] = element[1]
        num_choix_modules += 1
    # affichage permettant de choisir un numéro associé à un module
    print("Liste des modules: ")
    for module in affichage_modules.items():
        print('\t' + str(module[0]) + ") " + module[1])


def afficher_ressource(module):
    liste_ressources = get_ressources(module)
    affichage_ressource = {}
    num_choix_ressource = 1
    for element in liste_ressources:
        affichage_ressource[num_choix_ressource] = element[3]
        num_choix_ressource += 1
    # affichage permettant de choisir un numéro associé à une ressource
    print("Ressource(s) proposé(es): ")
    for ressource in affichage_ressource.items():
        print('\t' + str(ressource[0]) + ") " + ressource[1])
