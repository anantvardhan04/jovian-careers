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
    result_all = result.all()  # List of sqlalchemy data objects
    jobs = []  # List of maps(dictionary)
    for result in result_all:
      jobs.append(dict(result))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    query = f"SELECT * from jobs where id={id}"
    result = conn.execute(text(query))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


def post_application_to_db(job_id, application_data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    result = conn.execute(query,
                          job_id=job_id,
                          full_name=application_data['full_name'],
                          email=application_data['email'],
                          linkedin_url=application_data['linkedin_url'],
                          education=application_data['education'],
                          work_experience=application_data['work_experience'],
                          resume_url=application_data['resume_url'])
