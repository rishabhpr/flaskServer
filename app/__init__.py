from flask import Flask
from .service import PlayerService

def create_app(csv_file='data/Players.csv'):
    app = Flask(__name__)
    
    # Initialize the PlayerService
    app.player_service = PlayerService(csv_file)
    
    # Register routes
    from . import routes
    routes.init_app(app)
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {'error': 'Resource not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
        
    return app