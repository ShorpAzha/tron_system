'''
Tron: NSI Mini-project
'''
user=False
while user==False:
    user_name_j1=input('J1:')
    user_name_j2=input('J2:')
    user=True

import pygame
from random import *

from score_system import *

#constantes de la fenêtre d'affichage
LARGEUR=1200       #hauteur de la fenêtre
HAUTEUR=700      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
MAGENTA=(255,0,128)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//2
motoY=HAUTEUR//2
motoX_=LARGEUR//3
motoY_=HAUTEUR//3
direction = 'gameover'
direction_ = 'gameover'
tempsPartie=0
pl_win=''
spw_crc=20
spw_sqr=30
user_srch=find(user_name_j1,reader_data(log[100]))
exist=False
if user_srch == None: scoretot=0; xp=0
else: scoretot=user_srch[1]; xp=user_srch[3]; exist=True
score=0
user_srch_=find(user_name_j2,reader_data(log[100]))
exist_=False
if user_srch_ == None: score_tot=0; xp_=0
else: score_tot=user_srch_[1]; xp_=user_srch_[3]; exist_=True
score_=0

def rand():
    x,y=randrange(0,LARGEUR),randrange(0,HAUTEUR)
    h=randrange(5,20)
    return x,y,h

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],1)
    for i in range(0,spw_crc):
        x,y,h=rand()
        pygame.draw.circle(fenetre, ROUGE, (x,y), h)
    for i in range(0,spw_sqr):
        x,y,h=rand()
        pygame.draw.rect(fenetre, BLEU, [x, y, h, h],0)

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def end_game(scr):
    global motoY_,motoX_,motoY,motoX,direction,direction_
    fenetre.fill((0,0,0))
    afficheTexte(5,5,'Game Over')
    afficheTexte(5,25,'Winner: '+str(pl_win))
    afficheTexte(5,45,'Score: '+str(scr))
    motoX=LARGEUR//2
    motoY=HAUTEUR//2
    motoX_=LARGEUR//3
    motoY_=HAUTEUR//3
    direction_='gameover'
    direction='gameover'

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond à une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto_():
    global motoX_,motoY_
    touche_=False
    if direction_=='haut':
        x_=motoX_
        y_=motoY_-1
        touche_=collisionMur(x_,y_)
    elif direction_=='bas':
        x_=motoX_
        y_=motoY_+1
        touche_=collisionMur(x_,y_)
    elif direction_=='droite':
        x_=motoX_+1
        y_=motoY_
        touche_=collisionMur(x_,y_)
    elif direction_=='gauche':
        x_=motoX_-1
        y_=motoY_
        touche_=collisionMur(x_,y_)
    elif direction_=='gameover':
        x_=motoX_
        y_=motoY_
        touche_=False
    if touche_==False:
        motoX_=x_
        motoY_=y_
    fenetre.set_at((x_, y_), MAGENTA)
    return touche_

def deplacementmoto():
    """
    deplace la moto si c'est possible
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX+1
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gameover':
        x=motoX
        y=motoY
        touche=False
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), VERT)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée


loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE: #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction = 'gauche'
    if keys[pygame.K_z]:
        direction_ = 'haut'
    elif keys[pygame.K_s]:
        direction_ = 'bas'
    elif keys[pygame.K_d]:
        direction_ = 'droite'
    elif keys[pygame.K_q]:
        direction_ = 'gauche'

    #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisé ici

    if deplacementmoto()==True or deplacementmoto_()==True:
        if deplacementmoto()==True:
            pl_win=str(user_name_j1)
            score=tempsPartie
            scoretot+=score
            xp+=1
            win_scr=score
        elif deplacementmoto_()==True:
            pl_win=str(user_name_j2)
            score_=tempsPartie
            score_tot+=score_
            xp_+=1
            win_scr=score_
        tempsPartie=0 
        end_game(win_scr)
        dessineDecor()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
    tempsPartie+=1
pygame.quit()
statsj1=(user_name_j1,scoretot,0,xp)
if exist == True: mod_data(log[100],statsj1,user_name_j1)
else: set_data(log[100],Ingame_data_reverse(statsj1))
statsj2=(user_name_j2,score_tot,0,xp_)
if exist_==True: mod_data(log[100],statsj2,user_name_j2)
else: set_data(log[100],Ingame_data_reverse(statsj2))
print('R.I.P.')
print('temps partie',tempsPartie)


