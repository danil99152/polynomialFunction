from sqlalchemy import Column, Integer, String, create_engine, Table, DateTime, \
    MetaData

from settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

metadata_obj = MetaData()

launch_facts = Table(
    "launch_facts",
    metadata_obj,

    Column('id', Integer, primary_key=True, index=True, autoincrement=True),
    Column('launch_date', DateTime, index=True, nullable=False),
    Column('function_name', String, index=True, nullable=False),
    Column('arguments', String, index=True, nullable=False),
    Column('result_parameters', String, index=True, nullable=False),
    Column('result_values', String, index=True, nullable=False),
    Column('error_message', String, index=True),
)
