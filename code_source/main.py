from code_source.presentation.affichage import Afficher
from code_source.presentation.choix_user import Choix
# from code_source.business.entities.user import User

if __name__ == '__main__':
    #création des objets nécessaires à l'utilisation des méthodes
    obj_affichage = Afficher()
    obj_choix = Choix()

    #création de l'utilisateur

    #affichage et choix des classes
    obj_affichage.afficher_liste_classes()
    obj_choix.choisir_classe()


    #affichage et choix de matière
    obj_affichage.afficher_liste_matieres()
    obj_choix.choisir_matiere()

    #affichage et choix modules
    obj_affichage.afficher_liste_modules()
    obj_choix.choisir_module()

    #affichage et choix des ressources
    obj_affichage.afficher_ressource()