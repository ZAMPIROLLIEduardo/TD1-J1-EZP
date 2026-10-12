#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes.
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard.
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture.
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant.
"""

import os
import sys


def ouvrir():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r") as flux:
                return flux.read()
        except OSError as erreur:
            print(
                f"Erreur : impossible de lire '{sys.argv[1]}' ({erreur.strerror})",
                file=sys.stderr,
            )
            sys.exit(1)
    return sys.stdin.read()


def compter(text, debug=False):
    char = 0
    lig = 0
    mots = 0
    nouvelle_mot = True
    for c in text:
        char += 1

        # Substituído os 'if' pelo 'match/case' obrigatório do exercício
        match c:
            case "\n":
                lig += 1
                nouvelle_mot = True
            case " " | "\t":  # Adicionado o '\t' solicitado
                nouvelle_mot = True
            case _:
                if nouvelle_mot:
                    nouvelle_mot = False
                    mots += 1
                    if debug:
                        print(f"[DEBUG] mot n°{mots}", file=sys.stderr)

    return (char, lig, mots)


def lire():
    text = ouvrir()
    debug = int(os.environ.get("DEBUG") == "1")
    char, lig, mots = compter(text, debug)
    print(f"Caractères : {char}")
    print(f"Lignes     : {lig}")
    print(f"Mots       : {mots}")


if __name__ == "__main__":
    lire()
