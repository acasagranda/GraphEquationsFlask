import numpy as np                     
import random
import matplotlib.pyplot as plt


colors=[['darkviolet','blue','deepskyblue','lime','yellow','orange'],['violet','darkviolet','blue','deepskyblue','aquamarine','green','chartreuse','yellow','darkorange','orangered']]



def absvalmakeanswer(id):
    if id==1:   #set up y=|x|+k
        m=1
        k=0
        h=0
        while k==0:
            k=random.randrange(-9, 9)
        frac=False
    elif id==2:  #set up y=|x+h|
        m=1
        h=0
        k=0
        while h==0:
            h=random.randrange(-9,9)
        frac=False
    elif id==3:  #set up y=|x+h|+k
        m=1
        h=0
        k=0
        while h==0:
            h=random.randrange(-9,9)
        while k==0:
            k=random.randrange(-9, 9)
        frac=False
    else:    #set up y=+m|x|
        h=0
        k=0
        list1 = [2,3,4,5,6,7,8]
        m=random.choice(list1)
        list2=[True,False]
        frac=random.choice(list2)
    if id==5:  #use y=+m|x| and make y=-m|x|
        m=-m
    if id==6:    #use y=+m|x| and make it y=m|x + h|+k
        list3=[-1,1]
        msign=random.choice(list3)
        m=msign*m
        h=random.randrange(-9, 9)
        k=random.randrange(-9, 9)

    #set up |x| part of equation
    if h==0:
        heq='|x|'
    elif h>0:
        heq='|x + '+str(h)+' |'
    else:
        heq='|x - '+str(abs(h))+' |'

    #set up m of eq
    if frac and m<-1:
        meq='-1/'+str(abs(m))
        m=1/m
    elif frac and m>1:
        meq='1/' + str(m)
        m=1/m
    elif m==-1:
        meq='-'
    elif m==1:
        meq=''
    else:
        meq=str(m)

    #set up k part of equation
    if k<0:
        keq=' - '+str(abs(k))
    elif k>0:
        keq=' + '+str(k)
    else:
        keq=''

    targeteq='y = '+meq+heq+keq    
   
    return (m,h,k,targeteq)


def absvalgeteq(usereq,answer,id):
    if id==1:
        errortext=f"Equations should follow the format  y = |x| + k    or    y = |x| - k   where k is an integer between 1 and 9."
    elif id==2:
        errortext=f"Equations should follow the format  y = |x + h|    or    y = |x - h|   where h is an integer between 1 and 9."
    elif id==3:
        errortext=f"Equations should follow the format  y = |x + h| + k    where h and k are integers between -9 and 9."
    elif id==4:
        errortext=f"Equations should follow the format  y = m|x|    or    y = 1/m |x|   where m is an integer between 2 and 8."
    elif id==5:
        errortext=f"Equations should follow the format  y = -m|x|    or    y = -1/m |x|   where m is an integer between 2 and 8."
    else:
        errortext=f"Equations should follow the format\n      y = m|x + h| + k  or  y = 1/m |x + h| + k  or\n   y = -m|x + h| + k  or  y = -1/m |x + h| + k\nwhere m is an integer between 2 and 8 and h and k are an integers between -8 and 8."
    
    userin="".join(usereq.split())
    userin=userin.lower()
    frac=False
    msign=1
    hsign=1
    ksign=1
    if userin[:2]=='y=':
        userin=userin[2:]
    elif userin[-2:]=='=y':
        userin=userin[:-2]
    else:
        return 1,0,0,errortext
    
    #check for 2 abs val symbols
    absidx1=0
    while absidx1<len(userin) and userin[absidx1]!='|':
        absidx1+=1
    absidx2=absidx1+1
    while absidx2<len(userin) and userin[absidx2]!='|':
        absidx2+=1
    if absidx1==len(userin) or absidx2==len(userin):
        return 1,0,0,errortext
    
    #find x and h
    hsign=1
    inside=userin[absidx1+1:absidx2]
    if inside[0]=='x':
        inside=inside[1:]
    elif inside[-1]=='x':
        inside=inside[:-1]
    else:
        return 1,0,0,errortext
    if inside=='':
        h=0
    else:
        if inside and (inside[-1]=='+' or inside[-1]=='-'):
            inside=inside[:-1]
        if inside[0]=='-':
            hsign=-1
            inside=inside[1:]
        elif inside[0]=='+':
            inside=inside[1:]
        if inside.isnumeric():
            h=int(inside)
        else:
            return 1,0,0,errortext
        if h>9:
            return 1,0,0,errortext
        
    #find m
    m=0
    msign=1
    mstr=userin[:absidx1]
    midx=0
    if mstr=='':
        m=1
    if mstr=='-':
        m=1
        msign=-1
    if '/' in mstr:
        frac=True
        if mstr[0]=='1':
            midx=2
        elif mstr[:2]=='-1':
            msign=-1
            midx=3
        elif mstr[:2]=='+1':
            midx=3
        else:
            return 1,0,0,errortext
        if midx>=len(mstr) or not mstr[midx].isnumeric():
            return 1,0,0,errortext
          
    if mstr and mstr[midx]=='-':
        msign=-1
        midx+=1
    elif mstr and mstr[midx]=='+':
        midx+=1
    if m==0 and not mstr[midx:absidx1].isnumeric():
        return 1,0,0,errortext
    elif m==0:
        m=int(mstr[midx:absidx1])
    if m>9:
        return 1,0,0,errortext
    
    #find k
    ksign=1
    kstr=userin[absidx2+1:]
    k=-1
    if kstr=='':
        k=0
    if kstr and kstr[0]=='+':
        kstr=kstr[1:]
    elif kstr and kstr[0]=='-':
        ksign=-1
        kstr=kstr[1:]
    if k==-1 and kstr=='':
        return 1,0,0,errortext
    elif k==-1 and not kstr.isnumeric():
        return 1,0,0,errortext
    elif k==-1:
        k=int(kstr)
    if k>9:
        return 1,0,0,errortext
    
    if frac:
        m=1/m
    if answer[0]==m*msign and answer[1]==h*hsign and answer[2]==k*ksign:
            return m*msign,h*hsign,k*ksign,"Congratulations!  You've found the correct equation for the red graph."
    return m*msign,h*hsign,k*ksign,""


def absvalpuzzlegraph(m,h,k,targeteq,eqtries,userequations,scale,id):
    
    #set up size of graph
    axisdim=scale*10+10

    #make two columns of graphs
    if id<6:
        fig, (ax,textarea) = plt.subplots(1,2,figsize=(13,5),frameon=False)
    else:
        fig, (ax,textarea) = plt.subplots(1,2,figsize=(17,5),frameon=False)
    textarea.set(autoscale_on=False)
    #set up axes
    ax.set(xlim=(-axisdim, axisdim), ylim=(-axisdim, axisdim), aspect='equal',autoscale_on=False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    textarea.axis('off')

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03) 
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
    
    # Hide X and Y axes label marks
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)

    # Hide X and Y axes tick marks
    ax.set_xticks([])
    ax.set_yticks([])
    
    #no background grid
    ax.grid(False)

    # set up arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    
    
    text1="The "+ r"$\bf{"+ 'black' +"}$" + f" graph to the left is the \'parent\' function y = |x|."
    text2="\n\nYour task is to find the equation of the "+ r"$\bf{"+ 'red' +"}$" + f" graph.\
                      \n\nSince there are no unit marks on the graph, you'll have to guess\
                      \nand then use the result to get closer and closer\
                      \nuntil you find the red graph\'s equaton."
   
    if id==1:
        text3="The equations used in this puzzle will look like\
                      \ny = |x| + k where k is an integer between -9 and 9.\
                      \n\n(The | key is typically on the keyboard between\n the Enter and Backspace keys.)\
                      \n\nEnter your guess below."
    elif id==2:
        text3="The equations used in this puzzle will look like\
                      \ny = |x + h| where h is an integer between -9 and 9.\
                      \n\n(The | key is typically on the keyboard between\n the Enter and Backspace keys.)\
                      \n\nEnter your guess below."
    elif id==3:
        text3="The equations used in this puzzle will look like\
                      \ny = |x + h| + k where h and k are integers between -9 and 9.\
                      \n\n(The | key is typically on the keyboard between\n the Enter and Backspace keys.)\
                      \n\nEnter your guess below."
    elif id==4:
        text3="The equations used in this puzzle will either look like\
                      \ny = a|x| or y = 1/a |x|\
                      \nwhere a is an integer between 2 and 8.\
                      \n\n(The equation can actually by y = c/a |x| for any c but\
                      \nwe are limiting it to 1/a for this puzzle.)\
                      \n\n(The | key is typically on the keyboard between\n the Enter and Backspace keys.)\
                      \n\nEnter your guess below."
    elif id==5:
        text3="The equations used in this puzzle will either look like\
                      \ny = -a|x| or y = -1/a |x|\
                      \nwhere a is an integer between 2 and 8.\
                      \n\n(The equation can actually by y = c/a |x| for any c but\
                      \nwe are limiting it to 1/a for this puzzle.)\
                      \n\n(The | key is typically on the keyboard between\n the Enter and Backspace keys.)\
                      \n\nEnter your guess below."
    else:
        text3="The equations used in this puzzle will either look like\
                      \ny = a|x + h| + k  or  y = 1/a |x + h| + b  or\
        \ny = -a|x + h| + k  or  y = -1/a |x + h| + k\
                      \nwhere a is an integer between 2 and 8 \
                      \nand h and k are integers between -9 and 9.\
                      \n\n(The | key is typically on the keyboard between\n the Enter and Backspace keys.)\
                      \n\nEnter your guess below."


    #set up lines putting label here used in legend
    x11 =np.linspace(-axisdim,0)
    x12=np.linspace(0,axisdim)
    x21 =np.linspace(-axisdim,-h)
    x22=np.linspace(-h,axisdim)

    #plot parent
    ax.plot(x11, -x11,c='k',lw=1.5,label = 'y = |x|')
    ax.plot(x12,x12,c='k',lw=1.5)
    #plot answer if user found correct answer
    if userequations and userequations[-1][0]==m and userequations[-1][1]==h and userequations[-1][2]==k:  
        ax.plot(x21, m*abs(x21+h)+k,c='r',lw=3.5,label = userequations[-1][3])
        ax.plot(x22, m*abs(x22+h)+k,c='r',lw=3.5)
    #plot answer if user ran out of time
    elif id<6 and eqtries>=6:
        ax.plot(x21, m*abs(x21+h)+k,c='r',lw=1.5,label = targeteq)
        ax.plot(x22, m*abs(x22+h)+k,c='r',lw=1.5)
    elif id==6 and eqtries>=10:
        ax.plot(x21, m*abs(x21+h)+k,c='r',lw=1.5,label = targeteq)
        ax.plot(x22, m*abs(x22+h)+k,c='r',lw=1.5)
    #plot answer if normal user guess
    else:
        ax.plot(x21, m*abs(x21+h)+k,c='r',lw=1.5,label = "y = ?")
        ax.plot(x22, m*abs(x22+h)+k,c='r',lw=1.5)
    
    #plot all user guesses except last
    if userequations and id<6:
        for idx in range(len(userequations)-1):
            x31 =np.linspace(-axisdim,-userequations[idx][1])
            x32=np.linspace(-userequations[idx][1],axisdim)
            ax.plot(x31, userequations[idx][0]*abs(x31+userequations[idx][1])+userequations[idx][2],c=colors[0][idx],lw=1.5,label = userequations[idx][3])
            ax.plot(x32, userequations[idx][0]*abs(x32+userequations[idx][1])+userequations[idx][2],c=colors[0][idx],lw=1.5)
    if userequations and id==6:
        for idx in range(len(userequations)-1):
            x31 =np.linspace(-axisdim,-userequations[idx][1])
            x32=np.linspace(-userequations[idx][1],axisdim)
            ax.plot(x31, userequations[idx][0]*abs(x31+userequations[idx][1])+userequations[idx][2],c=colors[1][idx],lw=1.5,label = userequations[idx][3])
            ax.plot(x32, userequations[idx][0]*abs(x32+userequations[idx][1])+userequations[idx][2],c=colors[1][idx],lw=1.5)
    
    #plot current user guess if not correct 
    if userequations and id<6 and (userequations[-1][0]!=m or userequations[-1][1]!=h or userequations[-1][2]!=k):
        x31 =np.linspace(-axisdim,-userequations[-1][1])
        x32=np.linspace(-userequations[-1][1],axisdim)
        ax.plot(x31, userequations[-1][0]*abs(x31+userequations[-1][1])+userequations[-1][2],c=colors[0][len(userequations)-1],lw=1.5,label = userequations[-1][3])
        ax.plot(x32, userequations[-1][0]*abs(x32+userequations[-1][1])+userequations[-1][2],c=colors[0][len(userequations)-1],lw=1.5)
   
    if userequations and id==6 and (userequations[-1][0]!=m or userequations[-1][1]!=h or userequations[-1][2]!=k):
        x31 =np.linspace(-axisdim,-userequations[-1][1])
        x32=np.linspace(-userequations[-1][1],axisdim)
        ax.plot(x31, userequations[-1][0]*abs(x31+userequations[-1][1])+userequations[-1][2],c=colors[1][len(userequations)-1],lw=1.5,label = userequations[-1][3])
        ax.plot(x32, userequations[-1][0]*abs(x32+userequations[-1][1])+userequations[-1][2],c=colors[1][len(userequations)-1],lw=1.5)
    
    #set up legend
    ax.legend(loc="lower right")
    if id==6:
        ax.legend(bbox_to_anchor=(1.05, 1.0))

    
    #set up text
    textarea.text(0,.9,text1,fontsize=12)
    textarea.text(0,.6,text2,fontsize=12)
    textarea.text(0,.1,text3,fontsize=12)
    ax.margins(y=0)
    
    return fig
    
