from flask import Flask
from pathlib import Path

from app.routes.principal import principal
from app.routes.personagem import personagem
from app.routes.inventario import inventario


def create_app():
    base_dir = Path(__file__).resolve().parent.parent

    app = Flask(
        __name__,
        template_folder=base_dir / "frontend" / "templates",
        static_folder=base_dir / "frontend" / "static"
    )

    app.config["SECRET_KEY"] = "chave-temporaria"

    app.register_blueprint(principal)
    app.register_blueprint(personagem)
    app.register_blueprint(inventario)

    return app