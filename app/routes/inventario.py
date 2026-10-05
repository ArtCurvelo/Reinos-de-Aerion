from flask import Blueprint, render_template, session

inventario = Blueprint(
    "inventario",
    __name__,
    url_prefix="/inventario"
)


@inventario.route("/")
def index():
    jogador = session.get("jogador")

    return render_template(
        "inventario.html",
        jogador=jogador
    )