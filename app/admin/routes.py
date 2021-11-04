from app.admin import blueprint
from flask import render_template

@blueprint.route('/admin')
def index():
    return render_template('index.html', segment='index')
