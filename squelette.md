title: --- Skel3t0r ---

<style>
    p {
        -webkit-animation: color-change2 5s infinite;
        -moz-animation: color-change2 5s infinite;
        -o-animation: color-change2 5s infinite;
        -ms-animation: color-change2 5s infinite;
        animation: color-change2 5s infinite;
    }
    code {
        -webkit-animation: color-change 5s infinite;
        -moz-animation: color-change 5s infinite;
        -o-animation: color-change 5s infinite;
        -ms-animation: color-change 5s infinite;
        animation: color-change 5s infinite;
    }

    @-webkit-keyframes color-change {
        0% { color: #0f0f23; }
        50% { color: #CCCCCC; }
        100% { color: #0f0f23; }
    }
    @-moz-keyframes color-change {
        0% { color: #0f0f23; }
        50% { color: #CCCCCC; }
        100% { color: #0f0f23; }
    }
    @-ms-keyframes color-change {
        0% { color: #0f0f23; }
        50% { color: #CCCCCC; }
        100% { color: #0f0f23; }
    }
    @-o-keyframes color-change {
        0% { color: #0f0f23; }
        50% { color: #CCCCCC; }
        100% { color: #0f0f23; }
    }
    @keyframes color-change {
        0% { color: #0f0f23; }
        50% { color: #CCCCCC; }
        100% { color: #0f0f23; }
    }

    @-webkit-keyframes color-change2 {
        0% { color: #CCCCCC; }
        50% { color: #0F0F23; }
        100% { color: #CCCCCC; }
    }
    @-moz-keyframes color-change2 {
        0% { color: #CCCCCC; }
        50% { color: #0F0F23; }
        100% { color: #CCCCCC; }
    }
    @-ms-keyframes color-change2 {
        0% { color: #CCCCCC; }
        50% { color: #0F0F23; }
        100% { color: #CCCCCC; }
    }
    @-o-keyframes color-change2 {
        0% { color: #CCCCCC; }
        50% { color: #0F0F23; }
        100% { color: #CCCCCC; }
    }
    @keyframes color-change2 {
        0% { color: #CCCCCC; }
        50% { color: #0F0F23; }
        100% { color: #CCCCCC; }
    }
</style>

          .-.          
         (o.o)  boo !       
          |=|          
         __|__         
       //.=|=.\\       
      // .=|=. \\      
      \\ .=|=. //      
       \\(_=_)//       
        (:| |:)        
         || ||         
         () ()         
         || ||         
         || ||         
        ==' '==        

Oh! un squelette de code ! P'têt qu'en le modifiant ça peut te servir ? À toi de voir ...

    # Conseils pour jeune hacker :
    # Hacker ça veut dire bidouiller
    # N'hésite pas à transformer ce code et faire des essais. 
    # Ne change qu'un élément à la fois




    # La listes des instructions que le robot à effectué
    log = ['R5', 'L5', 'R5', 'R3']


    # Direction vers lequel le robot regarde. Variable de type texte (chaine de charactères) 
    # Peut-être :
    # 'N' -> Le nord
    # 'S' -> Le sud
    # 'O' -> L'ouest
    # 'E' -> L'est 
    direction = 'N' # Direction au départ

    # Variable dans laquelle on va enregistrer les coordonnées du robot.
    # Il s'agit d'une liste de deux nombres entiers.
    # On va considérer que le premier nombre est la position x et le deuxieme la position y sur une grille
    # On y accéde de cete manière :
    # x -> coord[0], premier élément de la liste.
    # y -> coord[1], deuxième élément de la liste.
    # Ainsi si le robot se déplace :
    # - vers l'est la position x augmente
    # - vers l'ouest la position x diminue
    # - vers le nord la position y diminue
    # - vers le sud la position y augmente
    coord = [0, 0] # Position au départ : x = 0, y = 0

    # Distance total parcourue par le robot à la fin des instructions
    longueur_parcour = 0

    # Boucle pour chaque instruction contenu dans la liste
    for instruction in log:

        # Essaye d'afficher instruction en décommentant la ligne ci-dessous
        # print(instruction)

        # Ici on décode l'instruction : on la coupe en deux. 
        # En fait une chaine de charactère (un mot) peut-être considérée comme une liste (de lettre). 
        tourne = instruction[0] # Dans quel sens tourne le robot : 'R' -> droite, 'L' -> gauche
        distance = int(instruction[1:]) # nombre entier représantant la distance que parcours le robot pendant cette instruction
        
        # A essayer aussi :
        # print(tourne)
        # print(distance)

        # On stocke dans cette variable le cumul de toutes les distance parcourue
        longueur_parcour = longueur_parcour + distance

        # Une fois l'instruction décodé on la traite.
        if tourne == 'R': # Si le robot tourne à droite

            if direction == 'N': # Si la direction actuelle est le nord et que le robot tourne à droite ...
                direction = 'E' # ... alors le robot regarde maintenant vers l'est ...
                                # Dans les deux lignes précédentes, faut bien faire la différence entre :
                                # == : utiliser pour tester l'égalité
                                # = : pour affecter une nouvelle valeur à la variable direction
                coord[0] += distance # ... et la position est modifiée 
                                # Ici += est un raccourci pour : coord[0] = coord[0] + distance
                                # on additionne la distance à la position x du robot
            elif direction == 'E':
                direction = 'S'
                coord[1] += distance
            elif direction == 'S':
                direction = 'O'
                coord[0] -= distance
            else: #direction=O
                direction = 'N'
                coord[1] -= distance

        else: # tourne = 'L'. # Si le robot tourne à gauche

            if direction == 'N': 
                direction = 'O'
                coord[0] -= distance
            elif direction == 'E':
                direction = 'N'
                coord[1] -= distance
            elif direction == 'S':
                direction = 'E'
                coord[0] += distance
            else: #direction=O
                direction = 'S'
                coord[1] += distance

    # On affiche un résultat
    print(longueur_parcour)
    # La même chose en plus joli : les {} sont remplacé par le contenu de la variable longueur_parcouru grâce à la fonction format
    print("BipBop s'est déplacé de {} plaques.".format(longueur_parcour))

    # Mais ou est BipBop ? D'ou part-il et ou arrive-il ?