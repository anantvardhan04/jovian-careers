from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os

password = quote_plus(os.environ['DB_PASSWORD'])
username = os.environ['DB_USERNAME']
host_name = os.environ['DB_HOST']

db_connection_string = f'mysql+pymysql://{username}:{password}@{host_name}/joviancareers'

engine = create_engine(db_connection_string)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    jobs = []
    for result in result_all:
      jobs.append(dict(result))
    return jobs
