import os
from os.path import join, dirname

from dotenv import load_dotenv
from sqlalchemy import create_engine, engine
from sqlalchemy.sql import text


_dotenv_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(_dotenv_path)

class Database:

  def __init__(self) -> None:
    query = text("""CREATE TABLE IF NOT EXISTS car(id SERIAL PRIMARY KEY, name VARCHAR, year INTEGER)""")
    self.engine = create_engine(os.environ.get("DB_URL"))
    try:
      with self.engine.connect() as conn:
        conn.execute(query)
    except Exception as e:
      print(e)
