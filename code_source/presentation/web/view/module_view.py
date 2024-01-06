from code_source.presentation.web.view.htmlbuilder import *
from code_source.presentation.web.view.iview import *

class ModuleView(IView):

    def __init__(self):
        self._classe = 0
        self._matiere = 0
        self._tableau_modules = []

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

