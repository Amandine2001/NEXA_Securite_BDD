# Cargement de la configuration


def lire_configuration(chemin_fichier: str) -> dict:
    config = {}

    with open(chemin_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()

            # ignorer lignes vides et commentaires
            if not ligne or ligne.startswith("#"):
                continue

            if "=" in ligne:
                cle, valeur = ligne.split("=", 1)

                cle = cle.strip()
                valeur = valeur.strip()

                # enlever les guillemets éventuels
                if valeur.startswith('"') and valeur.endswith('"'):
                    valeur = valeur[1:-1]

                config[cle] = valeur

    return config
