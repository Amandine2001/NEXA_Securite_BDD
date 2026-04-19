# Création de copie d’un fichier dans 2 locations différentes

import shutil
import os


def sauvegarde_fichier(source_path: str, destination1: str, destination2: str):
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Fichier introuvable: {source_path}")

    # Création des dossiers si inexistants
    os.makedirs(destination1, exist_ok=True)
    os.makedirs(destination2, exist_ok=True)

    # Nom du fichier
    filename = os.path.basename(source_path)

    dest1_path = os.path.join(destination1, filename)
    dest2_path = os.path.join(destination2, filename)

    # Copie
    shutil.copy2(source_path, dest1_path)
    shutil.copy2(source_path, dest2_path)

    print(f"Sauvegarde effectuée :")
    print(f"- {dest1_path}")
    print(f"- {dest2_path}")

    return dest1_path, dest2_path
