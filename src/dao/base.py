from src.database.db_connection import async_session_maker
from sqlalchemy import select, insert, delete, update


class BaseDAO:
    """
    Base class for operation with DB
    """
    model = None

    @classmethod
    async def get_all(cls):
        """
        Get all records from DB
        :return: all record from DB
        """
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_workflow(cls, workflow_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=workflow_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        """
        Add record to DB
        :param data: params that should be added to DB
        """
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, **data):
        """
        Update record in DB
        :param data: record id that should be updated and new values
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=data["id"])
            result = await session.execute(query)
            record_to_delete = result.scalars().all()
            id_to_update = [record.id for record in record_to_delete]
            query = update(cls.model).where(cls.model.id == id_to_update[0]).values({**data})
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **data):
        """
        Delete record from DB by ID
        :param data: workflow or node name and workflow ID
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**data)
            result = await session.execute(query)
            record_to_delete = result.scalars().all()
            id_to_delete = [record.id for record in record_to_delete]
            delete_query = delete(cls.model).where(cls.model.id == id_to_delete[0])
            await session.execute(delete_query)
            await session.commit()

