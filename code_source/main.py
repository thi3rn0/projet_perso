from affichage import *

nom_enfant = input("Entre ton nom: ")
afficher_accueil(nom_enfant)
'\n'
liste_des_classes = afficher_liste_classes()
choix_classe = int(input("choisis ta classe: "))

# choix de la classe
if choix_classe == 1:
    liste_des_matieres_cp = afficher_liste_matieres_cp()
    # choix de la matière
    choix_matiere_cp = int(input("choisis ta matière: "))

    if choix_matiere_cp == 1:
        modules_maths_cp = afficher_modules_maths_cp()
        choix_module_maths_cp = int(input("Choisis le module: "))
        # affichage du conseil et de la ressource selon le module choisi
        affichage_conseil_maths_cp(choix_module_maths_cp)

    else:
        pass
else:
    pass
