import os
from flask import Flask, render_template, url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from werkzeug import url_encode
app = Flask(__name__)

UPLOAD_FOLDER='/home/sai/datavideoapp/static'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///videonames.db"
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


db=SQLAlchemy(app)
# Migrate(app,db)

class videofiles(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)


@app.route('/',methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        f = request.files['inputfiles']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        newdata = videofiles(name=f.filename)
        db.session.add(newdata)
        db.session.commit()
        return redirect(url_for('play'))
    
    return render_template('home.html')

@app.route('/play')
def play():
    file_data = videofiles.query.all()
    l=[]
    for i in file_data:
        l.append(i.name)
        print(i.name)
    print(l)

    return render_template('play.html',videos=l)


if __name__ == '__main__':
    app.run(debug=True)
