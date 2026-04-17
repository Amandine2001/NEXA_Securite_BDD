# Importation des librairies et modules
import chiffrement
import lecture_fichier
import sauvegarde
import check_format

from cryptography.fernet import Fernet


# -------- FONCTION PRINCIPALE --------
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

    key = Fernet.generate_key()

    encrypted_data_sym = chiffrement.chiffrement_symetrique(data, key)
    print(f"Données chiffrées (symétrique) : {encrypted_data_sym}")

    decrypted_data_sym = chiffrement.dechiffrement_symetrique(encrypted_data_sym, key)
    print(f"Données déchiffrées (symétrique) : {decrypted_data_sym}")


if __name__ == "__main__":
    chemin_fichier = "data/text_to_clean.txt"
    main(chemin_fichier=chemin_fichier)
