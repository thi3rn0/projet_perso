from code_source.business.components.creation_listes import RecupElements


"""l'idée sera de récupérer tous les modules de la bdd à partir de la couche business (et non data),
 puis via une autre méthode, afficher les modules concernés par les choix de classe et matiere via le formulaire """

class ModuleModel:

    def __init__(self):
        self._recup_elements = RecupElements()


    def get_modules(self, nom_classe, nom_matiere):
        modules = [self._recup_elements.modules_classe_matiere(nom_classe,nom_matiere)]
        return modules

