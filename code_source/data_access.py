import psycopg2

HOST = "localhost"
DATABASE = "db_appli"
USER = "dev_apprentissage"
PASSWORD = "dev"
PORT = 5432
#fonction de connection


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


def creer_liste_classes():
    # récupérer la requête sql contenant les classes
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_classes = """ SELECT * FROM "CLASSES" """
    cur.execute(sql_classes)
    res = cur.fetchall()
    return res

def creer_liste_matieres_cp():
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_matieres_cp = """ SELECT * FROM "MATIERES_CP" """
    cur.execute(sql_matieres_cp)
    res = cur.fetchall()
    return res


def creer_liste_modules_maths_cp():
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_maths_cp = """ SELECT * FROM "MODULES_MATHS_CP" """
    cur.execute(sql_maths_cp)
    res = cur.fetchall()
    return res

def creer_liste_conseils_maths_cp():
    connexion = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
    cur = connexion.cursor()
    sql_maths_cp = """ SELECT * FROM "MODULES_MATHS_CP" """
    cur.execute(sql_maths_cp)
    res = cur.fetchall()
    return res