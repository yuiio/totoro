title: --- { cmd & fichier } ---

Pour executer du code python, deux possibilités :

1. Directement en ligne de commande
2. Depuis un fichier

Va falloir savoir faire ça pour la suite sinon ça risque d'être compliquer.

Essaye d'executer avec python en ligne de commande : `print('Hello Elliot')`

Puis enregistre le code suivant dans un fichier txt avec l'extension _.py_:

    def perroquet(num, nom):
        num = int(num)
        print(nom*num)

    print("Je suis le perroquet le plus rapide de l'ouest")
    nom = input('Ton prenom ?: ')
    num = input('Ton chiffre préféré ?: ')
    perroquet(num, nom)

Puis execute le.

_Tips pour le level suivant_: Lit chaque ligne de la séquence à haute voix en regardant la ligne précédente.

