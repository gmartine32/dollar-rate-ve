from flask import Flask, request
from flask_cors import CORS
from app.models import db
from ports.routes import rate_bp
from config import DATABASE_URL
import logging
from logging.handlers import RotatingFileHandler
import time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

# Configurar logging
log_formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

file_handler = RotatingFileHandler('logs/api.log', maxBytes=1000000, backupCount=3)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(log_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(log_formatter)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)

CORS(app)
db.init_app(app)
app.register_blueprint(rate_bp)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request(response):
    duration = round(time.time() - request.start_time, 4)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    method = request.method
    path = request.path
    status = response.status_code

    app.logger.info(f"{ip} {method} {path} {status} [{duration}s]")
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.exception("Unhandled exception: %s", str(e))
    return {"error": "Internal server error"}, 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=3000)