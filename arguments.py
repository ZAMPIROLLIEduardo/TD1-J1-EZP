#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell.
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant.
"""

import os, sys


def arguments():
    """Fonction qui affiche les arguments de la ligne de commande."""
    args = sys.argv[1:]
    if not args:
        print("Erreur, aucun argument dans env", file=sys.stderr)
        sys.exit(1)
    if "DEBUG" in os.environ:
        debug = 1
    else:
        debug = 0
    i = 1
    for arg in args:
        if debug and os.environ["DEBUG"] == "1":
            print(f"{i} : {arg}")
        else:
            print(f"{arg}")
        i += 1


if __name__ == "__main__":
    arguments()
