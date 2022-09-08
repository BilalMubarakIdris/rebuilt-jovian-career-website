from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
}]


@app.route('/')
def home_page():
    return render_template("index.html", jobs=JOBS, company_name="Jovian")


@app.route('/jobs/data_analyst')
def data_analyst():
    return render_template("data_analyst.html")


@app.route('/jobs/data_scientist')
def data_scientist():
    return render_template("data_scientist.html")


@app.route('/jobs/frontend_engineer')
def frontend_engineer():
    return render_template("frontend_engineer.html")


@app.route('/jobs/backend_engineer')
def backend_engineer():
    return render_template("backend_engineer.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/api/jobs')
def jobs_api():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
