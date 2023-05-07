from code_source.business.entities.classe import Classe
from code_source.business.entities.matiere import Matiere
from code_source.business.entities.modules import Module

class Ressource:
# ------------------------------
# constructeur
# ------------------------------
    def __init__(self):
        self.ressource = "ressource"
        self.module = Module()
        self.matiere = Matiere()
        self.classe = Classe()
# ------------------------------
# propriétés
# ------------------------------
    @property
    def ressource(self):
        return self._ressource

    @ressource.setter
    def ressource(self, value):
        self._ressource = value
# ------------------------------
# méthodes
# ------------------------------

    #récupérer la ressource selon les critères de classe, matière, module
    def get_ressources(self):
        pass
