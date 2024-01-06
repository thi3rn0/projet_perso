"""
ici on implémentera la mise en page des "cartes" qui contiendront les modules à afficher
"""
from code_source.presentation.web.view.iview import IView


class ModuleBulmaView(IView):
    def __init__(self):
        self._choix_classe = 0
        self._choix_matiere = 0
        self._liste_modules = []

    @property
    def choix_classe(self):
        return self._choix_classe

    @choix_classe.setter
    def choix_classe(self, value):
        self._choix_classe = value

    @property
    def choix_matiere(self):
        return self._choix_matiere

    @choix_matiere.setter
    def choix_matiere(self, value):
        self._choix_matiere = value

    @property
    def liste_modules(self):
        return self._liste_modules

    @liste_modules.setter
    def liste_modules(self, value):
        self._liste_modules = value

    def _build_module_tile(self):
        pass

    #méthode qui permettra de créer la page contenant les tuiles
    def render(self) -> str:
        pass
    pass