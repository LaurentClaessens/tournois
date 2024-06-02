# Tournois

## Principe

Nous considérons un tournois dans lequel plusieurs personnes s'affrontent. Si des poules sont faites, il est possible d'avoir des "incohérences" dans les résultats. Par exemple, il peut arriver que :

- A bat B
- B bat C
- C bat A.

Si des poules sont organisées, il peut arriver que A gagne contre B en poule, mais perde en tableau.


Le but de ce programme est de prendre en entrée les résultats de chacune des rencontres, et d'attribuer une force moyenne et un écart-type à chaque participant de façon à maximiser la probabilité des résultats.


## Hypothèses

Je suppose qu'un joueur a une force moyenne et un écart-type. À chaque combat, chaque joueur donne une force aléatoire selon une normale centrée en sa moyenne.


## Mathématique

Ce qui est cherché est la moyenne et l'écart-type `(m_i, s_i)` pour chaque joueur `i`.

La probabilité que `i` gagne le combat `i vs j` est la probabilité que la variable aléatoire normale `(m_i, s_i)` soit plus grande que la normale `(m_j, s_j)`.

Les résultats de toutes les rencontres sont donnés. Je veux maximiser leur probabilité simultanée en fonction des variables `(m_i,s_i)`.

## Implémentation

Au départ je voulais faire une descente de gradient, mais comme ça va quand même vite, j'optimise un paramètre à la fois et je fais plusieurs passages.


## Exemple


Je prends comme exemple les -40kg ici :
https://liguebfc.ffjudo.com/resultat/criterium-bfc-benjamins-nes/32502
Les résultats sont ici : 
https://dev.licences-ffjudo.com/FFJDA_events_Docs/94528_Resultats_Sportifs_Feminines.pdf
