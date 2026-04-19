# Importation

from cryptography.fernet import Fernet
import os


# Fonctions de chiffrement symétrique

""" def chiffrement_symetrique(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def dechiffrement_symetrique(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data """


def chiffrement_symetrique(
    chemin_fichier_entree: str, key: bytes, chemin_fichier_sortie: str = None
) -> str:
    if not os.path.exists(chemin_fichier_entree):
        raise FileNotFoundError(f"Fichier introuvable: {chemin_fichier_entree}")

    if chemin_fichier_sortie is None:
        chemin_fichier_sortie = chemin_fichier_entree + ".enc"

    fernet = Fernet(key)

    with open(chemin_fichier_entree, "rb") as f:
        data = f.read()

    crypte = fernet.encrypt(data)

    with open(chemin_fichier_sortie, "wb") as f:
        f.write(crypte)

    return chemin_fichier_sortie


def dechiffrement_symetrique(
    chemin_fichier_entree: str, key: bytes, chemin_fichier_sortie: str = None
) -> str:
    if not os.path.exists(chemin_fichier_entree):
        raise FileNotFoundError(f"Fichier introuvable: {chemin_fichier_entree}")

    if chemin_fichier_sortie is None:
        if chemin_fichier_entree.endswith(".enc"):
            chemin_fichier_sortie = chemin_fichier_entree[:-4]
        else:
            chemin_fichier_sortie = chemin_fichier_entree + ".dec"

    fernet = Fernet(key)

    with open(chemin_fichier_entree, "rb") as f:
        crypte_data = f.read()

    try:
        decrypte = fernet.decrypt(crypte_data)
    except Exception:
        raise ValueError("Échec du déchiffrement (clé incorrecte ou fichier corrompu)")

    with open(chemin_fichier_sortie, "wb") as f:
        f.write(decrypte)

    return chemin_fichier_sortie
