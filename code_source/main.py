from code_source.presentation.affichage import *

nom_enfant = str(input("Entre ton nom: "))
afficher_accueil(nom_enfant)


#choix de la classe
liste_des_classes = afficher_liste_classes()
choix_classe = int(input("choisis ta classe: "))

# choix de la matière
liste_des_matieres = afficher_liste_matieres(choix_classe)
choix_matiere = int(input("Choisis la matiere: "))

#choix du module en fonction de la matière
liste_modules = afficher_modules(choix_matiere)
choix_module = int(input("Choisis le module que tu souhaites aborder: "))

liste_ressource = afficher_ressource(choix_module)
choix_ressource = int(input("Ressources: "))
# if choix_classe == 1:
#     try:
#         choix_matiere_cp = int(input("choisis ta matière: "))
#
#         if choix_matiere_cp == 1:
#             modules_maths_cp = afficher_modules_maths_cp()
#             choix_module_maths_cp = int(input("Choisis le module: "))
#             # affichage du conseil et de la ressource selon le module choisi
#             affichage_conseil_maths_cp(choix_module_maths_cp)
#
#         else:
#             pass
#     except ValueError:
#         print("Merci de choisir un nombre parmi la liste.")
# else:
#     pass
