import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"URL de conexión a PostgreSQL: {DATABASE_URL}")
API_KEY = os.getenv("API_KEY")