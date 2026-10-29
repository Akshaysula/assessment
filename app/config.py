
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./vulntracker.db")

SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DB_USER = os.environ.get("DB_USER", "vulntracker_app")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "change-me-in-production")

ADMIN_API_KEY = os.environ.get("ADMIN_API_KEY", "change-me-in-production")

NOTIFY_SERVICE_URL = os.environ.get("NOTIFY_SERVICE_URL", "http://localhost:3001")