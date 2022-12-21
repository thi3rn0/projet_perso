from affichage import *
from data_access import *


nom_enfant = input("Entre ton nom: ")
afficher_accueil(nom_enfant)

liste_des_classes = afficher_liste_classes()
choix_classe = int(input("choisis ta classe: "))

#choix de la classe
if choix_classe == 1:
     liste_des_matieres_cp = afficher_liste_matieres_cp()
     #choix de la matière
     choix_matiere_cp = int(input("choisis ta matière: "))
     if choix_matiere_cp == 1:
          modules_maths_cp = afficher_modules_maths_cp()
          # choix du module
          choix_module_maths_cp = int(input("Choisis le module: "))
          if choix_module_maths_cp == 1:
               pass

     else:
          pass
else:
     pass

