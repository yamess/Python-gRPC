from sqlalchemy import Boolean, Column, String, DateTime, func

from configs.env_vars import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True),  server_default=func.now())
    updated_at = Column(DateTime)
    created_by = Column(String)
    updated_by = Column(String)

    def __str__(self):
        return self.email
