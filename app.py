from flask import Flask
from flask import render_template

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "DevOps Engineer",
    "salary": "Rs 60,00,000",
    "location": "Jaipur, India"
}, {
    "id": 2,
    "title": "Backend Engineer",
    "location": "Bengaluru, India"
}, {
    "id": 3,
    "title": "Business Analyst",
    "salary": "$150,000",
    "location": "San Francisco, USA"
}, {
    "id": 4,
    "title": "Project Manager",
    "salary": "Rs 80,00,000",
    "location": "Mumbai, India"
}]


@app.route('/')
def helloworld():
  return render_template("index.html", jobs=JOBS)


if (__name__ == "__main__"):
  app.run(debug=True, host='0.0.0.0', port=8080)
