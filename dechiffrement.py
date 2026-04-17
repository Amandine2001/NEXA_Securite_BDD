# Importation
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


### Fonction de déchiffrement symetrique
def dechiffrement_symetrique(encrypted_data, key):
    # Génération d'une clé de chiffrement à partir de la clé fournie
    fernet = Fernet(key)

    # Déchiffrement des données
    decrypted_data = fernet.decrypt(encrypted_data).decode()

    return decrypted_data


# Fonction de déchiffrement asymetrique
def dechiffrement_asymetrique(encrypted_data, private_key):

    # Déchiffrement des données avec la clé privée
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    ).decode()

    return decrypted_data
