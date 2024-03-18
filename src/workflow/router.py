from fastapi import APIRouter
from src.workflow.dao import WorkflowDAO
from src.workflow.workflow_schemas import SchemaWorkflow

router = APIRouter(
    prefix="/workflows/v1",
    tags=["Workflow"]
)


@router.get("/get/all")
async def get_workflows():
    return await WorkflowDAO.get_all()


@router.get("/get/workflow/{workflow_id}")
async def get_workflow(workflow_id: int):
    return await WorkflowDAO.get_workflow(workflow_id)


@router.post("/create")
async def create_workflow(create: SchemaWorkflow):
    return await WorkflowDAO.add(id=create.workflow_id, workflow_name=create.workflow_name)


@router.put("/update/workflow/{w_id}")
async def update_workflow(update: SchemaWorkflow, w_id: int):
    return await WorkflowDAO.update(id=update.workflow_id, workflow_name=update.workflow_name)


@router.delete("/delete/workflow/{w_id}")
async def delete_workflow(delete: SchemaWorkflow, w_id: int):
    return await WorkflowDAO.delete(id=delete.workflow_id, workflow_name=delete.workflow_name)

