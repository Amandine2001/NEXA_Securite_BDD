# Importation des librairies et modules
import chiffrement
import lecture_fichier
import sauvegarde
import check_format


def main(chemin_fichier):

    # Vérification du format du document
    format_fichier = check_format.check_format_doc(chemin_fichier)
    print(f"Format de fichier détecté : {format_fichier}")

    # Lecture du document
    match format_fichier:
        case "xlsx":
            data = lecture_fichier.lecture_fichier_xlsx(chemin_fichier)
        case "csv":
            data = lecture_fichier.lecture_fichier_csv(chemin_fichier)
        case "txt":
            data = lecture_fichier.lecture_fichier_txt(chemin_fichier)
        case _:
            raise ValueError("Format de fichier non supporté.")

    print(f"Données lues :{data}")

    # Chiffrement du document

    ## Chiffrement symetrique


if __name__ == "__main__":
    chemin_fichier = "data/text_to_clean.txt"
    main(chemin_fichier=chemin_fichier)
