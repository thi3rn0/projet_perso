from code_source.presentation.affichage import Afficher
from code_source.presentation.choix_user import Choix
from code_source.business.components.creation_listes import *
# from code_source.business.entities.user import User

if __name__ == '__main__':
    obj_affichage = Afficher()
    obj_liste = RecupElements()

    obj_affichage.afficher_liste_classes()
    obj_liste.get_list_classes()

    obj_affichage.afficher_liste_matieres()
    obj_liste.get_list_matieres()

    obj_affichage.afficher_liste_modules()
    obj_affichage.afficher_ressource()
