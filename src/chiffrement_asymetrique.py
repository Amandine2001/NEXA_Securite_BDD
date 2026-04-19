# Importation

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# Fonctions de chiffrement hybride (RSA + Fernet)


def encrypt_file_hybrid(input_path, public_key_path):
    # 1. clé symétrique
    sym_key = Fernet.generate_key()
    f = Fernet(sym_key)

    # 2. chiffrer fichier
    with open(input_path, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(input_path + ".enc", "wb") as file:
        file.write(encrypted_data)

    # 3. chiffrer la clé avec RSA
    with open(public_key_path, "rb") as fkey:
        public_key = serialization.load_pem_public_key(fkey.read())

    encrypted_key = public_key.encrypt(
        sym_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    with open(input_path + ".key.enc", "wb") as file:
        file.write(encrypted_key)


def decrypt_file_hybrid(input_path, private_key_path):
    # 1. charger clé privée
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # 2. récupérer clé symétrique
    with open(input_path + ".key.enc", "rb") as f:
        encrypted_key = f.read()

    sym_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # 3. déchiffrer fichier
    f = Fernet(sym_key)

    with open(input_path + ".enc", "rb") as file:
        encrypted_data = file.read()

    decrypted = f.decrypt(encrypted_data)

    with open(input_path + ".dec", "wb") as file:
        file.write(decrypted)


""" from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import os


def encrypt_file_hybrid(input_path, public_key_path):
    # 1. clé symétrique
    sym_key = Fernet.generate_key()
    f = Fernet(sym_key)

    # 2. lire fichier
    with open(input_path, "rb") as file:
        data = file.read()

    # 3. chiffrer données
    encrypted_data = f.encrypt(data)

    # 4. sauvegarde fichier chiffré
    encrypted_file_path = input_path + ".enc"
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)

    # 5. charger clé publique RSA
    with open(public_key_path, "rb") as fkey:
        public_key = serialization.load_pem_public_key(fkey.read())

    # 6. chiffrer clé AES
    encrypted_key = public_key.encrypt(
        sym_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # 7. sauvegarde clé (plus propre)
    key_path = os.path.splitext(input_path)[0] + ".key"

    with open(key_path, "wb") as file:
        file.write(encrypted_key)

    print(f"✅ Fichier chiffré : {encrypted_file_path}")
    print(f"🔑 Clé chiffrée : {key_path}")

def decrypt_file_hybrid(encrypted_path, private_key_path):
    # ex: encrypted_path = "data.csv.enc"

    # 1. retrouver nom original
    original_path = encrypted_path.replace(".enc", "")

    # 2. retrouver fichier clé
    key_path = os.path.splitext(original_path)[0] + ".key"

    # 3. charger clé privée RSA
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # 4. récupérer clé AES
    with open(key_path, "rb") as f:
        encrypted_key = f.read()

    sym_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # 5. déchiffrer fichier
    f = Fernet(sym_key)

    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()

    decrypted = f.decrypt(encrypted_data)

    # 6. sauvegarde avec BONNE extension
    with open(original_path, "wb") as file:
        file.write(decrypted)

    print(f"✅ Fichier restauré : {original_path}") """
