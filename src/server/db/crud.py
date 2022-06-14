from typing import Optional, Union

from jose import jwt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import db.user_schema as sc
import db.user_model as model
from configs.env_vars import SECRET_KEY, ALGORITHM
from utils.auth import hash_password, verify_password
import logging
import uuid
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def create_user(session: Session, user: sc.CreateUserRequest) -> sc.CreateUserResponse:
    user.password = hash_password(user.password)
    data = {k: v for k, v in user.dict().items()}
    data["id"] = str(uuid.uuid4())
    db_user = model.User(**data)
    try:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except IntegrityError as e:
        logger.error(e)
    finally:
        session.close()


def get_user(session: Session, user_id: str):
    try:
        user = session.query(model.User).filter(model.User.id == user_id).first()
        return user
    finally:
        session.close()


def get_user_by_email(session: Session, email: str):
    try:
        user = session.query(model.User).filter(model.User.email == email).first()
        return user
    finally:
        session.close()


def update_user(session: Session, data):
    try:
        user = session.query(model.User).filter(model.User.id == data.id).first()
        user.email = data.email
        user.is_active = data.is_active
        user.is_admin = data.is_admin
        user.updated_at = datetime.utcnow()

        session.flush()
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        logger.error(e)
    finally:
        session.close()


def update_pwd(session: Session, data):
    try:
        user = session.query(model.User).filter(model.User.id == data.id).first()
        if not verify_password(
            plain_password=data.password, hashed_password=user.password
        ):
            raise ValueError("Wrong password")

        user.password = hash_password(data.new_password)
        user.updated_at = datetime.utcnow()

        session.flush()
        session.commit()
        session.refresh(user)
        return user
    finally:
        session.close()


def delete_user(session: Session, user_id: str):
    try:
        session.query(model.User).filter(model.User.id == user_id).delete()
        session.commit()
    except Exception as e:
        raise e
    finally:
        session.close()


def authenticate(session, auth_data: dict) -> Union[bool, model.User]:
    user = get_user_by_email(session, auth_data["email"])
    if not user:
        return False
    if not verify_password(
        plain_password=auth_data["password"], hashed_password=user.password
    ):
        return False
    return user


def create_access_token(to_encode: dict, expires_delta: Optional[int] = None):
    data = to_encode.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    data.update({"exp": expire, "iat": datetime.utcnow(), "nbf": datetime.utcnow()})
    encoded_jwt = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
