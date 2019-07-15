from app.authenticator.auth import require_apikey

def main_routes(app):

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>My API</h1><p>Home page</p>"

    @app.route('/api', methods=['GET'])
    @require_apikey
    def api():
        return "<h1>My API</h1><p>Success Api Page</p>"