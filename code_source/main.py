from code_source.presentation.affichage import *
from code_source.business.entities.user import User

if __name__ == '__main__':

    nom_enfant = str(input("Entre ton nom: "))
    afficher_accueil(nom_enfant)

    while True:
        try:
            #choix de la classe
            liste_des_classes = afficher_liste_classes()
            choix_classe = int(input("choisis ta classe: "))
        except ValueError:
            print("Merci d'entrer un entier parmi la liste :) ")
            continue
        print("----------------")
        while True:
            try:
                # choix de la matière
                liste_des_matieres = afficher_liste_matieres(choix_classe)
                choix_matiere = int(input("Choisis la matiere: "))
            except ValueError:
                print("Merci d'entrer un entier parmi la liste :) ")
                continue
            print("----------------")
            while True:
                try:
                    #choix du module en fonction de la matière
                    liste_modules = afficher_modules(choix_matiere, choix_classe)
                    choix_module = int(input("Choisis le module que tu souhaites aborder: "))
                except ValueError:
                    print("Merci d'entrer un entier parmi la liste :) ")
                    continue
                print("----------------")
                while True:
                    try:
                        #choix de la ressource en fonction du module
                        liste_ressource = afficher_ressource(choix_module)
                        choix_ressource = int(input("Choisis ta ressource: "))
                    except ValueError:
                        print("Merci de sélectionner un nombre parmi la liste !")


