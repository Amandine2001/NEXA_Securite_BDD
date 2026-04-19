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
