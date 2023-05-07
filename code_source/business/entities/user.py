from code_source.business.entities.classe import Classe


class User:

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):
        self.nom = "username"
        self.prenom = "user_lastname"
        self.age = 0
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
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value
    # ------------------------------
    # méthodes
    # ------------------------------

