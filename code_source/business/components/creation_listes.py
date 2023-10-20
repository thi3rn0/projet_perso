from code_source.data.data_access import DataAccess
from code_source.presentation.choix_user import Choix


# from code_source.business.entities.classe import Classe

class RecupElements:
    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        self._data = DataAccess()
        self._choix_classe = Choix()
        self._choix_matiere = Choix()
        self._choix_module = Choix()

    # récupérer liste des classe via la requête sql
    def get_list_classes(self):
        liste_des_classes = self._data.get_classes()
        return liste_des_classes

    def get_list_matieres(self):
        liste_des_matieres = self._data.get_matieres()
        return liste_des_matieres

    def modules(self):
        return self._data.all_modules()


    #récupérer la liste des modules( en fonction des choix matiere et classe ?)
    def get_list_modules(self):
        classe = self._choix_classe.choisir_classe()
        matiere = self._choix_matiere.choisir_matiere()
        liste_des_modules = self._data.get_modules(classe, matiere)
        return liste_des_modules

    def get_list_ressources(self):
        module = self._choix_module.choisir_module()
        liste_des_ressources = self._data.get_ressources(module)
        return liste_des_ressources

    def modules_classe_matiere(self, classe, matiere):
        return self._data.get_modules(classe, matiere)


# elements = RecupElements()
# classe = 1
# matiere = 1
# test = elements.modules_classe_matiere(classe,matiere)
# print(test)
