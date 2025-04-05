from collections import Counter
import re


def top_5_mots(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as file:
            text = file.read()
            texte = texte.translate(str.maketrans("", "", text.punctuation)).lower()
            compteur = Counter(mots)
            mots_les_plus_communs = compteur.most_common(5)
            print("Les 5 mots les plus utilisés sont :")
            for mot, freq in mots_les_plus_communs:
                print(f"{mot}: {freq} fois")
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
