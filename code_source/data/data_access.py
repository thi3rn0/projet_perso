import psycopg2



HOST = "localhost"
DATABASE = "db_appli"
USER = "dev"
PASSWORD = "dev"
PORT = 5432


# fonction de connection


def connect():
    """
    Fonction qui permet de valider la connexion à la base de données
    """
    global connection
    try:
        # obtention de la connexion à la base de données
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)

        # obtentention d'un curseur, c'est à dire l'objet qui va recueillir les lignes en réponse des requêtes envoyées
        # au serveur de base de données
        cursor = connection.cursor()

        # exécution de la requête
        print('Version du serveur PostgreSQL:')
        cursor.execute('SELECT version()')

        # récupération des valeurs + affichage
        db_version = cursor.fetchone()
        print(db_version)


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Connection à la base de données fermée.')


def get_classes():
    """
    description fonction
    :param
    :return

    """
    # récupérer la requête sql contenant les classes
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_classes = """ SELECT * FROM "CLASSE" """
    cur.execute(sql_classes)
    res = cur.fetchall()
    return res

#créer une liste selon la classe choisie
def get_matieres(classe):
    """
    description fonction
    :param
    :return
    """
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_matieres = f""" SELECT * FROM "MATIERE" """
    cur.execute(sql_matieres)
    res = cur.fetchall()
    return res


def get_modules(matiere, classe):
    """
    description fonction
    :param
    :return
    """
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_modules = f""" select "MODULE".id_module,nom_module from "MODULE" join "MODULE_CLASSE" on "MODULE_CLASSE".id_module = "MODULE".id_module join "CLASSE" ON "CLASSE".id_classe = "MODULE_CLASSE".id_classe where id_matiere={matiere} and "CLASSE".id_classe={classe}; """
    cur.execute(sql_modules)
    res = cur.fetchall()
    return res

def get_ressources(module):
    """
    description fonction
    :param
    :return
    """
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_ressources = f""" SELECT "RESSOURCE".id_module, ressource FROM "RESSOURCE" WHERE id_module={module}"""
    cur.execute(sql_ressources)
    res = cur.fetchall()
    return res

