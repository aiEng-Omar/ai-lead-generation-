from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String)
    website = Column(String)
    email = Column(String)
    snippet = Column(Text)
    analysis = Column(Text)
    score = Column(Integer)
    outreach = Column(Text)