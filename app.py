import io
import json
import os

import datetime
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

try:
    app.config['GA_TRACKING_ID'] = os.environ['GA_TRACKING_ID']
except:
    print('Tracking ID not set')

resume_pdf_link = 'https://drive.google.com/open?id=0B2BrrDjIiyvmcWp5T194cy00UmM'
 # to do.


@app.route('/')
def index():
    age = int((datetime.date.today() - datetime.date(1988, 4, 22)).days / 365)
    return render_template('home.html', age=age)


@app.route('/projects')
def projects():
    data = get_static_json("static/projects/projects.json")['projects']
    data.sort(key=order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower() for project_tag in project['tags']]]

    return render_template('projects.html', projects=data, tag=tag)


@app.route('/blog')
def blog():
    return redirect("https://medium.com/@beebayoadegunloye", code=302)


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


@app.route('/colourgame')
def colourgame():
    colourgame = get_static_file("static/templates/colourgame.html")
    return render_template('colourgame.html', colourgame=colourgame)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))


if __name__ == "__main__":
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)
