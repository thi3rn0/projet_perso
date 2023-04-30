from code_source.business.entities.classe import Classe


class Matiere:

# ------------------------------
# constructeur
# ------------------------------
    def __int__(self):
        self.nom = "nom_matiere"
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
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value