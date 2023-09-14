import numpy as np                     
import random
import matplotlib.pyplot as plt


colors=[['darkviolet','blue','deepskyblue','lime','yellow','orange'],['violet','darkviolet','blue','deepskyblue','aquamarine','green','chartreuse','yellow','darkorange','orangered']]



def quadmakeanswer(id):
    if id==1:   #set up y=x^2+k
        m=1
        k=0
        h=0
        while k==0:
            k=random.randrange(-9, 9)
        frac=False
    elif id==2:  #set up y=(x+h)^2
        m=1
        h=0
        k=0
        while h==0:
            h=random.randrange(-9,9)
        frac=False
    elif id==3:  #set up y=(x+h)^2+k
        m=1
        h=0
        k=0
        while h==0:
            h=random.randrange(-9,9)
        while k==0:
            k=random.randrange(-9, 9)
        frac=False
    else:    #set up y=+mx^2
        h=0
        k=0
        list1 = [2,3,4,5,6,7,8]
        m=random.choice(list1)
        list2=[True,False]
        frac=random.choice(list2)
    if id==5:  #use y=+mx^2 and make y=-mx^2
        m=-m
    if id==6:    #use y=+mx^2 and make it y=m(x + h)^2+k
        list3=[-1,1]
        msign=random.choice(list3)
        m=msign*m
        h=random.randrange(-9, 9)
        k=random.randrange(-9, 9)

    #set up (x)^2 part of equation
    if h==0:
        heq='x\u00b2'
    elif h>0:
        heq='(x + '+str(h)+' )\u00b2'
    else:
        heq='(x - '+str(abs(h))+' )\u00b2'

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


def quadgeteq(usereq,answer,id):
    #set up error messages for each level
    if id==1:
        errortext=f"Equations should follow the format  y = x\u00b2 + k    or    y = x\u00b2 - k   where k is an integer between 1 and 9."
    elif id==2:
        errortext=f"Equations should follow the format  y = (x + h)\u00b2    or    y = (x - h)\u00b2   where h is an integer between 1 and 9."
    elif id==3:
        errortext=f"Equations should follow the format  y = (x + h)\u00b2 + k    where h and k are integers between -9 and 9."
    elif id==4:
        errortext=f"Equations should follow the format  y = mx\u00b2    or    y = 1/m x\u00b2   where m is an integer between 2 and 8."
    elif id==5:
        errortext=f"Equations should follow the format  y = -mx\u00b2    or    y = -1/m x\u00b2   where m is an integer between 2 and 8."
    else:
        errortext=f"Equations should follow the format\n      y = m(x + h)\u00b2 + k  or  y = 1/m (x + h)\u00b2 + k  or\n   y = -m(x + h)\u00b2 + k  or  y = -1/m (x + h)\u00b2 + k\nwhere m is an integer between 2 and 8 and h and k are an integers between -8 and 8."
    
    #take out spaces and make all vars lowercase
    userin="".join(usereq.split())
    userin=userin.lower()
    frac=False
    msign=1
    hsign=1
    ksign=1

    #check if equation is y= or =y
    if userin[:2]=='y=':
        userin=userin[2:]
    elif userin[-2:]=='=y':
        userin=userin[:-2]
    else:
        return 1,0,0,errortext
    
    #check for ^
    hatidx=0
    while hatidx<len(userin) and userin[hatidx]!='^':
        hatidx+=1
    if hatidx==len(userin) or hatidx==0:
        return 1,0,0,errortext
    if userin[hatidx+1]!='2':
        return 1,0,0,errortext
    if hatidx+1!=len(userin)-1 and userin[hatidx+2]!='+' and userin[hatidx+2]!='-':
        return 1,0,0,errortext
    
    
    #find x and h
    hsign=1
    if userin[hatidx-1]=='x':
        h=0
        end=hatidx-2
    elif userin[hatidx-1]==')':
        #find (
        pidx=hatidx-2
        while pidx>-1 and userin[pidx]!='(':
            pidx-=1
        if pidx==-1:
            return 1,0,0,errortext
        end=pidx-1
        inside=userin[pidx+1:hatidx-1]
        #find x
        xidx=0
        while xidx<len(inside) and inside[xidx]!='x':
            xidx+=1
        if xidx==len(inside):
            return 1,0,0,errortext
        if xidx==0:
            inside=inside[1:]
        elif xidx==1 and inside[0]=='+':
            inside=inside[2:]
        elif xidx==1 and inside[0]=='-':
            hsign*=(-1)
            inside=inside[2:]
        elif xidx==1:
            return 1,0,0,errortext
        elif xidx==len(inside)-1 and inside[xidx-1]=='+':
            inside=inside[:-2]
        elif xidx==len(inside)-1 and inside[xidx-1]=='-':
            hsign*=(-1)
            inside=inside[:-2]
        else:
            return 1,0,0,errortext
        
        #find h
        if inside=='':
            h=0
        elif inside[0]=='+':
            inside=inside[1:]
        elif inside[0]=='-':
            hsign*=(-1)
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
    mstr=userin[:end+1]
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
    if m==0 and not mstr[midx:end+1].isnumeric():
        return 1,0,0,errortext
    elif m==0:
        m=int(mstr[midx:end+1])
    if m>9:
        return 1,0,0,errortext
    
    #find k
    ksign=1
    kstr=userin[hatidx+2:]
    
    if kstr=='':
        k=0
    else:
        if kstr[0]=='+':
            kstr=kstr[1:]
        elif kstr[0]=='-':
            ksign=-1
            kstr=kstr[1:]
        if kstr=='':
            return 1,0,0,errortext
        elif not kstr.isnumeric():
            return 1,0,0,errortext
        
        k=int(kstr)
    if k>9:
        return 1,0,0,errortext
    
    if frac:
        m=1/m
    if answer[0]==m*msign and answer[1]==h*hsign and answer[2]==k*ksign:
            return m*msign,h*hsign,k*ksign,"Congratulations!  You've found the correct equation for the red graph."
    return m*msign,h*hsign,k*ksign,""



def quadpuzzlegraph(m,h,k,targeteq,eqtries,userequations,scale,id):
    
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
    
    
    text1="The "+ r"$\bf{"+ 'black' +"}$" + f" graph to the left is the \'parent\' function y = x\u00b2."
    text2="\n\nYour task is to find the equation of the "+ r"$\bf{"+ 'red' +"}$" + f" graph.\
                      \n\nSince there are no unit marks on the graph, you'll have to guess\
                      \nand then use the result to get closer and closer\
                      \nuntil you find the red graph\'s equaton."
   
    if id==1:
        text3="The equations used in this puzzle will look like\
                      \ny = x\u00b2 + k where k is an integer between -9 and 9.\
                      \n\nUse the ^ (hat or carot) key above the 6 on the keyboard\n to mark that the next character is an exponent.\
                      \n(Type y = x^2 for y = x\u00b2.)\
                      \n\nEnter your guess below."
    elif id==2:
        text3="The equations used in this puzzle will look like\
                      \ny = (x + h)\u00b2 where h is an integer between -9 and 9.\
                      \n\nUse the ^ (hat or carot) key above the 6 on the keyboard\n to mark that the next character is an exponent.\
                      \n(Type y = (x+2)^2 for y = (x+2)\u00b2.)\
                      \n\nEnter your guess below."
    elif id==3:
        text3="The equations used in this puzzle will look like\
                      \ny = (x + h)\u00b2 + k where h and k are integers between -9 and 9.\
                      \n\nUse the ^ (hat or carot) key above the 6 on the keyboard\n to mark that the next character is an exponent.\
                      \n(Type y = (x+2)^2-3 for y = (x+2)\u00b2-3.)\
                      \n\nEnter your guess below."
    elif id==4:
        text3="The equations used in this puzzle will either look like\
                      \ny = ax\u00b2 or y = 1/a x\u00b2\
                      \nwhere a is an integer between 2 and 8.\
                      \n\n(The equation can actually by y = c/a x\u00b2 for any c but\
                      \nwe are limiting it to 1/a for this puzzle.)\
                      \n\nUse the ^ (hat or carot) key above the 6 on the keyboard\n to mark that the next character is an exponent.\
                      \n(Type y = x^2 for y = x\u00b2.)\
                      \n\nEnter your guess below."
    elif id==5:
        text3="The equations used in this puzzle will either look like\
                      \ny = -ax\u00b2 or y = -1/a x\u00b2\
                      \nwhere a is an integer between 2 and 8.\
                      \n\n(The equation can actually by y = c/a x\u00b2 for any c but\
                      \nwe are limiting it to 1/a for this puzzle.)\
                      \n\nUse the ^ (hat or carot) key above the 6 on the keyboard\n to mark that the next character is an exponent.\
                      \n(Type y = x^2 for y = x\u00b2.)\
                      \n\nEnter your guess below."
    else:
        text3="The equations used in this puzzle will either look like\
                      \ny = a(x + h)x\u00b2 + k  or  y = 1/a (x + h)x\u00b2 + b  or\
        \ny = -a(x + h)x\u00b2 + k  or  y = -1/a (x + h)x\u00b2 + k\
                      \nwhere a is an integer between 2 and 8 \
                      \nand h and k are integers between -9 and 9.\
                      \n\nUse the ^ (hat or carot) key above the 6 on the keyboard\n to mark that the next character is an exponent.\
                      \n(Type y = 4(x+2)^2-3 for y = 4(x+2)\u00b2-3.)\
                      \n\nEnter your guess below."


    #set up lines putting label here used in legend
    x =np.linspace(-axisdim,axisdim,num=150)
    
    #plot parent
    ax.plot(x, x*x,c='k',lw=1.5,label = 'y = x\u00b2')
    
    #plot answer if user found correct answer
    if userequations and userequations[-1][0]==m and userequations[-1][1]==h and userequations[-1][2]==k:  
        ax.plot(x, m*(x+h)**2+k,c='r',lw=3.5,label = userequations[-1][3])
    
    #plot answer if user ran out of time
    elif id<6 and eqtries>=6:
        ax.plot(x, m*(x+h)**2+k,c='r',lw=1.5,label = targeteq)
    elif id==6 and eqtries>=10:
        ax.plot(x, m*(x+h)**2+k,c='r',lw=1.5,label = targeteq)
        
    #plot answer if normal user guess
    else:
        ax.plot(x, m*(x+h)**2+k,c='r',lw=1.5,label = "y = ?")
        
    
    #plot all user guesses except last
    if userequations and id<6:
        for idx in range(len(userequations)-1):
            ax.plot(x, userequations[idx][0]*(x+userequations[idx][1])**2+userequations[idx][2],c=colors[0][idx],lw=1.5,label = userequations[idx][3])
            
    if userequations and id==6:
        for idx in range(len(userequations)-1):
            ax.plot(x, userequations[idx][0]*(x+userequations[idx][1])**2+userequations[idx][2],c=colors[1][idx],lw=1.5,label = userequations[idx][3])
            
    
    #plot current user guess if not correct 
    if userequations and id<6 and (userequations[-1][0]!=m or userequations[-1][1]!=h or userequations[-1][2]!=k):
        ax.plot(x, userequations[-1][0]*(x+userequations[-1][1])**2+userequations[-1][2],c=colors[0][len(userequations)-1],lw=1.5,label = userequations[-1][3])
       
    if userequations and id==6 and (userequations[-1][0]!=m or userequations[-1][1]!=h or userequations[-1][2]!=k):
        ax.plot(x, userequations[-1][0]*(x+userequations[-1][1])**2+userequations[-1][2],c=colors[1][len(userequations)-1],lw=1.5,label = userequations[-1][3])
        
    
    #set up legend
    ax.legend(loc="lower right")
    if id==6:
        ax.legend(bbox_to_anchor=(1.05, 1.0))

    
    #set up text
    textarea.text(0,1,text1,fontsize=12)
    textarea.text(0,.7,text2,fontsize=12)
    textarea.text(0,.1,text3,fontsize=12)
    ax.margins(y=0)
    
    return fig
    

