import nltk
from nltk.tokenize import word_tokenize

# Assure-toi d'avoir les ressources nécessaires de NLTK
nltk.download("punkt")


def richesse_lexicale(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            texte = f.read()
    except FileNotFoundError:
        print(f"Fichier non trouvé : {fichier}")
        return None

    tokens = word_tokenize(texte.lower())  # Tokenisation + mise en minuscules
    types = set(tokens)  # Éléments uniques

    nb_tokens = len(tokens)
    nb_types = len(types)

    ratio = nb_types / nb_tokens if nb_tokens > 0 else 0

    print(f"Nombre de tokens : {nb_tokens}")
    print(f"Nombre de types : {nb_types}")
    print(f"Richesse lexicale (type/token) : {ratio:.4f}")

    return ratio


# Exemple d'utilisation :
# Remplace 'mon_texte.txt' par le nom de ton fichier texte
if __name__ == "__main__":
    fichier = "littJeun.txt"
    ttt = richesse_lexicale(fichier)
    print(ttt)
