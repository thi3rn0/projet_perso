from code_source.presentation.web.view.module_view import *
from code_source.presentation.web.model.module_model import ModuleModel

class ModuleBulmaController:
    def __init__(self):
        self._bulma_view = None
        self._bulma_model = None

    def sort_modules(self, choix_classe: int, choix_matiere: int):
        self._model = ModuleModel()
        self._bulma_view.classe = choix_classe
        self._bulma_view.matiere = choix_matiere
        self._bulma_view._tableau_modules = self._model.get_modules(choix_classe, choix_matiere)

    pass
