# AI-Quixo

## Stratégie

Notre stratégie est essentiellement basé sur la défense.

Au début, nous essayons de jouer tous les coins afin de pouvoir maximiser le nombres de lignes ou de colonnes sur les quelles nous pouvons gagner.

Pour la défense, nous comptons à chaque fois le nombre de X ou de O, selon ce que l'adversaire est, sur les différentes lignes et colonnes et lorsque le nombre est égale ou plus grand à 3, on fait tout pour réduire ce nombre à 2. 

En ce qui consiste l'attaque, nous jouons des coups au hasards si tous les coins sont pris.

Lorsque nous possédons 4 X ou O sur la même ligne ou colonne nous essayons de faire aligner un 5e afin de pouvoir gagner la partie.

## Bibliothèques
    -Numpy
    -Random
    -Cherrypy
    -sys
## Auteurs
    Finias Calugar 17184
    Yassin Souidi 17031