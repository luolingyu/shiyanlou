from flask import Blueprint,render_template
from simpledu.models import User

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    user = User.query.first()
    
    return render_template('user.html',user=user)
