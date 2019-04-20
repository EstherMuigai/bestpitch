from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))

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

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")

    def __repr__(self):
        return f'User {self.id}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    users = db.relationship('User',backref = 'comment',lazy="dynamic")

    def __repr__(self):
        return f'User {self.id}'