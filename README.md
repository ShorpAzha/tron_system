# Save Game System
## Sommaire:
### [1. Fonctions](https://github.com/ShorpAzha/tron_system#fonctions)
### [2. Intégration (*WIP*)](https://github.com/ShorpAzha/tron_system#ajout-dans-un-jeu-d%C3%A9j%C3%A0-existants)
## Fonctions:
### get_data(filename)
Récupére les données de ```filename```
### set_data(filename, string)
Ajoute les données ```string``` à ```filename```
### mod_data(filename, string, place)
Modifie/Remplace les données en ```place``` par ```string``` dans ```filename```
### reader_data(filename)
Lit les données de ```filename``` et en fait une table
### inGame_data(l,c)
Prend la table n°```c``` dans la table ```l``` et l'extait en format ```stats```
### inGame_data_reverse(stats)
Convertie le tuple ```stats``` en une table èn format ```stats```
### find(string,l)
Trouve le ```string``` dans la table ```l```
## Ajout dans un jeu déjà existants (en cours de création)
### Dans le script du jeu *WIP*
Pour l'intégré, il faut bien sûr utiliser:
```
from score_system import *
```
Ensuite, pour sauvegarder les données:
```
statsj1=([name_j1],[score],[level],[xp])
set_data(log[100],Ingame_data_reverse(statsj1))
```
La variable: ```log[100]``` correspond au fichier ```'scrore.txt'```
*WIP*