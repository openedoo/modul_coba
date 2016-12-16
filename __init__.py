from openedoo.core.libs import blueprint

modul_coba = blueprint('modul_coba', __name__)
@modul_coba.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"
