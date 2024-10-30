from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ensemble(db.Model):
    __tablename__ = 'ensembles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    albums = db.relationship('Album', backref='ensemble', lazy=True)

class Musician(db.Model):
    __tablename__ = 'musicians'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    instruments = db.Column(db.String(150))
    ensemble_id = db.Column(db.Integer, db.ForeignKey('ensembles.id'), nullable=True)

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    release_date = db.Column(db.Date)
    wholesale_price = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    sales_last_year = db.Column(db.Integer, default=0)
    sales_current_year = db.Column(db.Integer, default=0)
    quantity_available = db.Column(db.Integer, default=0)
    ensemble_id = db.Column(db.Integer, db.ForeignKey('ensembles.id'), nullable=True)
