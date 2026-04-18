# Importation des librairies et modules
import chiffrement_symetrique
import chiffrement_asymetrique
import lecture_fichier
import sauvegarde
import check_format
import gestion_cle

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# -------- FONCTION PRINCIPALE --------
def main(chemin_fichier):

    # 1. Vérification du format du document
    format_fichier = check_format.check_format_doc(chemin_fichier)
    print(f"Format de fichier détecté : {format_fichier}")

    # 2. Lecture du document
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

    # 3. Chiffrement du document

    # 3.1. Chiffrement symetrique
    print("\n--- Chiffrement symétrique ---")

    # 3.1.1. Gestion des clés
    gestion_cle.generation_cle("cle_symetrique.key")
    key = gestion_cle.lecture_cle("cle_symetrique.key")
    print(f"Clé symétrique : {key}")

    # 3.1.2. Chiffrement et déchiffrement
    fichier_crypte = chiffrement_symetrique.chiffrement_symetrique(chemin_fichier, key)
    print(f"Fichier chiffré : {fichier_crypte}")

    fichier_decrypter = chiffrement_symetrique.dechiffrement_symetrique(
        fichier_crypte, key
    )
    print(f"Fichier déchiffré : {fichier_decrypter}")

    """ # 3.2. Chiffrement asymetrique
    print("\n--- Chiffrement asymétrique ---")

    # 3.2.1. Génération des clés
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    print(f"Clé publique : {public_key}")
    print(f"Clé privée : {private_key}")

    # 3.2.2. Chiffrement et déchiffrement
    data_str = str(data)
    encrypted_data = chiffrement_asymetrique.chiffrement_asymetrique(data_str, public_key)
    print(f"Données chiffrées : {encrypted_data}")

    decrypted_data = chiffrement_asymetrique.dechiffrement_asymetrique(encrypted_data, private_key)
    print(f"Données déchiffrées : {decrypted_data}") """


if __name__ == "__main__":
    chemin_fichier = "data/Atelier1-RACIO-SNCF.xlsx"
    main(chemin_fichier=chemin_fichier)
