from pydantic import BaseModel


class SchemaWorkflow(BaseModel):
    workflow_id: int
    workflow_name: str


