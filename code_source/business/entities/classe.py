#classe permettant de récupérer la classe à partir de la bdd


class Classe:
# ------------------------------
# constructeur
# ------------------------------
    def __int__(self):
        self.nom = "nom_classe"

# ------------------------------
# propriétés
# ------------------------------
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value
