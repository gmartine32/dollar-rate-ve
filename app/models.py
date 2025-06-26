from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ExchangeRate(db.Model):
    __tablename__ = 'exchange_rates'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)
    rate = db.Column(db.Numeric(10, 4), nullable=False)
    change_pct = db.Column(db.Numeric(6, 2))
    created_at = db.Column(db.DateTime)