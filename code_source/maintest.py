import os



print("Initialisation du serveur...")
project_directory = os.getcwd()
print(f"Répertoire du projet = {project_directory}")
command = f"uvicorn --app-dir={project_directory} testapi:app --reload"
print(f"Lancement de la commande : {command}")
os.system(command)
print("Serveur démarré et à l'écoute.")