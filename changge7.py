from flask import Falsk
from flask.ext.sqlalchemy import SQLAIchemy
from datetime import fatetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:    '
db = SQLAlchemy(app)

class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.string(80))
	created_time = db.Column(db.DateTime())
	category_id = db.Column(db.Integer,db.ForeignKey('Category.id'))
	content = db.Column(db.Text)
	
	def __init__(self,id,title,created_time,category_id,content)
		self.title = title
		self.content = content
		if created_time is None:
		    created_time = datetime.now()
		self.created_time = created_time
		self.category_id = category_id
		
	def __repr__(self):
	    return '<Post %r>' %self.title
		
class Category(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(50))
	
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return '<Category %r>'% self.name
		
@app.route('/')
def index():
    return render_template('index.html',titles = Post.self.title)
	
@app.route('/files/<file_id>')
def file(file_id):


if __name__=='__main__':
	app.run()
