from flask import Flask
from pathlib import Path
from app.routes.principal import principal

def create_app():
    base_dir = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=base_dir / "frontend" / "templates"
    )
    
    app.register_blueprint(principal)
    return app