import time
import src.chiffrement_symetrique as chiffrement_symetrique
import src.chiffrement_asymetrique as chiffrement_asymetrique
import src.chiffrement_test_rsa as chiffrement_test_rsa
import src.gestion_cle as gestion_cle
import os

import time
from cryptography.fernet import Fernet


def benchmark(fichier):
    resultats = {}

    # Fernet
    key = Fernet.generate_key()

    start = time.time()
    chiffrement_symetrique.chiffrement_symetrique(fichier, key)
    t_enc = time.time() - start

    start = time.time()
    chiffrement_symetrique.dechiffrement_symetrique(fichier + ".enc", key)
    t_dec = time.time() - start

    resultats["Fernet"] = (t_enc, t_dec)

    """ # RSA
    gestion_cle.generation_cle_rsa()

    start = time.time()
    chiffrement_test_rsa.encrypt_file_rsa(fichier, "public.pem")
    t_enc = time.time() - start

    start = time.time()
    chiffrement_test_rsa.decrypt_file_rsa(fichier + ".rsa", "private.pem")
    t_dec = time.time() - start

    resultats["RSA"] = (t_enc, t_dec) """

    # Hybride
    start = time.time()
    chiffrement_asymetrique.encrypt_file_hybrid(fichier, "public.pem")
    t_enc = time.time() - start

    start = time.time()
    chiffrement_asymetrique.decrypt_file_hybrid(fichier, "private.pem")
    t_dec = time.time() - start

    resultats["Hybride"] = (t_enc, t_dec)

    return resultats
