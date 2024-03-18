from fastapi import APIRouter

from src.node.dao import NodeDAO
from src.node.node_schemas import SchemaNode, SchemaDeleteNode, SchemaLinkNodes, SchemaUpdateNode

router = APIRouter(
    prefix="/node/v1",
    tags=["Nodes"]
)


@router.get("/all")
async def get_all_nodes():
    return await NodeDAO.get_all()


@router.post("/create/node")
async def create_node(create: SchemaNode):
    return await NodeDAO.add(workflow_id=create.workflow_id, node_name=create.node_name,
                             text=create.text, status=create.status, condition=create.condition)


@router.post("/create/node/message")
async def create_node(create: SchemaNode):
    return await NodeDAO.add(workflow_id=create.workflow_id, node_name=create.node_name,
                             text=create.text, status=create.status, condition=create.condition)


@router.post("/create/node/condition")
async def create_node(create: SchemaNode):
    return await NodeDAO.add(workflow_id=create.workflow_id, node_name=create.node_name,
                             text=create.text, status=create.status, condition=create.condition)


@router.put("/links-node")
async def links_node(link: SchemaLinkNodes):
    return await NodeDAO.update(id=link.node_id, node_name=link.node_name, workflow_id=link.workflow_id,
                                source=link.source, target=link.target)


@router.put("/update/node")
async def update_node(update: SchemaUpdateNode):
    return await NodeDAO.update(id=update.node_id, node_name=update.new_node_name, workflow_id=update.workflow_id,
                                text=update.new_text, status=update.new_status, condition=update.new_condition)


@router.delete("/delete/node")
async def delete_node(delete: SchemaDeleteNode):
    return await NodeDAO.delete(node_name=delete.node_name, workflow_id=delete.workflow_id)

