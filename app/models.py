from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import  login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    
    __tablename__ = 'blogs'
   
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_blogs(cls):
        Blog.blog_list.clear()

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.all()
        return blogs

    def get_specific_blog(cls,id):
        blogs = Blog.query.filter_by(id=id).all()
        return blogs

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'user', lazy= "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,author, quote):
        self.author = author
        self.quote = quote
