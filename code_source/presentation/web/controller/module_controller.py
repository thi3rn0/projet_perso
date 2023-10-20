from code_source.presentation.web.view.module_view import ModuleView
from code_source.presentation.web.model.module_model import ModuleModel


class ModuleController:

    def __init__(self):

        self._view = ModuleView()
        self._model = None

    def trier_modules(self, choix_classe: int, choix_matiere: int) -> str:
        self._model = ModuleModel()
        self._view.classe = choix_classe
        self._view.matiere = choix_matiere
        self._view._tableau_modules = self._model.get_modules(choix_classe, choix_matiere)

        return self._view.render()


    #
    # def testHTTP(self):
    #     return "Ca marche"