from flask import Flask,render_template,url_for,flash,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///root1.db'
db=SQLAlchemy(app)
class Task(db.Model):
    id= db.Column(db.Integer,primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(400), nullable=False)
    lastname = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False)
    content = db.Column(db.String(400), nullable=False)

    def __init__(self, firstname, lastname, email, content):
        self.firstname = firstname
        self.lastname = lastname
        self.email= email
        self.content = content
        


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index")
def home1():
    return render_template("index.html")


@app.route("/portfolio-page.html")
def portfolio1():
    return render_template("portfolio-page.html")


@app.route("/portfolio-page2.html")
def portfolio2():
    return render_template("portfolioII-page.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")
    
        
@app.route('/insert',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        firstname = request.form['Fname']
        lastname = request.form['Lname']
        email = request.form['Email']
        content = request.form['Comment']

        mydata = Task(firstname,lastname,email,content)
        db.session.add(mydata)
        db.session.commit()

        print("data inserted successfully")

        return render_template("contact.html")



        

if __name__=="__main__":
    app.run(debug=True)








    
   

        
     
        



