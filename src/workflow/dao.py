from src.dao.base import BaseDAO
from src.models.models import Workflows


class WorkflowDAO(BaseDAO):
    model = Workflows
