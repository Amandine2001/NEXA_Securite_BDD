# Importation
import pandas as pd

# Lecture d'un fichier .txt


def lecture_fichier_txt(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = f.read()
    return data


# Lecture d'un fichier .csv
def lecture_fichier_csv(chemin_fichier):
    data = pd.read_csv(chemin_fichier, sep=";")
    return data


# Lecture d'un fichier .xlsx
def lecture_fichier_xlsx(chemin_fichier):
    data = pd.read_excel(chemin_fichier)
    return data
