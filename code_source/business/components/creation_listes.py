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

    #récupérer liste des classe via la requête sql
    def get_list_classes(self):
        # data = DataAccess()
        liste_des_classes = self._data.get_classes()
        # affichage_liste_classes = {}
        # num_choix_classes = 1
        # for element in liste_des_classes:
        #     affichage_liste_classes[num_choix_classes] = element[1]
        #     num_choix_classes += 1
        return liste_des_classes


x = RecupListe()
liste = x.get_list_classes()

print(liste[1])


