from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.db_connection import Base


class Workflows(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True)
    workflow_name = Column(String, nullable=False)


class Nodes(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    workflow_id = Column(ForeignKey("workflows.id"))
    node_name = Column(String)
    text = Column(String)
    status = Column(String)
    condition = Column(String)
    source = Column(String)
    target = Column(String)
