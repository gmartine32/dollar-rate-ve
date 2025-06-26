from app.models import db, ExchangeRate
from datetime import timedelta

def get_current_rate():
    return ExchangeRate.query.order_by(ExchangeRate.date.desc()).first()

def get_rate_by_date(target_date):
    return ExchangeRate.query.filter_by(date=target_date).first()

def create_rate(date, rate):
    previous = ExchangeRate.query.filter_by(date=date - timedelta(days=1)).first()
    change_pct = None
    if previous:
        change_pct = round(((rate - previous.rate) / previous.rate) * 100, 2)
    new_rate = ExchangeRate(date=date, rate=rate, change_pct=change_pct)
    db.session.add(new_rate)
    db.session.commit()
    return new_rate