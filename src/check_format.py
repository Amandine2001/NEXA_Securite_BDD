# Vérification des formats de documents : xlsx, csv, txt
import pandas as pd


def check_format_doc(chemin_fichier):
    ext = chemin_fichier.split(".")[-1].lower()

    match ext:
        case "xlsx":
            return "xlsx"
        case "csv":
            return "csv"
        case "txt":
            return "txt"
        case _:
            raise ValueError(
                "Format de fichier non supporté. Veuillez fournir un fichier .xlsx, .csv ou .txt."
            )
