# Importation
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Fonctions de gestion des clés


def generation_cle_fernet(key_path: str = None) -> bytes:
    key = Fernet.generate_key()
    if key_path:
        with open(key_path, "wb") as f:
            f.write(key)
    return key


def lecture_cle_fernet(key_path: str) -> bytes:
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Clé introuvable: {key_path}")
    with open(key_path, "rb") as f:
        return f.read()


""" def generation_cle_rsa():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # sauvegarde
    with open("private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("public.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
 """


def generation_cle_rsa():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    return private_key, public_key
