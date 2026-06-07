from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///empskills.db'

db=SQLAlchemy(app)

@app.route("/")
def homepage():
    return "<h1> Welcome to Employee Management System </h1>"

@app.route('/skillset/update',methods=['GET','POST'])
def updateskillset():
    if request.method=='POST':
        email=request.form['email']
        skillset = ','.join(request.form.getlist('skills'))
        data=Skills(emailid=email,skills=skillset)
        db.session.add(data)
        db.session.commit()
        return render_template('updateskill.html',success='Skill set updated successfully')
    return render_template('updateskill.html')

class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    emailid=db.Column(db.String(250))
    skills=db.Column(db.Text())
    
if not os.path.isfile('empskills.db'):
    with app.app_context():
        db.create_all()
