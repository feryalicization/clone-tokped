import email
from config import Config
from entity import db
from flask import Flask, render_template, jsonify, redirect, url_for, flash
from datetime import date 
import os
from entity.model import *
import validators
from entity.model import User
from flask_mail import Mail, Message
from random import randint
from flask import request, session





app = Flask(__name__)
mail=Mail(app)
app.config.from_object(Config)
db.init_app(app)


app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='fery.alicization@gmail.com'
app.config['MAIL_PASSWORD']='nzfxacevgeipxnjx'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=randint(000000,999999)




@app.route('/')
def index():
    
    query = db.session.query(User).filter(User.deleted_date ==  None)
    data = []
    for x in query:
        data.append({
            'username': x.username,
            'email': x.email
        })
        

    return render_template('index.html', data=data)


from random import *  
from tes import *

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
      
        email=request.form['email']
        msg=Message(subject='OTP',sender='fery.alicization@gmail.com',recipients=[email])
        msg.body=str(otp)
        mail.send(msg)

        # req = db.session.query(User).filter_by(id=3).first()
        # req.otp=otp
        # db.session.commit()

        # print(f'thai {req.otp}')
        return redirect(url_for('verify'))

    return render_template('register.html')



@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp=request.form['otp']
        if otp==int(user_otp):
            return "<h3>Email varification succesfull</h3>"
        return "<h3>Please Try Again</h3>"

    return render_template('verify.html')



     


    
    
























if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True)