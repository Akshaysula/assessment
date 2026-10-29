from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def search_scans_by_query(db, query):
    from models import ScanResult
    results = db.query(ScanResult).filter(
        (ScanResult.title.ilike(f"%{query}%")) |
        (ScanResult.description.ilike(f"%{query}%")) |
        (ScanResult.cve_id.ilike(f"%{query}%"))
    ).all()
    return results