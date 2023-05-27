# construction de menus d'affichages simples
from code_source.business.entities.user import User
from code_source.business.components.creation_listes import RecupListe


class Afficher:
    def __init__(self):
        self.create_liste = RecupListe()
        self._user = User()

    def afficher_accueil(self):
        """
        description fonction
        :param
        :return
        """
        print(f"bienvenue sur l'appli,{self._user.prenom}")

    def afficher_liste_classes(self):
        """
        description fonction
        :param
        :return
        """
        liste_classes = self.create_liste.get_list_classes()
        print("====================")
        print("Liste des classes")
        print("====================")
        for element in liste_classes:
            print('\t' + str(element[0]) + ") " + element[1])
        print("----------------")

#
    def afficher_liste_matieres(self):
        """
        Affiche la liste des matières issues du resulat de la recherche, avec une formatage
        permettant de présenter l'index
        pour chaque matière à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
        :param self._create_liste
        """
        # affichage permettant de choisir un numéro associé à une matière
        liste_matieres = self.create_liste.get_list_matieres()
        print("====================")
        print("Liste des matieres")
        print("====================")
        for element in liste_matieres:
            print('\t' + str(element[0]) + ") " + element[1])
        print("----------------")



    def afficher_liste_modules(self):
        """
        Affiche la liste des modules issues du resulat de la recherche, avec une formatage permettant de présenter l'index
        pour chaque module à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
        :param: matiere,classe
        :return
        """
        liste_modules = self.create_liste.get_list_modules()
        # affichage permettant de choisir un numéro associé à un module
        print("====================")
        print("Liste des modules")
        print("====================")
        for element in liste_modules:
            print('\t' + str(element[0]) + ") " + element[1])
        print("----------------")

#
    def afficher_ressource(self):
        """
        Affiche la liste des modules issues du resulat de la recherche, avec une formatage permettant de présenter l'index
        pour chaque module à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
        :param: matiere,classe
        :return
        """
        liste_ressources = self.create_liste.get_list_ressources()
        # affichage permettant de choisir un numéro associé à une ressource
        print("====================")
        print("Liste des ressources")
        print("====================")
        for element in liste_ressources:
            print('\t' + str(element[0]) + ") " + element[1])
        print("----------------")