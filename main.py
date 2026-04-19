# Importation des librairies et modules
import src.chiffrement_symetrique as chiffrement_symetrique
import src.chiffrement_asymetrique as chiffrement_asymetrique
import src.lecture_fichier as lecture_fichier
import src.sauvegarde as sauvegarde
import src.check_format as check_format
import src.gestion_cle as gestion_cle
import src.lecture_configuration as lecture_configuration
import os

# -------- FONCTION PRINCIPALE --------


def main(chemin_fichier, dossier_local="sauvegarde_1", dossier_cloud="sauvegarde_2"):

    format_fichier = check_format.check_format_doc(chemin_fichier)
    print(f"\n Format de fichier détecté : {format_fichier}")

    match format_fichier:
        case "xlsx":
            data = lecture_fichier.lecture_fichier_xlsx(chemin_fichier)
        case "csv":
            data = lecture_fichier.lecture_fichier_csv(chemin_fichier)
        case "txt":
            data = lecture_fichier.lecture_fichier_txt(chemin_fichier)
        case _:
            raise ValueError("Format de fichier non supporté.")

    print(f"\n Données lues : \n {data}")

    print("\n--- Chiffrement symétrique ---")

    gestion_cle.generation_cle_fernet("cle_symetrique.key")
    key = gestion_cle.lecture_cle_fernet("cle_symetrique.key")
    print(f"Clé symétrique : {key}")

    fichier_crypte = chiffrement_symetrique.chiffrement_symetrique(chemin_fichier, key)
    print(f"Fichier chiffré : {fichier_crypte}")

    fichier_decrypter = chiffrement_symetrique.dechiffrement_symetrique(
        fichier_crypte, key
    )
    print(f"Fichier déchiffré : {fichier_decrypter}")

    print("\n--- Chiffrement asymétrique ---")

    private_key, public_key = gestion_cle.generation_cle_rsa()
    print(f"Clé publique : {public_key}")
    print(f"Clé privée : {private_key}")

    if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
        print("Génération des clés RSA...")
        gestion_cle.generation_cle_rsa()

    chiffrement_asymetrique.encrypt_file_hybrid(chemin_fichier, "public.pem")
    print(f"Fichier chiffré : {chemin_fichier}.enc")
    print(f"Clé chiffrée : {chemin_fichier}.key.enc")

    chiffrement_asymetrique.decrypt_file_hybrid(chemin_fichier, "private.pem")
    fichier_dechiffre = chemin_fichier + ".dec"
    print(f"Fichier déchiffré : {fichier_dechiffre}")

    print("\n--- Sauvegarde du document chiffré ---")
    sauvegarde.sauvegarde_fichier(fichier_crypte, dossier_local, dossier_cloud)


if __name__ == "__main__":
    config = lecture_configuration.lire_configuration("config.properties")

    fichier = config["NOM_FICHIER_A_CHIFFRE"]
    dossier_sauvegarde_1 = config["NOM_DOSSIER_SAUVEGARDE_LOCALE"]
    dossier_sauvegarde_2 = config["NOM_DOSSIER_SAUVEGARDE_CLOUD"]

    print("---- Configuration chargée : ----")
    print(f"Fichier : {fichier}")
    print(f"Dossier local : {dossier_sauvegarde_1}")
    print(f"Dossier cloud : {dossier_sauvegarde_2}")

    main(
        chemin_fichier=fichier,
        dossier_local=dossier_sauvegarde_1,
        dossier_cloud=dossier_sauvegarde_2,
    )
