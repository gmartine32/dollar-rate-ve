from flask import Blueprint, jsonify, request
from app.schemas import RateInput
from app.services import get_current_rate, get_rate_by_date, create_rate
from adapters.auth import require_api_key

rate_bp = Blueprint("rate", __name__)

@rate_bp.route("/rate/current", methods=["GET"])
def current_rate():
    rate = get_current_rate()
    if not rate:
        return jsonify({"error": "No data"}), 404
    return jsonify({
        "date": rate.date,
        "rate": float(rate.rate),
        "change_pct": float(rate.change_pct) if rate.change_pct else None
    })

@rate_bp.route("/rate/<date>", methods=["GET"])
def rate_by_date(date):
    rate = get_rate_by_date(date)
    if not rate:
        return jsonify({"error": "Date not found"}), 404
    return jsonify({
        "date": rate.date,
        "rate": float(rate.rate),
        "change_pct": float(rate.change_pct) if rate.change_pct else None
    })

@rate_bp.route("/rate", methods=["POST"])
def insert_rate():
    require_api_key()
    body = request.get_json()
    data = RateInput(**body)
    rate = create_rate(data.date, data.rate)
    return jsonify({
        "message": "Rate inserted successfully",
        "rate": float(rate.rate),
        "change_pct": float(rate.change_pct) if rate.change_pct else None
    }), 201