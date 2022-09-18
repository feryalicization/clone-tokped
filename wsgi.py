from config import Config
from entity import db
from flask import Flask, render_template, jsonify
from datetime import date 
import requests
import os
from entity.model import *
import validators
from entity.model import User



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)




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



@app.route('/register')
def register():

    # email
    # if param['email'] is None:
    #     return jsonify({'msg': 'Email cannot be empty', 'code': '-1'})
    # if not validators.email(param['email']):
    #     return jsonify({'error': "Email is not valid"})

    

    return render_template('register.html')
























if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True)