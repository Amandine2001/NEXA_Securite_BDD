# Développement d'une solution de chiffrement de données

## Importation
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


### Fonction de chiffrement symetrique
def chiffrement_symetrique(data, key):
    # Génération d'une clé de chiffrement à partir de la clé fournie
    fernet = Fernet(key)

    # Chiffrement des données
    encrypted_data = fernet.encrypt(data.encode())

    return encrypted_data


### Fonction de déchiffrement symetrique
def dechiffrement_symetrique(encrypted_data, key):
    # Génération d'une clé de chiffrement à partir de la clé fournie
    fernet = Fernet(key)

    # Déchiffrement des données
    decrypted_data = fernet.decrypt(encrypted_data).decode()

    return decrypted_data


### Fonction de chiffrement asymetrique


def chiffrement_asymetrique(data, public_key):

    # Chiffrement des données avec la clé publique
    encrypted_data = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return encrypted_data


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


# Test des fonctions de chiffrement et déchiffrement
if __name__ == "__main__":
    # Génération d'une clé de chiffrement symétrique
    key = Fernet.generate_key()
    data = "Ceci est un message secret."
    # Chiffrement et déchiffrement symétrique
    encrypted_data_sym = chiffrement_symetrique(data, key)
    decrypted_data_sym = dechiffrement_symetrique(encrypted_data_sym, key)
    print("Données chiffrées (symétrique) :", encrypted_data_sym)
    print("Données déchiffrées (symétrique) :", decrypted_data_sym)
    # Génération d'une paire de clés asymétriques
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    # Chiffrement et déchiffrement asymétrique
    encrypted_data_asym = chiffrement_asymetrique(data, public_key)
    decrypted_data_asym = dechiffrement_asymetrique(encrypted_data_asym, private_key)
    print("Données chiffrées (asymétrique) :", encrypted_data_asym)
    print("Données déchiffrées (asymétrique) :", decrypted_data_asym)
