import numpy as np                     
import random
import matplotlib.pyplot as plt


colors=[['darkviolet','blue','deepskyblue','lime','yellow','orange'],['violet','darkviolet','blue','deepskyblue','aquamarine','green','chartreuse','yellow','darkorange','orangered']]



def linearmakeanswer(id):
    if id==1:   #set up y=x+b
        m=1
        b=0
        while b==0:
            b=random.randrange(-9, 9)
        frac=False
    else:    #set up y=+mx
        b=0
        list1 = [2,3,4,5,6,7,8]
        m=random.choice(list1)
        list2=[True,False]
        frac=random.choice(list2)
    if id==3:  #use y=+mx and make y=-mx
        m=-m
    if id==4:    #use y=+mx and make it y=mx+b
        list3=[-1,1]
        msign=random.choice(list3)
        m=msign*m
        b=random.randrange(-9, 9)

    #set up x part of equation
    if frac and m<-1:
        meq='-1/'+str(abs(m))+'x'
        m=1/m
    elif frac and m>1:
        meq='1/' + str(m)+'x'
        m=1/m
    elif m==-1:
        meq='-x'
    elif m==1:
        meq='x'
    else:
        meq=str(m)+'x'
    #set up b part of equation
    if b<0:
        beq=' - '+str(abs(b))
    elif b>0:
        beq=' + '+str(b)
    else:
        beq=''

    targeteq='y = '+meq+beq    
   
    return (m,b,targeteq)


def lineargeteq(usereq,answer,id):
    if id==1:
        errortext=f"Equations should follow the format  y = x + b    or    y = x - b   where b is an integer between 1 and 9."
    elif id==2:
        errortext=f"Equations should follow the format  y = mx    or    y = 1/m x   where m is an integer between 2 and 8."
    elif id==3:
        errortext=f"Equations should follow the format  y = -mx    or    y = -1/m x   where m is an integer between 2 and 8."
    else:
        errortext=f"Equations should follow the format\n      y = ax + b  or  y = 1/a x  or   y = -ax + b  or  y = -1/a x + b\nwhere a is an integer between 2 and 8 and b is an integer between -8 and 8.\n"
    
    userin="".join(usereq.split())
    userin=userin.lower()
    frac=False
    msign=1
    bsign=1
    if userin[:2]=='y=':
        userin=userin[2:]
    elif userin[-2:]=='=y':
        userin=userin[:-2]
    else:
        return 1,0,errortext
    xidx=0
    
    while xidx<len(userin) and userin[xidx]!='x':
        xidx+=1
    if xidx==len(userin):
        return 1,0,errortext
    startidx=xidx-1
    while startidx>-1 and userin[startidx]!='-' and userin[startidx]!='+':
        startidx-=1
    if startidx==-1:
        startidx=0
    startp=startidx
    if '/' in userin[startp:xidx]:
        frac=True
        if userin[startp]=='1':
            startp+=2
        elif userin[startp:startp+2]=='-1':
            msign=-1
            startp+=3
        elif userin[startp:startp+2]=='+1':
            startp+=3
        else:
            return 1,0,errortext
        if startp==xidx or not userin[startp:xidx].isnumeric():
            return 1,0,errortext
        
    
    if userin[startp]=='-':
        msign=-1
        startp+=1
    elif userin[startp]=='+':
        startp+=1
    
    if startp==xidx:
        m=1
    elif userin[startp:xidx].isnumeric():
        m=int(userin[startp:xidx])
    else:
        return 1,0,errortext
   
    if m<-9 or m>9:
        return 1,0,errortext
    userin=userin[:startidx]+userin[xidx+1:]
    bsign=1
    if userin=='':
        b=0
    elif userin[0]=='-':
        bsign=-1
        userin=userin[1:]
    elif userin[0]=='+':
        userin=userin[1:]
    if userin!='' and userin.isnumeric():
        b=int(userin)
    elif userin!='':
        return 1,0,errortext
    if b<-9 or b>9:
        return 1,0,errortext
    if frac:
        m=1/m
    if answer[0]==m*msign and answer[1]==b*bsign:
            return m*msign,b*bsign,"Congratulations!  You've found the correct equation for the red line."
    return m*msign,b*bsign,""



def linearpuzzlegraph(m,b,targeteq,eqtries,userequations,scale,id):
    
    #set up size of graph
    axisdim=scale*10+10

    #make two columns of graphs
    fig, (ax,textarea) = plt.subplots(1,2,figsize=(13,5),frameon=False)
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
    
    
    text1="The "+ r"$\bf{"+ 'black' +"}$" + f" line graphed to the left is the \'parent\' function y = x."
    text2="\n\nYour task is to find the equation of the "+ r"$\bf{"+ 'red' +"}$" + f" line.\
                      \n\nSince there are no unit marks on the graph, you'll have to guess\
                      \nand then use the result to get closer and closer\
                      \nuntil you find the red line\'s equaton."
    
    if id==1:
        text3="All numbers used in the equation will be integers\
                      \nbetween -9 and 9.\
                      \n\nEnter your guess below."
    elif id==2:
        text3="The equation used in this puzzle will either look like\
                      \ny = ax or y=1/a x where a is an integer between 2 and 8.\
                      \n\n(The equation can be y=c/a x for any c\
                       \nbut we are limiting it to 1/a x for this puzzle.)\
                      \n\nEnter your guess below."
    elif id==3:
        text3="The equation used in this puzzle will either look like\
                      \ny = -ax or y=-1/a x where a is an integer between 2 and 8.\
                      \n\n(The equation can be y=c/a x for any c\
                       \nbut we are limiting it to 1/a x for this puzzle.)\
                      \n\nEnter your guess below."
    else:
        text3="The equation used in this puzzle will either look like\
                      \ny = ax + b  or  y = 1/a x + b  or   y = -ax + b  or  y = -1/a x + b\
                      \nwhere a is an integer between 2 and 8 \
                      \nand b is an integer between -8 and 8.\
                      \n\nEnter your guess below."


    #set up lines putting label here used in legend
    x =np.linspace(-axisdim,axisdim)
    

    ax.plot(x, x,c='k',lw=1.5,label = 'y = x')
    #ax.plot(x,m*x+b,c='r',lw=1.5,label='y = ?')
    
    if userequations and userequations[-1][0]==m and userequations[-1][1]==b:  
        ax.plot(x, m*x+b,c='r',lw=3.5,label = userequations[-1][2])
    elif id<4 and eqtries>=6:
        ax.plot(x, m*x+b,c='r',lw=1.5,label = targeteq)
    elif id==4 and eqtries>=10:
        ax.plot(x, m*x+b,c='r',lw=1.5,label = targeteq)
    else:
        ax.plot(x, m*x+b,c='r',lw=1.5,label = "y = ?")
    
    if userequations and id<4:
        for idx in range(len(userequations)-1):
            ax.plot(x, userequations[idx][0]*x+userequations[idx][1],c=colors[0][idx],lw=1.5,label = userequations[idx][2])
    if userequations and id==4:
        for idx in range(len(userequations)-1):
            ax.plot(x, userequations[idx][0]*x+userequations[idx][1],c=colors[1][idx],lw=1.5,label = userequations[idx][2])  
    
    if userequations and id<4 and (userequations[-1][0]!=m or userequations[-1][1]!=b):
        ax.plot(x, userequations[-1][0]*x+userequations[-1][1],c=colors[0][len(userequations)-1],lw=1.5,label = userequations[-1][2])
    if userequations and id==4 and (userequations[-1][0]!=m or userequations[-1][1]!=b):
        ax.plot(x, userequations[-1][0]*x+userequations[-1][1],c=colors[1][len(userequations)-1],lw=1.5,label = userequations[-1][2])
    
    #set up legend
    ax.legend(loc="lower right")
    
    #set up text
    textarea.text(0,.9,text1,fontsize=12)
    textarea.text(0,.6,text2,fontsize=12)
    textarea.text(0,.2,text3,fontsize=12)
    ax.margins(y=0)
    
    return fig
    



