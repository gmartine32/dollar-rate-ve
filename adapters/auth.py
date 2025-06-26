from flask import request, abort
from config import API_KEY

def require_api_key():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        abort(401, "Unauthorized")