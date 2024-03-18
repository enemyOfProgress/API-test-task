from src.dao.base import BaseDAO
from src.models.models import Nodes


class NodeDAO(BaseDAO):
    model = Nodes
