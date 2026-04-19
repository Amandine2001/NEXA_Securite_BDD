from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization


def encrypt_file_rsa(input_path, public_key_path):
    # Charger clé publique
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Lire fichier
    with open(input_path, "rb") as file:
        data = file.read()

    # ⚠️ Limite de taille (approximation pour RSA 2048)
    max_size = 190  # dépend du padding

    if len(data) > max_size:
        raise ValueError("Fichier trop volumineux pour RSA seul")

    # Chiffrement RSA
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # Sauvegarde
    with open(input_path + ".rsa.enc", "wb") as file:
        file.write(encrypted_data)


def decrypt_file_rsa(input_path, private_key_path):
    # Charger clé privée
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Lire fichier chiffré
    with open(input_path + ".rsa.enc", "rb") as file:
        encrypted_data = file.read()

    # Déchiffrement
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # Sauvegarde
    with open(input_path + ".rsa.dec", "wb") as file:
        file.write(decrypted_data)
