from app.routes.SlackRoutes import slack_routes
from app.routes.MainRoutes import main_routes

def configure_routes(app):
    main_routes(app)
    slack_routes(app)