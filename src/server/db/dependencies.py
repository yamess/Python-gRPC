from configs.env_vars import SessionLocal


def get_db():
    """provide db session to path operation functions"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
