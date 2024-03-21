# Save Game System
## Fonctions:
### get_data(filename)
récupére les données de filename (chemin)
### set_data(filename, string)
ajoute les données string à filename
### mod_data(filename, string, place)
modifie les données données en [place] en string dans filename
### reader_data(filename)
lit les données de filename et en fait des tableaux
### inGame_data()
transforme les tableaux en données lisible par le jeux
### inGame_data_reverse()
### find(string,l)
trouve le string dans la table l
## Ajout dans un jeu déjà existants
### Dans le script du jeu
Pour l'intégré, il faut bien sûr utiliser:```from system import *```
Ensuite, pour sauvegarder les données:
```
set_data('score.txt',data)
```
