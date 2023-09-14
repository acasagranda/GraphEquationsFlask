from flask import Flask, render_template,Response, session 
from helperlinear import linearpuzzlegraph,lineargeteq,linearmakeanswer
from helperabsval import absvalpuzzlegraph,absvalgeteq,absvalmakeanswer
from helperquad import quadpuzzlegraph,quadgeteq,quadmakeanswer
import io    
import matplotlib   
matplotlib.use('Agg')             
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from forms import GetEquationForm



app=Flask(__name__)
app.config['SECRET_KEY']='gslnh48937&%$_&'
app.secret_key='gslnh48937&%$_&'
funcchoices=['linear','absolute_value','quadratic']


#Home page - choose function
@app.route('/')
def index():
    return render_template('index.html',funcchoices=funcchoices)

#Function pages - choose level
@app.route('/linear')
def linear():
    return render_template('linear.html')

@app.route('/absolute_value')
def absolute_value():
    return render_template('absolute_value.html')

@app.route('/quadratic')
def quadratic():
    return render_template('quadratic.html')


#Function information pages
@app.route('/linearintro/<int:id>')
def linearintro(id):
    session["eqtries"]=0
    session["userequations"]=[]
    session["scale"]=random.random()
    m,b,targeteq=linearmakeanswer(id)
    session["answer"]=(m,b,targeteq)
    currpath="/static/images/linearintro"+str(id)+".png"
    return render_template('linearintro.html',currpath=currpath,id=id)

@app.route('/absolute_valueintro/<int:id>')
def absolute_valueintro(id):
    session["eqtries"]=0
    session["userequations"]=[]
    session["scale"]=random.random()
    m,h,k,targeteq=absvalmakeanswer(id)
    session["answer"]=(m,h,k,targeteq)
    currpath="/static/images/absvalintro"+str(id)+".png"
    return render_template('absolute_valueintro.html',currpath=currpath,id=id)

@app.route('/quadraticintro/<int:id>')
def quadraticintro(id):
    session["eqtries"]=0
    session["userequations"]=[]
    session["scale"]=random.random()
    m,h,k,targeteq=quadmakeanswer(id)
    session["answer"]=(m,h,k,targeteq)
    currpath="/static/images/quadintro"+str(id)+".png"
    return render_template('quadraticintro.html',currpath=currpath,id=id)


#Puzzle pages
@app.route('/linearpuzzle/<int:id>',methods=["GET","POST"])
def linearpuzzle(id):
    equationform=GetEquationForm()
    errortext=""
    if equationform.validate_on_submit():
        usereq=equationform.usereq.data
        m,b,errortext=lineargeteq(usereq,session.get("answer",None),id)
        
        if errortext=="" or errortext[0]=='C':
            if "userequations" in session:
                session["userequations"].append((m,b,usereq))  #extend
            else:
                session["userequations"] = [(m,b,usereq)]
            
            session["eqtries"]=session.get("eqtries",0)+1
        if errortext=="" and id<4 and session.get("eqtries",0)>=6:
            errortext="The equation of the red line is "+ session.get("answer",[])[2]
        elif errortext=="" and id==4 and session.get("eqtries",0)>=10:
            errortext="The equation of the red line is "+ session.get("answer",[])[2]
        if errortext!="" and (errortext[0]=='T' or errortext[0]=='C'):
            return render_template('linearsolved.html',errortext=errortext,id=id)     
        
    return render_template('linearpuzzle.html',errortext=errortext,template_form=equationform,id=id)


@app.route('/absolute_valuepuzzle/<int:id>',methods=["GET","POST"])
def absolute_valuepuzzle(id):
    equationform=GetEquationForm()
    errortext=""
    if equationform.validate_on_submit():
        usereq=equationform.usereq.data
        m,h,k,errortext=absvalgeteq(usereq,session.get("answer",None),id)
        
        if errortext=="" or errortext[0]=='C':
            if "userequations" in session:
                session["userequations"].append((m,h,k,usereq))  #extend
            else:
                session["userequations"] = [(m,h,k,usereq)]
            
            session["eqtries"]=session.get("eqtries",0)+1
        if errortext=="" and id<6 and session.get("eqtries",0)>=6:
            errortext="The equation of the red graph is "+ session.get("answer",[])[3]
        elif errortext=="" and id==6 and session.get("eqtries",0)>=10:
            errortext="The equation of the red graph is "+ session.get("answer",[])[3]
        if errortext!="" and (errortext[0]=='T' or errortext[0]=='C'):
            return render_template('absolute_valuesolved.html',errortext=errortext,id=id)     
        
    return render_template('absolute_valuepuzzle.html',errortext=errortext,template_form=equationform,id=id)

@app.route('/quadraticpuzzle/<int:id>',methods=["GET","POST"])
def quadraticpuzzle(id):
    equationform=GetEquationForm()
    errortext=""
    if equationform.validate_on_submit():
        usereq=equationform.usereq.data
        m,h,k,errortext=quadgeteq(usereq,session.get("answer",None),id)
        
        if errortext=="" or errortext[0]=='C':
            if "userequations" in session:
                session["userequations"].append((m,h,k,usereq))  
            else:
                session["userequations"] = [(m,h,k,usereq)]
            
            session["eqtries"]=session.get("eqtries",0)+1
        if errortext=="" and id<6 and session.get("eqtries",0)>=6:
            errortext="The equation of the red graph is "+ session.get("answer",[])[3]
        elif errortext=="" and id==6 and session.get("eqtries",0)>=10:
            errortext="The equation of the red graph is "+ session.get("answer",[])[3]
        if errortext!="" and (errortext[0]=='T' or errortext[0]=='C'):
            return render_template('quadraticsolved.html',errortext=errortext,id=id)     
        
    return render_template('quadraticpuzzle.html',errortext=errortext,template_form=equationform,id=id)



#Graphs for puzzle pages
@app.route('/plotlinear.png/<int:id>')
def plotlinear(id):
    m,b,targeteq=session.get("answer",None)
    fig = linearpuzzlegraph(m,b,targeteq,session.get("eqtries",0),session.get("userequations",[]),session.get("scale",.5),id)
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),mimetype='image/png')

@app.route('/plotabsval.png/<int:id>')
def plotabsval(id):
    m,h,k,targeteq=session.get("answer",None)
    fig = absvalpuzzlegraph(m,h,k,targeteq,session.get("eqtries",0),session.get("userequations",[]),session.get("scale",.5),id)
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),mimetype='image/png')

@app.route('/plotquad.png/<int:id>')
def plotquad(id):
    m,h,k,targeteq=session.get("answer",None)
    fig = quadpuzzlegraph(m,h,k,targeteq,session.get("eqtries",0),session.get("userequations",[]),session.get("scale",.5),id)
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),mimetype='image/png')



#Puzzle solved pages - choose what's next
@app.route('/linearsolved/<int:id>')
def linearsolved(id):
    return render_template('linearsolved.html',id=id)

@app.route('/absolute_valuesolved/<int:id>')
def absolute_valuesolved(id):
    return render_template('absolute_valuesolved.html',id=id)

@app.route('/quadraticsolved/<int:id>')
def quadraticsolved(id):
    return render_template('quadraticsolved.html',id=id)

