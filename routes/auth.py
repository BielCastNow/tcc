from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models.database import db
from models.user import User

auth = Blueprint(
    "auth",
    __name__
)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        usuario = User.query.filter_by(
            email=email
        ).first()

        if usuario and check_password_hash(
            usuario.senha,
            senha
        ):

            session["user_id"] = usuario.id
            session["admin"] = usuario.admin

            return redirect("/")

        flash("Email ou senha inválidos")

    return render_template(
        "auth/login.html"
    )


@auth.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        existe = User.query.filter_by(
            email=email
        ).first()

        if existe:

            flash("Email já cadastrado")
            return redirect("/cadastro")

        usuario = User(
            nome=nome,
            email=email,
            senha=generate_password_hash(
                senha
            )
        )

        db.session.add(usuario)
        db.session.commit()

        flash("Cadastro realizado")

        return redirect("/login")

    return render_template(
        "auth/cadastro.html"
    )


@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/")