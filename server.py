import os
from flask import Flask
from app.routes import router
try:
    from config.creds import config
except(AttributeError, ModuleNotFoundError) as e:
    config = None

app = Flask(__name__)
app.config["DEBUG"] = True

router.configure_routes(app)

if __name__ == '__main__':
    app.run(port=(os.environ.get("port") or config['port']))
