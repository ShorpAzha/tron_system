# Save Game System
## Sommaire:
### [1. Fonctions](#fonctions)
### [2. Intégration](#ajout-dans-un-jeu-déjà-existants)
## Fonctions:
### get_data(filename)
Récupére les données de ```filename```
### set_data(filename, string)
Ajoute les données ```string``` à ```filename``` à la fin du fichier
### mod_data(filename, stats, name)
Remplace les données de ```name``` en ```stats``` qui est demandé comme un tuple, dans ```filename```
### reader_data(filename)
Lit les données de ```filename``` et en retourne une table
### find(string,l)
Trouve le ```string``` dans la table ```l```
### find_data_place(string,l)
Trouve l'emplacement de ```string``` dans la table ```l``` et en retourne la valeur
### inGame_data(l,c)
Prend la table n°```c``` dans la table ```l``` et le retourne en tuple ```stats```
### inGame_data_reverse(stats)
Convertie le tuple ```stats``` en une table en format ```stats```
## Ajout dans un jeu déjà existants
### Partie haute du script
Avant l'import de pygame ou du module graphique, mettre:
```
user=False
while user==False:
    user_name_j1=input('J1:')
    #user_name_j2=input('J2:')
    user=True
```
Ici, il y a besoin de 2 joueurs: ```user_name_j1``` & ```user_name_j2```, mais il est possible d'en ajouter autant que souhaité. Il faut simplement en ajouter autant par morceaux suivants.
### Partie variables
Ensuite, plus loin, après les variables pour optimisé son script et ainsi le rendre plus lisible:
```
user_srch=find(user_name_j1,reader_data(log[100]))
exist=False
if user_srch == None: scoretot=0; xp=0
else: scoretot=user_srch[1]; xp=user_srch[3]; exist=True
score=0
```
### Partie Basse
Enfin, à la fin du script, une fois le jeu éteint mais pas le script:
```
statsj1=(user_name_j1,scoretot,0,xp)
if exist == True: mod_data(log[100],statsj1,user_name_j1)
else: set_data(log[100],Ingame_data_reverse(statsj1))
```