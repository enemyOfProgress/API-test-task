from fastapi import APIRouter
from src.workflow.dao import WorkflowDAO
from src.workflow.workflow_schemas import SchemaWorkflow

router = APIRouter(
    prefix="/workflows/v1",
    tags=["Workflow"]
)

def returned_response(**data):
    return data


@router.get("/get/all")
async def get_workflows():
    workflows = await WorkflowDAO.get_all()
    response = Response(status_code=status.HTTP_200_OK)
    return returned_response(code=response.status_code, message="Successfully", details=workflows)


@router.get("/get/workflow/{workflow_id}")
async def get_workflow(workflow_id: int):
    workflow = await WorkflowDAO.get_workflow(workflow_id)
    response = Response(status_code=status.HTTP_200_OK)
    return returned_response(code=response.status_code, message="Successfully", details=workflow)


@router.post("/create")
async def create_workflow(create: SchemaWorkflow):
    await WorkflowDAO.add(id=create.workflow_id, workflow_name=create.workflow_name)
    response = Response(status_code=status.HTTP_201_CREATED)
    return returned_response(code=response.status_code, message="Created Successfully")


@router.post("/run/{workflow_id}")
async def run_workflow(workflow_id: int):
    pass


@router.put("/update/workflow/{w_id}")
async def update_workflow(update: SchemaWorkflow, w_id: int):
    await WorkflowDAO.update(id=update.workflow_id, workflow_name=update.workflow_name)
    response = Response(status_code=status.HTTP_201_CREATED)
    return returned_response(code=response.status_code, message="Updated Successfully")


@router.delete("/delete/workflow/{w_id}")
async def delete_workflow(delete: SchemaWorkflow, w_id: int):
    await WorkflowDAO.delete(id=delete.workflow_id, workflow_name=delete.workflow_name)
    response = Response(status_code=status.HTTP_201_CREATED)
    return returned_response(code=response.status_code, message="Deleted Successfully")
