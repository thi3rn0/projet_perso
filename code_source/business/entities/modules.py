from code_source.business.entities.classe import Classe
from code_source.business.entities.matiere import Matiere


class Module:

# ------------------------------
# constructeur
# ------------------------------
    def __int__(self):
        self.nom = "nom_module"
        self.matiere = Matiere()
        self.classe = Classe()

# ------------------------------
# propriétés
# ------------------------------
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def matiere(self):
        return self._matiere

    @matiere.setter
    def matiere(self, value):
        self._matiere = value

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value

# ------------------------------
# méthodes
# ------------------------------

