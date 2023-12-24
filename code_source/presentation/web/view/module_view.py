from code_source.presentation.web.view.htmlbuilder import *
from code_source.presentation.web.view.iview import *

class ModuleView(IView):

    def __init__(self):
        self._classe = 0
        self._matiere = 0
        self._tableau_modules = ["Comprendre et utiliser des nombres entiers pour dénombrer, ordonner, repérer, comparer ", "Nommer, lire, écrire, représenter des nombres entiers ", "Résoudre des problèmes en utilisant des nombres entiers et le calcul" , "Faits numériques mémorisés utiles pour tous les types de calcul", "Procédure de calcul mental ", "Calcul en ligne", "Calcul posé", "Comparer, estimer, mesurer des longueurs, des masses, des contenances, des durées, tiliser le lexique, les unités, les instruments de mesures spécifiques de ces grandeurs", "Résoudre des problèmes impliquant des longueurs, des masses, des contenances, des durées, des prix", "Se repérer et se déplacer en utilisant des repères et des représentations", "Reconnaître, nommer, décrire, reproduire quelques solides", "Reconnaître, nommer, décrire, reproduire, construire quelques figures géométriques - Reconnaître et utiliser les notions d’alignement, d’angle droit,d’égalité de longueurs, de milieu, de symétrie"]

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value

    @property
    def matiere(self):
        return self._matiere

    @matiere.setter
    def matiere(self, value):
        self._matiere = value

    @property
    def tableau_modules(self):
        return self._tableau_modules

    @tableau_modules.setter
    def tableau_modules(self, value):
        self._tableau_modules = value

    def _build_liste_modules(self):
        tableau = self._tableau_modules
        html_table = "<ul>"
        for item in tableau:
            # html_table += "<tr>"
            # print(item)
            html_table += f"<li>{str(item)}</li>"
            # html_table += "<br>"
            # html_table += "</tr>"
        html_table += "</ul>"
        return html_table

    def render(self) -> str:

        htmlBuilder = HtmlBuilder()
        htmlBuilder.ajouter_html(f"<h1>Classe: {self._classe}; Matière: {self._matiere}</h1>")
        htmlBuilder.ajouter_paragraphe(f"Voici les modules obtenus grâce au pattern MVC implémenté sur l'architecture couteau suisse")
        htmlBuilder.ajouter_html(self._build_liste_modules())
        htmlBuilder.ajouter_paragraphe(f"Le rendu est réalisé côté serveur, par le vue du modèle MVC")

        return htmlBuilder.HTML

t = ModuleView()
c = t._build_liste_modules()

