from typing import Optional

from pydantic import BaseModel


class SchemaNode(BaseModel):
    workflow_id: int
    node_name: str
    text: Optional[str] = ""
    status: Optional[str] = ""
    condition: Optional[str] = ""


class SchemaDeleteNode(BaseModel):
    node_name: str
    workflow_id: int


class SchemaUpdateNode(BaseModel):
    node_id: int
    workflow_id: int
    new_node_name: str
    new_text: Optional[str] = ""
    new_status: Optional[str] = ""
    new_condition: Optional[str] = ""


class SchemaLinkNodes(BaseModel):
    node_id: int
    node_name: str
    workflow_id: int
    source: str
    target: str
