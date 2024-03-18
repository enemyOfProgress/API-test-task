from fastapi import APIRouter

from src.node.dao import NodeDAO
from src.node.node_schemas import SchemaNode, SchemaDeleteNode, SchemaLinkNodes, SchemaUpdateNode

router = APIRouter(
    prefix="/node/v1",
    tags=["Nodes"]
)

def returned_response(**data):
    return data


@router.get("/all")
async def get_all_nodes():
    nodes = await NodeDAO.get_all()
    response = Response(status_code=status.HTTP_200_OK)
    return returned_response(code=response.status_code, message="Successfully", details=nodes)


@router.post("/create/node")
async def create_node(create: SchemaNode):
    await NodeDAO.add(workflow_id=create.workflow_id, node_name=create.node_name,
                      text=create.text, status=create.status, condition=create.condition)
    response = Response(status_code=status.HTTP_201_CREATED)
    return returned_response(code=response.status_code, message="Created Successfully")


@router.post("/create/node/message")
async def create_node(create: SchemaNode):
    await NodeDAO.add(workflow_id=create.workflow_id, node_name=create.node_name, text=create.text,
                      status=create.status, condition=create.condition)
    response = Response(status_code=status.HTTP_201_CREATED)
    return returned_response(code=response.status_code, message="Created Successfully")


@router.post("/create/node/condition")
async def create_node(create: SchemaNode):
    await NodeDAO.add(workflow_id=create.workflow_id, node_name=create.node_name,
                      text=create.text, status=create.status, condition=create.condition)
    response = Response(status_code=status.HTTP_201_CREATED)
    return returned_response(code=response.status_code, message="Created Successfully")


@router.put("/links-node")
async def links_node(link: SchemaLinkNodes):
    await NodeDAO.update(id=link.node_id, node_name=link.node_name, workflow_id=link.workflow_id, source=link.source,
                         target=link.target)
    response = Response(status_code=status.HTTP_200_OK)
    return returned_response(code=response.status_code, message="Nodes Linked Successfully")


@router.put("/update/node")
async def update_node(update: SchemaUpdateNode):
    await NodeDAO.update(id=update.node_id, node_name=update.new_node_name, workflow_id=update.workflow_id,
                         text=update.new_text, status=update.new_status, condition=update.new_condition)
    response = Response(status_code=status.HTTP_200_OK)
    return returned_response(code=response.status_code, message="Updated Successfully")


@router.delete("/delete/node")
async def delete_node(delete: SchemaDeleteNode):
    await NodeDAO.delete(node_name=delete.node_name, workflow_id=delete.workflow_id)
    response = Response(status_code=status.HTTP_200_OK)
    return returned_response(code=response.status_code, message="Deleted Successfully")
