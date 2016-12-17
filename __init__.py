from openedoo.core.libs import blueprint

module_coba = blueprint('modul_coba', __name__)
@module_coba.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"
