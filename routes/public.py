from flask import (
    Blueprint,
    render_template
)

from models.post import Post
from models.category import Category

public = Blueprint(
    "public",
    __name__
)


@public.route("/")
def home():

    posts = Post.query.order_by(
        Post.criado_em.desc()
    ).all()

    destaques = Post.query.filter_by(
        destaque=True
    ).all()

    return render_template(
        "home.html",
        posts=posts,
        destaques=destaques
    )


@public.route(
    "/categoria/<slug>"
)
def categoria(slug):

    categoria = Category.query.filter_by(
        slug=slug
    ).first_or_404()

    return render_template(
        "categoria.html",
        categoria=categoria
    )


@public.route("/sobre")
def sobre():

    return render_template(
        "sobre.html"
    )


@public.route("/contato")
def contato():

    return render_template(
        "contato.html"
    )