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
    print("----------------")

def afficher_liste_matieres(classe):
    """
    Affiche la liste des matières issues du resulat de la recherche, avec une formatage permettant de présenter l'index
    pour chaque matière à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix    :param
    :param classe
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
    print("----------------")

def afficher_modules(matiere, classe):
    """
    Affiche la liste des modules issues du resulat de la recherche, avec une formatage permettant de présenter l'index
    pour chaque module à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
    :param: matiere,classe
    :return
    """
    liste_modules = get_modules(matiere, classe)
    affichage_modules = {}
    num_choix_modules = 1
    for element in liste_modules:
        affichage_modules[num_choix_modules] = element[1]
        num_choix_modules += 1
    # affichage permettant de choisir un numéro associé à un module
    print("Liste des modules: ")
    for module in affichage_modules.items():
        print('\t' + str(module[0]) + ") " + module[1])
    print("----------------")

def afficher_ressource(module):
    """
    Affiche la liste des ressources issues du resulat de la recherche, avec une formatage permettant de présenter l'index
    pour chaque ressource à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
    :param module:
    """
    liste_ressources = get_ressources(module)
    affichage_ressource = {}
    num_choix_ressource = 1
    for element in liste_ressources:
        affichage_ressource[num_choix_ressource] = element[1]
        num_choix_ressource += 1
    # affichage permettant de choisir un numéro associé à une ressource
    print("Ressource(s) proposé(es): ")
    for ressource in affichage_ressource.items():
        print('\t' + str(ressource[0]) + ") " + str(ressource[1]))
    print("----------------")