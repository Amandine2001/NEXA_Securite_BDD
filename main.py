# Importation des librairies et modules
import chiffrement
import sauvegarde
import check_format

# Vérification du format du document

""" def lecture_configuration():
    config = {}
    with open('config.properties', 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config
 """


def main():
    """config = lecture_configuration()
    chemin_fichier = config.get('NOM_FICHIER')"""

    chemin_fichier = "data/boursobank.csv"

    format_fichier = check_format.check_format_doc(chemin_fichier)
    print(f"Format de fichier détecté : {format_fichier}")


if __name__ == "__main__":
    main()
