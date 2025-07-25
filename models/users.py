from . import db
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(100))
    username = db.Column(db.String(40),unique=True)
    email = db.Column(db.String(60),unique=True)
    password = db.Column(db.String(198))
    roleid = db.Column(db.Integer,db.ForeignKey('roles.id'))

    role = db.relationship('Roles', back_populates='users')

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    description = db.Column(db.Text)

    users = db.relationship('Users', back_populates='role', lazy=True)
    permissions = db.relationship('Permision', back_populates='role_rel', lazy=True)
class Permision(db.Model):
    __tablename__ = 'permisions'
    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.Integer,db.ForeignKey('roles.id'))
    name = db.Column(db.String(50),unique=True,nullable=False)
    description = db.Column(db.Text)

    role_rel = db.relationship('Roles', back_populates='permissions')
    # Role :
    # id:1 , name :guest
    # id:2 , name:customer ,

    # Permission
    # id:1 , role:1 , name:view product
    # id:2 , role:2 , name :view product,buy product