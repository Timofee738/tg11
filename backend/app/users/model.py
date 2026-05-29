from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, func

class Users(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )