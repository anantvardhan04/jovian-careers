from flask import Flask
from flask import render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, post_application_to_db

app = Flask(__name__)


@app.route('/')
def helloworld():
    JOBS = load_jobs_from_db()
    return render_template("index.html", jobs=JOBS)


@app.route('/job/<id>')
def list_job(id):
    job = load_job_from_db(id)
    return render_template('jobpage.html', job_details=job)


@app.route("/job/<id>/apply", methods=['POST'])
def applied_job(id):
    application_data = request.form
    job = load_job_from_db(id)
    post_application_to_db(id, application_data)
    return render_template('applied_job.html',
                           applied_job_details=application_data,
                           job_details=job)


# API Routes


@app.route('/api/jobs')
def list_jobs_api():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)


@app.route('/api/job/<id>')
def list_job_api(id):
    job = load_job_from_db(id)
    return jsonify(job)


if (__name__ == "__main__"):
    app.run(debug=True, host='0.0.0.0', port=8080)
