title: --- { Des boucles et des tests } ---

En python y a aussi des outils pour faire des [boucles](http://apprendre-python.com/page-apprendre-boucles-python-loop).

Par exemple pour comptre jusqu'à 100 :

    for i in range(0,100):
      print(i)

Ou pour boucler sur toutes les lettres :

    v = "Bonjour toi"
    for lettre in v:
        print lettre
    ...
    B
    o
    n
    j
    o
    u
    r

    t
    o
    i


Et y'a aussi des outils pour faire des [tests de conditions](http://apprendre-python.com/page-apprendre-conditions-structures-conditionnelles-if-else-python-cours-debutant).

Par exemple voici en test dans une fonction permettant de savoir si un caractère est bien une lettre :

    def verifie_lettre(caractere):
        if str(caractere).isalpha():
            print("C'est une lettre")
        else:
            print("Ce n'est pas une lettre")
        

    verifie_lettre(1)
    verifie_lettre('e')
    verifie_lettre('#')

    ...
    Ce n'est pas une lettre
    C'est une lettre
    Ce n'est pas une lettre



_Tips pour le prochain niveau_ : L'heure approche et tu connais déjà la réponse.

