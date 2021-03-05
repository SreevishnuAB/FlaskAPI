from sqlalchemy import Integer, String, Table, Column, MetaData

Car = Table(
  'car',
  MetaData(),
  Column('id', Integer,primary_key=True),
  Column('name', String),
  Column('year', Integer)
)