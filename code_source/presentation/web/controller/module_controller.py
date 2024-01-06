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
        #self._view._tableau_modules = ["Comprendre et utiliser des nombres entiers pour dénombrer, ordonner, repérer, comparer ", "Nommer, lire, écrire, représenter des nombres entiers ", "Résoudre des problèmes en utilisant des nombres entiers et le calcul" , "Faits numériques mémorisés utiles pour tous les types de calcul", "Procédure de calcul mental ", "Calcul en ligne", "Calcul posé", "Comparer, estimer, mesurer des longueurs, des masses, des contenances, des durées, tiliser le lexique, les unités, les instruments de mesures spécifiques de ces grandeurs", "Résoudre des problèmes impliquant des longueurs, des masses, des contenances, des durées, des prix", "Se repérer et se déplacer en utilisant des repères et des représentations", "Reconnaître, nommer, décrire, reproduire quelques solides", "Reconnaître, nommer, décrire, reproduire, construire quelques figures géométriques - Reconnaître et utiliser les notions d’alignement, d’angle droit,d’égalité de longueurs, de milieu, de symétrie"]


        return self._view.render()


