from project import db, bcrypt, app
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import datetime
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)
    items = db.relationship('Items', backref='user', lazy='dynamic')
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.authenticated = False
        self.registered_on = datetime.now()
        self.last_logged_in = None
        self.current_logged_in = datetime.now()
    @hybrid_property
    def password(self):
        return self._password
    @password.setter
    def set_password(self, password):
        self._password = bcrypt.generate_password_hash(password)
    @hybrid_method
    def is_correct_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated
    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True
    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False
    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)
    def __repr__(self):
        return '<User {}>'.format(self.email)


class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, notes, user_id):
        self.name = name
        self.notes = notes
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)