from config import Config
from entity import db
from flask import Flask, render_template, jsonify
from datetime import date 
import os
from entity.model import *
import validators
from entity.model import User
from flask_mail import Mail, Message
from random import randint
from flask import request, session
from utils import *




app = Flask(__name__)
mail=Mail(app)
app.config.from_object(Config)
db.init_app(app)


app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='fery.chaerul@gmail.com'
app.config['MAIL_PASSWORD']='putricantik2'                    #you have to give your password of gmail account
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



@app.route('/register', methods=['GET', 'POST'])
def register():

    # email
    # if param['email'] is None:
    #     return jsonify({'msg': 'Email cannot be empty', 'code': '-1'})
    # if not validators.email(param['email']):
    #     return jsonify({'error': "Email is not valid"})
    # if request.method == 'POST':
    email = request.form.get('email')
    msg=Message(subject='OTP',sender='fery.chaerul@gmail.com',recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template('register.html')
    
    
























if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True)