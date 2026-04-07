import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from fastapi import APIRouter
from sqlalchemy import text
from database import SessionLocal


router = APIRouter()


@router.get("/health")
def healthcheck():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}