''' 
===================================================================
==                   #####                  #  #                 ==
==                  #    #                   ##                  ==
==                   ##  ###   #  # # ###   #  #                 ==
==                     # #  # # # #   #  #  #  #                 ==
==     make by     ####  #  # ##  #   ###    ##                  ==
==                                    #                          ==
==                                    #                          ==
===================================================================
'''
from time import gmtime, strftime
import os

data=[]
log={
    0:'Action', 1:'Warning', 2:'Error',
    10:'Unknow',
    11:'get_data() info:', 12:'set_data() info:',
    13:'mod_data() info:', 14:'read_data() info:',
    15:'inGame_data() info:', 16:'inGame_data_reverse() info:',
    17:'find() info:',
    100:'score.txt', 101:'debug.txt', 102:'exp.txt'
}

def get_data(filename):
    file=open(filename)
    content=file.read()
    log_debug_add(0,11,'...')
    file.close()
    return content

def set_data(filename,string=''):
    file=open(filename,'a')
    file.write(str(string))
    log_debug_add(0,12,str(string))
    file.close()
    return get_data(filename)

def mod_data(filename,string,place):
    content=get_data(filename)
    file=open(filename,'w')
    content_modif=content[0:int(place)]+string+content[int(place)+len(string):len(content)]
    file.write(content_modif)
    log_debug_add(0,13,str(string)+' at '+str(place))
    file.close()
    return get_data(filename)

def log_debug_add(cts=0,txt=10,text=''):
    file=open('debug.txt','a')
    now=strftime('%Y-%m-%d %H:%M:%S', gmtime())
    content='['+str(now)+']-['+str(log[cts])+'] '+str(log[txt])+' '+str(text)+'\n'
    file.write(content)
    file.close()

def reader_data(filename):
    content=get_data(filename)
    list_ln=0; data=''; l=[]; l_data=[]
    for i in content:
        if i == ',':
            if list_ln >= 1:
                data=int(data)
            l_data.append(data)
            list_ln+=1; data=''
        elif i == '\n':
            l.append(l_data); list_ln=0
            l_data=[]; data+=''
        else:
            data+=i
    log_debug_add(0,14,l)
    return l

def find(string='',l=[]):
    content=None
    for i in l:
        if i[0] == string:
            content=i
    log_debug_add(0,17,' data find: '+str(content))
    return content

def inGame_data(l=[],c=0):
    list_=l[c]
    name=list_[0]
    score=list_[1]
    level=list_[2]
    xp=list_[3]
    log_debug_add(0,15,' extract n:'+str(c)+', name: '+str(name)+', score: '\
        +str(score)+', level: '+str(level)+', xp: '+str(xp))
    return name, score, level, xp

def Ingame_data_reverse(stats=()):
    (name,score,level,xp)=stats
    content=str(name)+','+str(score)+','+str(level)+','+str(xp)+',\n'
    log_debug_add(0,16,' '+content)
    return content

''' Commentaires:
print(reader_data('score.txt'))
print(set_data('score.txt','Essai,1,1,1,\n'))
mod_data('score.txt','3',6)
'''