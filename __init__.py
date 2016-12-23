#from openedoo.core.libs import blueprint,render_template
from flask import render_template
from flask import Blueprint as blueprint
module_coba = blueprint('modul_coba', __name__,static_url_path='/module_coba/static', static_folder='static',
                          template_folder='static')
@module_coba.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"
@module_coba.route('/<name>')
def hello(name=None):
    return render_template('hello2.html',name=name)