from code_source.data.data_access import DataAccess


# from code_source.business.entities.classe import Classe

class RecupListe:
    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        self._data = DataAccess()
        # self.classe = Classe()

    # ------------------------------
    # propriétés
    # ------------------------------
    #     @property
    #     def classe(self):
    #         return self._classe
    #
    #     @classe.setter
    #     def classe(self, value):
    #         self._classe = value

    # ------------------------------
    # méthodes
    # ------------------------------

    # récupérer liste des classe via la requête sql
    def get_list_classes(self):
        liste_des_classes = self._data.get_classes()
        return liste_des_classes

    def get_list_matieres(self):
        liste_des_matieres = self._data.get_matieres()
        return liste_des_matieres

    #récupérer la liste des modules( en fonction des choix matiere et classe ?)
    def get_list_modules(self):
        liste_des_modules = self._data.get_modules()
        return liste_des_modules

    def get_list_ressources(self):
        liste_des_ressources = self._data.get_ressources()
        return liste_des_ressources