# Importation
import os
from cryptography.fernet import Fernet


# Fonctions de gestion des clés


def generation_cle(key_path: str = None) -> bytes:
    key = Fernet.generate_key()

    if key_path:
        with open(key_path, "wb") as f:
            f.write(key)

    return key


def lecture_cle(key_path: str) -> bytes:
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Clé introuvable: {key_path}")

    with open(key_path, "rb") as f:
        return f.read()
