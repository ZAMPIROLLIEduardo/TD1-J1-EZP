#! /usr/bin/env python3
"""Ce programme permet de compter le nombre de caractères saisi par l'utilisateur dans son entrée standard et de l'afficher.
- Ce programme demandera à l'utilisateur de saisir une chaine uniquement s'il est invoqué en mode interactif.
- Ce programme ne devra afficher sur la sortie standard *que* le nombre de caractères saisi.
- Une fois le programme ci-dessous mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant.
"""

import sys


def comptage():
    """Retourne le nombre de caractères de l'entrée standard."""
    if sys.stdin.isatty():
        print("Inserez votre text (Ctrl+D pour terminer) :", file=sys.stderr)
    return len(sys.stdin.read())


if __name__ == "__main__":
    print(comptage())
