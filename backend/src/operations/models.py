from sqlalchemy import Table, Float, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

application = Table(
    "application",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("object", String, nullable=False),
    Column("hour", Float, nullable=False),
    Column("datetime", TIMESTAMP, nullable=False)
)