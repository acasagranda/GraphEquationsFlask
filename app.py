from flask import Flask, render_template,Response, session #request
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
from helperlinear1 import linear1puzzlegraph,linear1geteq,linear1makeanswer
from helperlinear2 import linear2makeanswer,linear2geteq,linear2puzzlegraph
import io
# import numpy as np    
import matplotlib   
matplotlib.use('Agg')          
# import matplotlib.pyplot as plt   
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from forms import GetEquationForm



app=Flask(__name__)
app.config['SECRET_KEY']='gslnh48937&%$_&'
app.secret_key='gslnh48937&%$_&'
funcchoices=['linear','absolute_value','quadratic']



@app.route('/')
def index():
    return render_template('index.html',funcchoices=funcchoices)

@app.route('/linear')
def linear():
    return render_template('linear.html')

@app.route('/linear1intro')
def linear1intro():
    session["eqtries"]=0
    session["userequations"]=[]
    session["scale"]=random.random()
    m,b,targeteq=linear1makeanswer()
    session["answer"]=(m,b,targeteq)
    
    return render_template('linear1intro.html')

@app.route('/linear2intro')
def linear2intro():
    session["eqtries"]=0
    session["userequations"]=[]
    session["scale"]=random.random()
    m,b,targeteq=linear2makeanswer()
    session["answer"]=(m,b,targeteq)
    
    return render_template('linear2intro.html')



@app.route('/linear1puzzle',methods=["GET","POST"])
def linear1puzzle():
    equationform=GetEquationForm()
    errortext=""
    if equationform.validate_on_submit():
        usereq=equationform.usereq.data
        m,b,errortext=linear1geteq(usereq,session.get("answer",None))
        if errortext=="" or errortext[0]=='C':
            if "userequations" in session:
                session["userequations"].append((m,b,usereq))  #extend
            else:
                session["userequations"] = [(m,b,usereq)]
            
            session["eqtries"]=session.get("eqtries",0)+1
        if errortext=="" and session.get("eqtries",0)>=6:
            errortext="The equation of the red line is "+ session.get("answer",[])[2]
        if errortext!="" and (errortext[0]=='T' or errortext[0]=='C'):
            return render_template('linear1solved.html',errortext=errortext)     
        
    return render_template('linear1puzzle.html',errortext=errortext,template_form=equationform)

@app.route('/linear2puzzle',methods=["GET","POST"])
def linear2puzzle():
    equationform=GetEquationForm()
    errortext=""
    if equationform.validate_on_submit():
        usereq=equationform.usereq.data
        m,b,errortext=linear2geteq(usereq,session.get("answer",None))
        if errortext=="" or errortext[0]=='C':
            if "userequations" in session:
                session["userequations"].append((m,b,usereq))  #extend
            else:
                session["userequations"] = [(m,b,usereq)]
            
            session["eqtries"]=session.get("eqtries",0)+1
        if errortext=="" and session.get("eqtries",0)>=6:
            errortext="The equation of the red line is "+ session.get("answer",[])[2]
        if errortext!="" and (errortext[0]=='T' or errortext[0]=='C'):
            return render_template('linear2solved.html',errortext=errortext)     
        
    return render_template('linear2puzzle.html',errortext=errortext,template_form=equationform)


@app.route('/plotlinear1.png')
def plotlinear1():
    m,b,targeteq=session.get("answer",None)
    fig = linear1puzzlegraph(m,b,targeteq,session.get("eqtries",0),session.get("userequations",[]),session.get("scale",.5))
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),mimetype='image/png')

@app.route('/plotlinear2.png')
def plotlinear2():
    m,b,targeteq=session.get("answer",None)
    fig = linear2puzzlegraph(m,b,targeteq,session.get("eqtries",0),session.get("userequations",[]),session.get("scale",.5))
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),mimetype='image/png')

@app.route('/linear1solved')
def linear1solved():
    return render_template('linear1solved.html')

@app.route('/linear2solved')
def linear2solved():
    return render_template('linear2solved.html')

@app.route('/absolute_value')
def absolute_value():
    return render_template('absolute_value.html')

@app.route('/quadratic')
def quadratic():
    return render_template('quadratic.html')
