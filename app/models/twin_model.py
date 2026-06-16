from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Twin(Base):
    __tablename__ = "twins"

    id = Column(Integer, primary_key=True, index=True)
    twin_name = Column(String(100), nullable=False)
    brand_description = Column(Text, nullable=False)