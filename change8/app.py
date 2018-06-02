from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/test'
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__='file'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),unique=True)
    create_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__(self,title,create_time,category,content):
        self.title = title
        self.create_time = create_time
        self.category = category
        self.content = content

class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    

    def __init__(self,name):
        self.name = name

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())
@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item = file_item)
@app.errorhandler(404)
def notfound(error):
    return render('404.html'),404

if __name__=='__main__':
    app.run()

