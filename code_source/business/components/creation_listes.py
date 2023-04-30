from code_source.data.data_access import DataAccess
from code_source.business.entities.classe import Classe

class RecupListe:
# ------------------------------
# constructeur
# ------------------------------
    def __int__(self):
        self._data_access = DataAccess()
        self.classe = Classe()


# ------------------------------
# propriétés
# ------------------------------
    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value

# ------------------------------
# méthodes
# ------------------------------

    #récupérer liste des classe via la requête sql
    def get_list_classes(self):
        liste_des_classes = DataAccess.get_classes(self)
        affichage_liste_classes = {}
        num_choix_classes = 1
        for element in liste_des_classes:
            affichage_liste_classes[num_choix_classes] = element[1]
            num_choix_classes += 1


    # récupérer liste des matières selon la classe
    def get_matiere(self):
        pass


    #récupérer liste des modules selon matière et classe
    def get_module(self):
        pass



if __name__ == '__main__':
    cp = DataAccess()
    liste_classe = RecupListe.get_list_classes(cp)