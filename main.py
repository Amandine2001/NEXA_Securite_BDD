# Importation des librairies et modules
import chiffrement_symetrique
import chiffrement_asymetrique
import lecture_fichier
import sauvegarde
import check_format
import gestion_cle
import os

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
    gestion_cle.generation_cle_fernet("cle_symetrique.key")
    key = gestion_cle.lecture_cle_fernet("cle_symetrique.key")
    print(f"Clé symétrique : {key}")

    # 3.1.2. Chiffrement et déchiffrement
    fichier_crypte = chiffrement_symetrique.chiffrement_symetrique(chemin_fichier, key)
    print(f"Fichier chiffré : {fichier_crypte}")

    fichier_decrypter = chiffrement_symetrique.dechiffrement_symetrique(
        fichier_crypte, key
    )
    print(f"Fichier déchiffré : {fichier_decrypter}")

    # 3.2. Chiffrement asymetrique
    print("\n--- Chiffrement asymétrique ---")

    # 3.2.1. Génération des clés

    private_key, public_key = gestion_cle.generation_cle_rsa()
    print(f"Clé publique : {public_key}")
    print(f"Clé privée : {private_key}")

    # 2. Génération des clés si elles n'existent pas
    if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
        print("Génération des clés RSA...")
        gestion_cle.generation_cle_rsa()

    # 3. Chiffrement du fichier
    print("Chiffrement en cours...")
    chiffrement_asymetrique.encrypt_file_hybrid(chemin_fichier, "public.pem")

    print(f"Fichier chiffré : {chemin_fichier}.enc")
    print(f"Clé chiffrée : {chemin_fichier}.key.enc")

    # 4. Déchiffrement
    print("Déchiffrement en cours...")
    chiffrement_asymetrique.decrypt_file_hybrid(chemin_fichier, "private.pem")

    fichier_dechiffre = chemin_fichier + ".dec"
    print(f"Fichier déchiffré : {fichier_dechiffre}")


if __name__ == "__main__":
    chemin_fichier = "data/text_to_clean.txt"
    main(chemin_fichier=chemin_fichier)
