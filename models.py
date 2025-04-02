from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    page_link = db.Column(db.String(10000), unique=True, nullable=False)
    rating = db.Column(db.Integer)
    cost = db.Column(db.String(10), nullable=False)
    time = db.Column(db.Integer)  # in minutes

    def __repr__(self):
        return f"{self.name} - {self.page_link}"
    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(10000), unique=True, nullable=False)
    rating = db.Column(db.Integer)
    cost = db.Column(db.String(10), nullable=False)
    time = db.Column(db.Integer)  # in minutes

    def __repr__(self):
        return f"{self.name} - {self.description}"
    
