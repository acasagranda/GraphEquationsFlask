import numpy as np                 
#import matplotlib.pyplot as plt    
import random
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

#other requirements
#import io

colors=['darkviolet','blue','deepskyblue','lime','yellow','orange']

def linear1makeanswer():
    m=1
    b=0
    while b==0:
        b=random.randrange(-9, 9)
    if b<0:
        targeteq='y = x - '+str(abs(b))
    else:
        targeteq='y = x + '+str(b)
    return (m,b,targeteq)

def linear1puzzlegraph(m,b,targeteq,eqtries,userequations,scale1):
    
    #set up size of graph
    axisdim=scale1*10+10

    #make to columns of graphs
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
                      \nuntil you find the red line\'s equaton.\
                      \n\nAll numbers used in the equation will be integers\
                      \nbetween -9 and 9.\
                      \n\nEnter your guess below."


    
    
    #set up lines putting label here used in legend
    x =np.linspace(-axisdim,axisdim)
    

    ax.plot(x, x,c='k',lw=1.5,label = 'y = x')
    #ax.plot(x,m*x+b,c='r',lw=1.5,label='y = ?')
    
    if userequations and userequations[-1][0]==m and userequations[-1][1]==b:  
        ax.plot(x, m*x+b,c='r',lw=3.5,label = userequations[-1][2])
    elif eqtries>=6:
        ax.plot(x, m*x+b,c='r',lw=1.5,label = targeteq)
    else:
        ax.plot(x, m*x+b,c='r',lw=1.5,label = "y = ?")
    
    if userequations:
        for idx in range(len(userequations)-1):
            ax.plot(x, userequations[idx][0]*x+userequations[idx][1],c=colors[idx],lw=1.5,label = userequations[idx][2])
        
    if userequations and (userequations[-1][0]!=m or userequations[-1][1]!=b):
        ax.plot(x, userequations[-1][0]*x+userequations[-1][1],c=colors[len(userequations)-1],lw=1.5,label = userequations[-1][2])

    #set up legend
    ax.legend(loc="lower right")
    
    #set up text
    textarea.text(0,.9,text1,fontsize=12)
    textarea.text(0,.3,text2,fontsize=12)
    ax.margins(y=0)
    
    #fig.bbox_inches('tight')
    return fig
    #return plt

def linear1geteq(usereq,answer):
    errortext=f"Equations should follow the format  y = x + b    or    y = x - b   where b is an integer between 1 and 9."
    
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


