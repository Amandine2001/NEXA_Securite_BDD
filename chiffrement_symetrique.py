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


def chiffrement_symetrique(input_path: str, key: bytes, output_path: str = None) -> str:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Fichier introuvable: {input_path}")

    if output_path is None:
        output_path = input_path + ".enc"

    fernet = Fernet(key)

    with open(input_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(output_path, "wb") as f:
        f.write(encrypted)

    return output_path


def dechiffrement_symetrique(
    input_path: str, key: bytes, output_path: str = None
) -> str:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Fichier introuvable: {input_path}")

    if output_path is None:
        if input_path.endswith(".enc"):
            output_path = input_path[:-4]
        else:
            output_path = input_path + ".dec"

    fernet = Fernet(key)

    with open(input_path, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted = fernet.decrypt(encrypted_data)
    except Exception:
        raise ValueError("Échec du déchiffrement (clé incorrecte ou fichier corrompu)")

    with open(output_path, "wb") as f:
        f.write(decrypted)

    return output_path
