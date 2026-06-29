from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from werkzeug.utils import secure_filename
from slugify import slugify

from models.database import db
from models.post import Post

import os
import uuid

posts = Blueprint(
    "posts",
    __name__
)


def gerar_slug(titulo):

    slug_base = slugify(titulo)

    slug = slug_base

    contador = 1

    while Post.query.filter_by(slug=slug).first():

        slug = f"{slug_base}-{contador}"

        contador += 1

    return slug


@posts.route("/post/<int:id>")
def visualizar(id):

    post = Post.query.get_or_404(id)

    post.visualizacoes += 1

    db.session.commit()

    return render_template(
        "post.html",
        post=post
    )


@posts.route("/admin/posts")
def listar_posts():

    if not session.get("admin"):
        return redirect("/")

    lista = Post.query.order_by(
        Post.criado_em.desc()
    ).all()

    return render_template(
        "admin/posts.html",
        posts=lista
    )


@posts.route(
    "/admin/posts/criar",
    methods=["GET", "POST"]
)
def criar_post():

    if not session.get("admin"):
        return redirect("/")

    if request.method == "POST":

        titulo = request.form["titulo"]
        resumo = request.form["resumo"]
        conteudo = request.form["conteudo"]

        imagem = request.files.get("imagem")

        nome_arquivo = None

        if imagem and imagem.filename:

            extensao = imagem.filename.rsplit(".", 1)[1]

            nome_arquivo = (
                str(uuid.uuid4())
                + "."
                + extensao
            )

            caminho = os.path.join(
                "static",
                "uploads",
                nome_arquivo
            )

            imagem.save(caminho)

        novo = Post(
            titulo=titulo,
            slug=gerar_slug(titulo),
            resumo=resumo,
            conteudo=conteudo,
            imagem_capa=nome_arquivo,
            autor_id=session["user_id"]
        )

        db.session.add(novo)
        db.session.commit()

        return redirect("/admin/posts")

    return render_template(
        "admin/criar_post.html"
    )


@posts.route(
    "/admin/posts/editar/<int:id>",
    methods=["GET", "POST"]
)
def editar_post(id):

    if not session.get("admin"):
        return redirect("/")

    post = Post.query.get_or_404(id)

    if request.method == "POST":

        post.titulo = request.form["titulo"]
        post.resumo = request.form["resumo"]
        post.conteudo = request.form["conteudo"]

        db.session.commit()

        return redirect("/admin/posts")

    return render_template(
        "admin/editar_post.html",
        post=post
    )


@posts.route(
    "/admin/posts/excluir/<int:id>",
    methods=["POST"]
)
def excluir_post(id):

    if not session.get("admin"):
        return redirect("/")

    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    return redirect("/admin/posts")