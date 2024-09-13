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
    17:'find() info:', 18:'find_data_place() info:',
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

def mod_data(filename,stats,name):
    content=reader_data(filename)
    file=open(filename,'w')
    (name_,score,level,xp)=stats
    #(name_,score,level,xp)=inGame_data(content,find_data_place(str(name),content))
    content_modif=[name_,score,level,xp]
    print(content_modif)
    del content[find_data_place(str(name),content)]
    content.append(content_modif)
    print(content)
    data=''
    for i in range(0,len(content)):
        data+=Ingame_data_reverse(inGame_data(content,i))
    file.write(data)
    log_debug_add(0,13,str(stats)+' in score of: '+str(name))
    
    file.close()
    return get_data(filename)

def log_debug_add(cts=0,txt=10,text=''):
    file=open('debug.txt','a')
    now=strftime('%Y-%m-%d %H:%M:%S', gmtime())
    content='['+str(now)+']-['+str(log[cts])+'] '+str(log[txt])+' '+str(text)+'\n'
    file.write(content)
    file.close()

def log_debug_get_num(date):
    (year,month,day,hour,minut,second)=date
    date_mod='['+str(year)+'-'+str(month)+'-'+str(day)\
        +' '+str(hour)+':'+str(minut)+':'+str(second)+']'
    content=get_data(log[101])
    data=''; ln=[]
    for i in content:
        if i == '\n': ln.append(data); data=''
        else: data+=str(i)
    inDate_content=[]
    for  j in range(0,len(ln)):
        if ln[j][0:21] == date_mod: inDate_content.append(j)
    return inDate_content, ln

def log_debug_get_data(date,printable=False):
    (inDate_content,ln)=log_debug_get_num(date)
    inDate_content_unlisted=[]
    for k in inDate_content:
        inDate_content_unlisted.append(ln[k])
        if printable == True: print(ln[k])
    return inDate_content_unlisted

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

def find_data_place(string='',l=[]):
    place=0
    for i in range(0,len(l)):
        if l[i][0] == string:
            place=i
    log_debug_add(0,18,' dat find at: '+str(place))
    return place

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

#log_debug_get_data((2024,'03',22,19,58,'06'),True)

#print(find_data_place('Shorp',reader_data(log[100])))
#print(Ingame_data_reverse(inGame_data(reader_data(log[100]),find_data_place('Shorp',reader_data(log[100])))))

'''
stats=('Shorp',2990,0,9)
mod_data(log[100],stats,'Shorp')

content=reader_data(log[100])
print(content)
del content[find_data_place('Shorp',reader_data(log[100]))]
print(content)

statsj2=('Essai',1000,0,0)
set_data(log[102],Ingame_data_reverse(statsj2))
user=find('Essai',reader_data(log[102]))
if user == None:
    print('non existant')
else:
    print('existant')

print(reader_data('score.txt'))
print(set_data('score.txt','Essai,1,1,1,\n'))
mod_data('score.txt','3',6)
'''