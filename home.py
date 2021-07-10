from flask import Flask,render_template,request,redirect,url_for
import os
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite12')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)




class filecontents(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)





@app.route('/')
def index():
    return render_template('home.html')




@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['inputfiles']
    return file.filename



if __name__ == '__main__':
    app.run(debug=True)

