# from code_source.business.entities.classe import Classe
# from code_source.business.entities.matiere import Matiere
# from code_source.business.entities.modules import Module
# from code_source.business.entities.ressources import Ressource
from code_source.business.entities.user import User


class Choix:
    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        #self._utilisateur = User
        pass
    # ------------------------------
    # propriétés
    # ------------------------------

    # ------------------------------
    # méthodes
    # ------------------------------

    def choisir_classe(self):
        choix_classe = int(input("Choisis ta classe: "))
        return choix_classe

    def choisir_matiere(self):
        choix_matiere = int(input("Choisis ta matière: "))
        return choix_matiere

    def choisir_module(self):
        choix_module = int(input("Choisis ton module: "))
        return choix_module

    def choisir_ressource(self):
        pass

    pass



